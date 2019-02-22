from odoo import fields, models, api


class Product(models.Model):
    _inherit = 'product.product'
    _sql_constraints = [
        ('construction_product_technical_name_uq',
         'UNIQUE (technical_name)',
         'Technical name should be unique.'),
    ]

    @api.depends('supplier_company_id.product_type')
    def _compute_type(self):
        for product in self:
            product.product_type = product.supplier_company_id.product_type

    supplier_company_id = fields.Many2one('res.company', string="Supplier")
    product_type = fields.Char('Supplier Specification', compute='_compute_type', readonly=True, store=True)
    count_in_dock = fields.Float('Count Of Product In Dock', default=0)

    @api.multi
    def write_off_product(self):
        for product in self:
            product.count_in_dock -= 1
