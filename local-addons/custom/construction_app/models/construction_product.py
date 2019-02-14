from odoo import fields, models, api
from openerp.exceptions import ValidationError


class Product(models.Model):
    _name = 'construction.product'
    _sql_constraints = [
        ('construction_product_technical_name_uq',
         'UNIQUE (technical_name)',
         'Technical name should be unique.'),
    ]

    @api.depends('supplier_company_id.product_type')
    def _compute_type(self):
        for product in self:
            product.product_type = product.supplier_company_id.product_type
            print(str(product.supplier_company_id.product_type))


    name = fields.Char('Product Name', required=True)
    technical_name = fields.Char('Product Technical Name', required=True)
    price = fields.Monetary('Price', 'currency_id')
    currency_id = fields.Many2one('res.currency')
    supplier_company_id = fields.Many2one('res.company', string="Supplier")
    product_type = fields.Char(compute='_compute_type', readonly=True, store=True)
    count_in_dock = fields.Integer('Count Of Product In Dock', default=0)

    @api.multi
    def write_off_product(self):
        for product in self:
            product.count_in_dock -= 1

    @api.constrains('price')
    def price_validation(self):
        for product in self:
            if product.price < 0:
                raise ValidationError('''Price Can't be less hen 0.''')
