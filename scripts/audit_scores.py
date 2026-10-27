#!/usr/bin/env python3
"""FactAtlas arithmetic checks / Contrôle arithmétique. No external dependencies."""
from __future__ import annotations
import json
import math
import sys
from pathlib import Path

FIELDS = {'fr': ('nom', 'poids', 'confiance', 'couverture'),
          'en': ('name', 'weight', 'confidence', 'coverage')}
MESSAGES = {
 'fr': {
  'usage': 'Usage : python3 scripts/audit_scores.py [--lang fr|en] fichier.json',
  'option': 'Paramètres invalides : fournir un fichier et au plus une langue cohérente fr ou en.',
  'language': 'Langue JSON invalide : fr ou en attendu.',
  'object': "Un objet JSON avec un tableau 'sections' non vide est requis.",
  'section': 'Section {n} incorrecte ou sans nom textuel.',
  'schema': 'Utiliser un seul schéma homogène : français ou anglais, sans clés bilingues doublées.',
  'score': '{field} : un nombre fini entre 0 et 100 est requis.',
  'weight': 'La somme des poids doit être 100 %, valeur : {total} %.',
  'read': 'Impossible de lire le fichier JSON ; vérifier accès, encodage et syntaxe.',
  'duplicate': 'Clés JSON doublées interdites.',
  'row': '{name} : poids={weight} %, confiance={confidence} %, couverture={coverage} %',
  'total': 'GLOBAL : confiance={confidence} % ; couverture={coverage} %',
  'note': 'NOTE : calcul arithmétique uniquement ; scores éditoriaux, non probabilités statistiques.',
  'error': 'ERREUR : ',
 },
 'en': {
  'usage': 'Usage: python3 scripts/audit_scores.py [--lang fr|en] file.json',
  'option': 'Invalid arguments: provide one file and at most one consistent language, fr or en.',
  'language': 'Invalid JSON language: expected fr or en.',
  'object': "A JSON object with a nonempty 'sections' array is required.",
  'section': 'Invalid section {n} or missing text name.',
  'schema': 'Use one homogeneous schema: French or English, without duplicate bilingual keys.',
  'score': '{field}: a finite number between 0 and 100 is required.',
  'weight': 'Weights must total 100%; found {total}%.',
  'read': 'Cannot read the JSON file; check access, encoding and syntax.',
  'duplicate': 'Duplicate JSON keys are not allowed.',
  'row': '{name}: weight={weight}%, confidence={confidence}%, coverage={coverage}%',
  'total': 'TOTAL: confidence={confidence}%; coverage={coverage}%',
  'note': 'NOTE: arithmetic only; editorial scores, not statistical probabilities.',
  'error': 'ERROR: ',
 }
}

def number(value, lang, decimals=None):
    text = f'{value:.{decimals}f}' if decimals is not None else f'{value:g}'
    return text.replace('.', ',') if lang == 'fr' else text


def fail(code, lang='fr', **kwargs):
    raise ValueError(MESSAGES[lang][code].format(**kwargs))


def schema_language(data):
    if isinstance(data, dict) and isinstance(data.get('sections'), list):
        for row in data['sections']:
            if isinstance(row, dict):
                if any(k in row for k in FIELDS['en']):
                    return 'en'
                if any(k in row for k in FIELDS['fr']):
                    return 'fr'
    return 'fr'


def validate_score(value: object, label: str, lang='fr') -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        fail('score', lang, field=label)
    try:
        result = float(value)
    except (OverflowError, ValueError):
        fail('score', lang, field=label)
    if not math.isfinite(result) or not 0 <= result <= 100:
        fail('score', lang, field=label)
    return result


def summarize(data: dict, lang='fr') -> tuple[float, float, list]:
    if not isinstance(data, dict) or not isinstance(data.get('sections'), list) or not data['sections']:
        fail('object', lang)
    schema = schema_language(data)
    keys = FIELDS[schema]
    other = FIELDS['en' if schema == 'fr' else 'fr']
    verified = []
    for i, section in enumerate(data['sections'], 1):
        if not isinstance(section, dict):
            fail('section', lang, n=i)
        if any(k in section for k in other) or not all(k in section for k in keys):
            fail('schema', lang)
        name = section[keys[0]]
        if not isinstance(name, str) or not name.strip():
            fail('section', lang, n=i)
        labels = FIELDS[lang][1:]
        values = [validate_score(section[k], labels[j], lang) for j, k in enumerate(keys[1:])]
        verified.append((name.strip(), *values))
    total = math.fsum(v[1] for v in verified)
    if not math.isclose(total, 100, rel_tol=0, abs_tol=1e-7):
        fail('weight', lang, total=number(total, lang))
    conf = math.fsum(w*c for _, w, c, _ in verified) / total
    cov = math.fsum(w*c for _, w, _, c in verified) / total
    return conf, cov, verified


def parse_args(argv):
    # Parse only real CLI arguments. Prompt-language selection remains the agent's job.
    lang = None
    files = []
    help_requested = False
    invalid = False
    i = 0
    while i < len(argv):
        arg = argv[i]
        if arg == '--lang' or arg.startswith('--lang='):
            if arg == '--lang':
                i += 1
                value = argv[i] if i < len(argv) else None
            else:
                value = arg.split('=', 1)[1]
            if value not in ('fr', 'en') or (lang and value != lang):
                invalid = True
            elif lang is None:
                lang = value
        elif arg in ('-h', '--help'):
            help_requested = True
        elif arg.startswith('-'):
            invalid = True
        else:
            files.append(arg)
        i += 1
    if invalid or (len(files) != 1 and not help_requested):
        return lang or 'fr', None, False, True
    return lang, Path(files[0]) if files else None, help_requested, False


def load_data(path, lang):
    def unique_pairs(pairs):
        result = {}
        for k, v in pairs:
            if k in result:
                fail('duplicate', lang)
            result[k] = v
        return result
    try:
        return json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=unique_pairs)
    except (OSError, UnicodeError, json.JSONDecodeError):
        fail('read', lang)


def main(argv=None):
    explicit, path, help_requested, invalid = parse_args(sys.argv[1:] if argv is None else argv)
    lang = explicit or 'fr'
    if invalid:
        print(MESSAGES[lang]['error'] + MESSAGES[lang]['option'], file=sys.stderr)
        return 2
    if help_requested:
        print(MESSAGES[lang]['usage'])
        return 0
    try:
        data = load_data(path, lang)
        if explicit is None:
            if isinstance(data, dict) and 'lang' in data:
                if data['lang'] not in ('fr', 'en'):
                    fail('language', lang)
                lang = data['lang']
            else:
                lang = schema_language(data)
        conf, cov, rows = summarize(data, lang)
    except ValueError as exc:
        print(MESSAGES[lang]['error'] + str(exc), file=sys.stderr)
        return 1
    for name, weight, confidence, coverage in rows:
        print(MESSAGES[lang]['row'].format(name=name, weight=number(weight,lang),
             confidence=number(confidence,lang), coverage=number(coverage,lang)))
    print(MESSAGES[lang]['total'].format(confidence=number(conf,lang,2), coverage=number(cov,lang,2)))
    print(MESSAGES[lang]['note'])
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
