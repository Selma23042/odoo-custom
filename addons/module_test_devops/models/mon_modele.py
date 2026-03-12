try:
    from odoo import models, fields

    class MonModele(models.Model):
        _name = 'mon.modele'
        _description = 'Modele de test DevOps'

        name = fields.Char(string='Nom', required=True)
        description = fields.Text(string='Description')
        actif = fields.Boolean(string='Actif', default=True)
        date_creation = fields.Date(
            string='Date création',
            default=fields.Date.today
        )

except ImportError:
    pass