from odoo import fields, models


class Company(models.Model):
    _inherit = 'res.company'

    product_type = fields.Selection(
        [('tile', 'Tile'),
         ('heater', 'Heater'),
         ('dye', 'Dye')],
        'Supplier Specification',
        default='tile', required=True)
    delivered_products_ids = fields.One2many(
        'product.product',
        'supplier_company_id',
        string='Delivered Products')
