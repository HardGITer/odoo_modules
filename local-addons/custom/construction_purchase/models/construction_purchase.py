from odoo import models, api


class Purchase(models.Model):
    _inherit = 'purchase.order'

    @api.model
    def create(self, vals):
        vals['order_line.product_qty'] = 5
        Product = self.env['product.product']
        if vals.get('order_line.product_qty'):
            product = Product.search([('product_id', '=', vals.get('order_line.product_id'))])
            product.write({'count_in_dock': product.count_in_dock - vals['order_line.product_qty']})
        return super(Purchase, self).create(vals)

    @api.multi
    def write(self, vals):
        Product = self.env['product.product']
        Purchase = self.env['purchase.order']
        purchase = Purchase.search([('name', '=', vals.get('name'))])
        old_product_count = purchase.order_line.product_qty
        if vals.get('order_line.product_qty') != old_product_count:
            difference = vals.get('order_line.product_qty') - old_product_count
            product = Product.search([('product_id', '=', vals.get('order_line.product_id'))])
            product.write({'count_in_dock': product.count_in_dock - difference})
        return super(Purchase, self).write(vals)
