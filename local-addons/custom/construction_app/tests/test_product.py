from odoo.tests.common import TransactionCase
from odoo import exceptions


class TestProduct(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestProduct, self).setUp(*args, **kwargs)
        admin_user = self.env.ref('base.user_admin')
        self.Product = self.env['product.product'].sudo(admin_user)
        self.product = self.Product.create({'name': 'test_name', 'technical_name': 'test_technical_name',
                                           'count_in_dock': 3})

    def test_button_write_off_product(self):
        count_in_dock_before = self.product.count_in_dock
        self.product.write_off_product()
        count_in_dock_after = self.product.count_in_dock
        self.assertEqual(count_in_dock_before, count_in_dock_after + 1,
                         'Expected to removing one product.')
        print("write_off_product test successfully completed")

    def test_price_validation_error(self):
        err_product = self.Product.create({'name': 'test_name', 'technical_name': 'test_technical_name',
                                           'count_in_dock': -1})
        self.assertFalse(err_product)

    def test_create_product_vals(self):
        self.assertEqual(self.product.name, 'test_name')
        self.assertEqual(self.product.technical_name, 'test_technical_name')
        self.assertEqual(self.product.count_in_dock, 3)
