from odoo import fields, models


class Company(models.Model):
    _inherit = 'res.company'

    product_type = fields.Selection(
        [('tile', 'Tile'),
         ('heater', 'Heater'),
         ('dye', 'Dye')],
        'Product Type',
        default='tile', required=True)
    # product_type = fields.Char('Product Type', required=True)
    delivered_products_ids = fields.One2many(
        'construction.product',
        'supplier_company_id',
        string='Delivered Products')
