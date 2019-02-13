from odoo import fields, models


class Company(models.Model):
    _inherit = 'res.company'

    # product_type = fields.Selection(
    #     [('0', 'Tile'),
    #      ('1', 'Heater'),
    #      ('2', 'Dye')],
    #     'Product Type',
    #     default='0')
    product_type = fields.Char('Product Type', required=True)
    delivered_products_ids = fields.One2many(
        'construction.product',
        'supplier_company_id',
        string='Delivered Products')
