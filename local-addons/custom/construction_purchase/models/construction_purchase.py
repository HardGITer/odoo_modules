from odoo import models, api
import logging


class Purchase(models.Model):
    _inherit = 'purchase.order'
    _logger = logging.getLogger('purchase_logger')

    # @api.model
    # def create(self, vals):
    #     Product = self.env['product.product']
    #     # if vals.get('product_qty'):
    #     product = Product.search([('product_id.packaging_ids.name', '=', vals['order_line.product_id.packaging_ids.name'])])
    #     super(Product, self).write(product)
    #     vals['order_line.product_qty'] = 4
    #     return super(Purchase, self).create(vals)
