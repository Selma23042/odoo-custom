from odoo.tests.common import TransactionCase


class TestMonModele(TransactionCase):

    def test_creation_enregistrement(self):
        record = self.env['mon.modele'].create({
            'name': 'Test DevOps',
            'description': 'Test pipeline CI/CD'
        })
        self.assertEqual(record.name, 'Test DevOps')
        self.assertTrue(record.actif)

    def test_champ_obligatoire(self):
        record = self.env['mon.modele'].create({
            'name': 'Salma Test'
        })
        self.assertEqual(record.name, 'Salma Test')