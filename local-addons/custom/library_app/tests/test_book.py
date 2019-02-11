from odoo.tests import TransactionCase


class TestBook(TransactionCase):

    def setUp(self, *args, **kwargs):
        result = super().setUp(*args, **kwargs)
        user_admin = self.env.ref('base.user_admin')
        self.env = self.env(user=user_admin)
        self.Book = self.env['library.book']
        self.book_ode = self.Book.create({
            'name': 'Odoo development essentials',
            'isbn': '879-1-78439-279-6'
        })
        return result

    def test_create(self):
        self.assertEqual(self.book_ode.active, True)

    def test_check_isbn(self):
        self.assertTrue(self.book_ode._check_isbn)