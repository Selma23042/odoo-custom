try:
    from odoo import models, fields

    class MonModele(models.Model):
        _name = 'mon.modele'
        _description = 'Modele de test DevOps'
        name = fields.Char(string='Nom', required=True)
        description = fields.Text(string='Description')
        actif = fields.Boolean(string='Actif', default=True)
        date_creation = fields.Date(
            string='Date creation',
            default=fields.Date.today
        )

except ImportError:
    pass


class MonModeleSimule:
    def __init__(self, name, description='', actif=True):
        if not name:
            raise ValueError('Le champ name est obligatoire')
        self.name = name
        self.description = description
        self.actif = actif
        self.date_creation = None


class TestMonModele:

    def test_creation_enregistrement(self):
        record = MonModeleSimule(
            name='Test DevOps',
            description='Test pipeline CI/CD'
        )
        assert record.name == 'Test DevOps'
        assert record.actif is True

    def test_champ_obligatoire(self):
        record = MonModeleSimule(name='Salma Test')
        assert record.name == 'Salma Test'

    def test_name_vide_leve_erreur(self):
        try:
            MonModeleSimule(name='')
            assert False, "Devrait lever une erreur"
        except ValueError:
            assert True

    def test_description_par_defaut(self):
        record = MonModeleSimule(name='Test')
        assert record.description == ''

    def test_actif_par_defaut(self):
        record = MonModeleSimule(name='Test')
        assert record.actif is True

    def test_actif_false(self):
        record = MonModeleSimule(name='Test', actif=False)
        assert record.actif is False

    def test_name_none_leve_erreur(self):
        try:
            MonModeleSimule(name=None)
            assert False, "Devrait lever une erreur"
        except (ValueError, TypeError):
            assert True

    def test_description_personnalisee(self):
        record = MonModeleSimule(
            name='Test',
            description='Ma description'
        )
        assert record.description == 'Ma description'