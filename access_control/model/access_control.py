from odoo import fields, models

class access_control(models.Model):
    _name = 'access.control'

    name = fields.Char('Name')
