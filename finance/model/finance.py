from odoo import fields, models

class finance_model(models.Model):
    _name = 'finance.model'

    name = fields.Char('Name')
