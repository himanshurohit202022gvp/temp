from odoo import api,models,fields

class ResPartner(models.Model):
    _inherit = "res.users"
    property_id = fields.One2many('estate.property', 'salesman_id')