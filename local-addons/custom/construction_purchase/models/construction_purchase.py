from odoo import models, api, _
from odoo.exceptions import UserError

class Purchase(models.Model):
    _inherit = 'purchase.order'

    @api.onchange('order_line')
    def compute_product_count_in_dock(self):
        Product = self.env['product.product']
        for line in self.order_line:
            if line.product_id.count_in_dock - line.product_qty < 0:
                raise UserError(_("Count of this product in dock less then inputed value"))
            line.product_id.write({'count_in_dock': line.product_id.count_in_dock - line.product_qty})
