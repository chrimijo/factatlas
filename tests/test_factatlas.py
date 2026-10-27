"""Local regression checks / Tests locaux. No network and no model evaluation."""
import copy
import csv
import importlib.util
import json
import math
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import audit_scores as audit
import validate_package as package

class ArithmeticTests(unittest.TestCase):
    def setUp(self):
        self.fr=json.loads((ROOT/'assets/exemple-scores.json').read_text())
        self.en=json.loads((ROOT/'assets/en/exemple-scores.json').read_text())

    def test_legacy_and_english_equivalent(self):
        for data in [self.fr,self.en]:
            conf,cov,rows=audit.summarize(data)
            self.assertAlmostEqual(conf,86.0)
            self.assertAlmostEqual(cov,69.0)
            self.assertEqual(sum(x[1] for x in rows),100)

    def test_distinct_confidence_and_coverage(self):
        data={'sections':[{'name':'Evidence','weight':100,'confidence':95,'coverage':40}]}
        self.assertEqual(audit.summarize(data)[:2],(95,40))

    def test_reject_invalid_scores(self):
        for value in [True,False,-1,101,None,'90',float('nan'),float('inf'),10**400]:
            for key in ['poids','confiance','couverture']:
                data=copy.deepcopy(self.fr); data['sections'][0][key]=value
                with self.subTest(value=str(value),key=key), self.assertRaises(ValueError):
                    audit.summarize(data)

    def test_reject_bad_weights(self):
        self.en['sections'][0]['weight']=19
        with self.assertRaises(ValueError): audit.summarize(self.en)

    def test_reject_partial_or_missing_scores(self):
        del self.fr['sections'][0]['couverture']
        with self.assertRaises(ValueError): audit.summarize(self.fr)

    def test_reject_mixed_schemas(self):
        self.fr['sections'][1]=self.en['sections'][1]
        with self.assertRaises(ValueError): audit.summarize(self.fr)

    def test_reject_bilingual_duplicate_fields(self):
        self.en['sections'][0]['poids']=20
        with self.assertRaises(ValueError): audit.summarize(self.en)

    def test_reject_invalid_structure(self):
        for data in [None,[],{}, {'sections':[]},{'sections':[None]}, {'sections':'bad'}]:
            with self.subTest(data=data),self.assertRaises(ValueError): audit.summarize(data)

    def test_reject_invalid_names(self):
        for name in ['', ' ',None,22]:
            self.en['sections'][0]['name']=name
            with self.assertRaises(ValueError): audit.summarize(self.en)

class CommandTests(unittest.TestCase):
    def run_cli(self,*args):
        return subprocess.run([sys.executable,str(ROOT/'scripts/audit_scores.py'),*args],
                              capture_output=True,text=True,cwd=ROOT)

    def test_french_output(self):
        p=self.run_cli('--lang','fr','assets/exemple-scores.json')
        self.assertEqual(p.returncode,0,p.stderr)
        self.assertIn('confiance=86,00 %',p.stdout)
        self.assertIn('couverture=69,00 %',p.stdout)
        self.assertNotIn('confidence=',p.stdout)

    def test_english_output(self):
        p=self.run_cli('--lang','en','assets/en/exemple-scores.json')
        self.assertEqual(p.returncode,0,p.stderr)
        self.assertIn('confidence=86.00%',p.stdout)
        self.assertIn('coverage=69.00%',p.stdout)
        self.assertNotIn('confiance=',p.stdout)

    def test_output_override_independent_of_input_schema(self):
        p=self.run_cli('--lang=en','assets/exemple-scores.json')
        self.assertEqual(p.returncode,0,p.stderr)
        self.assertIn('TOTAL: confidence=86.00%',p.stdout)

    def test_metadata_language(self):
        p=self.run_cli('assets/en/exemple-scores.json')
        self.assertEqual(p.returncode,0)
        self.assertIn('TOTAL:',p.stdout)

    def test_schema_language_without_metadata(self):
        data=json.loads((ROOT/'assets/en/exemple-scores.json').read_text()); del data['lang']
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/'scores.json'; path.write_text(json.dumps(data))
            p=self.run_cli(str(path))
            self.assertEqual(p.returncode,0,p.stderr)
            self.assertIn('TOTAL:',p.stdout)

    def test_localized_errors(self):
        for lang,label in [('fr','ERREUR'),('en','ERROR')]:
            p=self.run_cli('--lang',lang,'does-not-exist.json')
            self.assertEqual(p.returncode,1)
            self.assertTrue(p.stderr.startswith(label))
            self.assertNotIn('Traceback',p.stderr)

    def test_language_conflicts_and_invalid_values(self):
        for args in [['--lang','de'],['--lang'],['--lang','en','--lang','fr']]:
            p=self.run_cli(*args,'assets/exemple-scores.json')
            self.assertEqual(p.returncode,2)
            self.assertNotIn('TOTAL:',p.stdout)

    def test_identical_repeated_flags(self):
        p=self.run_cli('--lang','en','--lang=en','assets/en/exemple-scores.json')
        self.assertEqual(p.returncode,0,p.stderr)

    def test_duplicate_json_keys_and_bad_json(self):
        for contents in ['{"sections":[],"sections":[]}', '{broken']:
            with tempfile.TemporaryDirectory() as d:
                path=Path(d)/'bad.json';path.write_text(contents)
                p=self.run_cli('--lang','en',str(path))
                self.assertEqual(p.returncode,1)
                self.assertTrue(p.stderr.startswith('ERROR:'))

    def test_invalid_json_language(self):
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/'bad.json';path.write_text('{"lang":"de","sections":[]}')
            p=self.run_cli(str(path));self.assertEqual(p.returncode,1)

    def test_help_both_languages(self):
        for lang,label in [('fr','fichier.json'),('en','file.json')]:
            p=self.run_cli('--lang',lang,'--help')
            self.assertEqual(p.returncode,0)
            self.assertIn(label,p.stdout)

class BundleTests(unittest.TestCase):
    def test_structure_pairs_and_links(self):
        self.assertEqual(package.validate(),[])

    def test_csv_provenance_and_no_duplicate_headers(self):
        for prefix in ['assets','assets/en']:
            for name in ['registre-preuves.csv','registre-contradictions.csv']:
                with (ROOT/prefix/name).open() as f: fields=next(csv.reader(f))
                self.assertEqual(len(fields),len(set(fields)))
                if prefix.endswith('en'):
                    self.assertIn('source_language',fields)
                    self.assertIn('original_consulted',fields)
                else:
                    self.assertIn('langue_source',fields)
                    self.assertIn('original_consulte',fields)

    def test_identity_precedes_configuration(self):
        for prefix in ['assets','assets/en']:
            text=(ROOT/prefix/'gabarit-fiche.md').read_text()
            heading='## Configuration' if prefix=='assets' else '## Research configuration'
            self.assertLess(text.index('## 1. Identification'),text.index(heading))

    def test_validator_missing_translation_is_detected(self):
        # Exercise a real packaging failure in an isolated copy.
        import shutil
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'factatlas';shutil.copytree(ROOT,root)
            (root/'references/en/modules/pays.md').unlink()
            self.assertIn('references/en/modules/pays.md',package.validate(root))

if __name__=='__main__': unittest.main()
