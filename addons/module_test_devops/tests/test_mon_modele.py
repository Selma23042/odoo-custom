class MonModeleSimule:
    def __init__(self, name, description='', actif=True):
        if not name:
            raise ValueError('Le champ name est obligatoire')
        self.name = name
        self.description = description
        self.actif = actif


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