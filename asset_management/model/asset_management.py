from odoo import fields, models

class asset_management(models.Model):
    _name = 'asset.management'

    name = fields.Char('Name')
