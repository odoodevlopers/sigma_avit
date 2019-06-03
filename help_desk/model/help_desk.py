from odoo import fields, models

class help_desk(models.Model):
    _name = 'help.desk'

    name = fields.Char('Name')
