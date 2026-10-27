#!/usr/bin/env python3
"""Validate an extracted skill package / Valider le dossier extrait. Python standard only."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
MODULES = ['personnalites','entreprises','marques','produits','lieux','monuments','pays']
SPECIALITIES = ['moteurs-automobiles','montres','technologies-numeriques']
SHARED = ['index-modules','sources-wikipedia','contradictions-chiffrees','routage-modeles',
          'indices-documentaires','controle-qualite','langues']

def validate(root=ROOT):
    errors = []
    required = ['SKILL.md','README.md','README.en.md','CHANGELOG.md','CHANGELOG.en.md','VERSION',
                'scripts/audit_scores.py','scripts/validate_package.py','tests/test_factatlas.py']
    for prefix in ['references/', 'references/en/']:
        required += [prefix+x+'.md' for x in SHARED]
        required += [prefix+'modules/'+x+'.md' for x in MODULES]
        required += [prefix+'specialites/'+x+'.md' for x in SPECIALITIES]
    for prefix in ['assets/', 'assets/en/']:
        required += [prefix+x for x in ['gabarit-fiche.md','registre-preuves.csv',
                                       'registre-contradictions.csv','exemple-scores.json']]
    for prefix in ['examples/', 'examples/en/']:
        required += [prefix+x+'.md' for x in ['tests-fonctionnels','tests-bilingues',
                                            'exemple-registre-contradictions']]
    for name in required:
        if not (root/name).is_file():
            errors.append(name)
    if (root/'VERSION').is_file() and (root/'VERSION').read_text().strip() != '1.1.0':
        errors.append('VERSION != 1.1.0')
    if (root/'SKILL.md').is_file():
        skill = (root/'SKILL.md').read_text(encoding='utf-8')
        if not re.match(r'\A---\nname: fact-atlas\ndescription: [^\n]+\n---\n',skill):
            errors.append('SKILL.md: frontmatter')
        for name in ['references/langues.md','references/en/langues.md','assets/en/gabarit-fiche.md']:
            if name not in skill:
                errors.append('SKILL.md: '+name)
    for name in ['SKILL.md','README.md','README.en.md','CHANGELOG.md','CHANGELOG.en.md']:
        if (root/name).is_file() and '1.1.0' not in (root/name).read_text():
            errors.append(name+': 1.1.0')
    for p in root.rglob('*.md'):
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
            if '://' in target or target.startswith('#'):
                continue
            resolved = (p.parent/target.split('#')[0]).resolve()
            if not resolved.is_relative_to(root.resolve()) or not resolved.exists():
                errors.append(str(p.relative_to(root))+': '+target)
    return errors


def main():
    args = sys.argv[1:]
    lang = 'en' if 'en' in args or '--lang=en' in args else 'fr'
    valid = args in ([],['--lang','fr'],['--lang','en'],['--lang=fr'],['--lang=en'])
    if not valid:
        print('Usage: python3 scripts/validate_package.py [--lang fr|en]',file=sys.stderr)
        return 2
    errors = validate()
    if errors:
        print(('ERROR: missing or invalid resources' if lang=='en' else 'ERREUR : ressources absentes ou invalides'),file=sys.stderr)
        for error in errors:
            print(error,file=sys.stderr)
        return 1
    print('OK — FactAtlas v1.1.0: structure, language pairs and local links valid.' if lang=='en'
          else 'OK — FactAtlas v1.1.0 : structure, paires linguistiques et liens locaux valides.')
    return 0

if __name__=='__main__':
    raise SystemExit(main())
