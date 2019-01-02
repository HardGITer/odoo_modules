# from odoo.tests import common
# from odoo.tests import tagged
#
#
# @tagged('post_install')
# class TestProject(common.TransactionCase):
#
#     def test_create_student(self):
#         test_student = self.env['students.person'].create({
#             'name': 'testName',
#             'surname': 'testSurname',
#             'age': 11
#         })
#         self.assertEqual(test_student.name, 'testName')
#         print('success!')
#
#     def test_student_compute_field(self):
#         test_student = self.env['students.person'].create({
#             'name': 'testName',
#             'surname': 'testSurname',
#             'age': 11
#         })
#         self.assertEqual(test_student.age, 18)
#         print('success!')
#
#     def test_edit_student(self):
#         test_student = self.env['students.person'].create({
#             'name': 'testName',
#             'surname': 'testSurname',
#             'age': 11
#         })
#         test_student.write({'name': 'newName'})
#         self.assertEqual(test_student.name, 'newName')
#         print('success!')

#     def test_add_book_to_student(self):
#         test_student = self.env['students.person'].create({
#             'name': 'testName',
#             'surname': 'testSurname',
#             'age': 11
#         })
#         test_book = self.env['students.book'].create({
#             'name': 'testName',
#             'author': 'testAuthor'
#         })
#         test_student.books = test_book
#         self.assertEqual(test_student.name, 'testName')
#         self.assertEqual(test_book.name, 'testName')
#         self.assertEqual(test_student.books.search([('name', '=', 'testName')]), test_book.name)
#         print('Your test was succesfull!')
#
#


import pytest
from odoo.tests import common
from odoo.tests import tagged


class TestProject(object):

    def test_create_student(self):
        test_student = self.env['students.person'].create({
            'name': 'testName',
            'surname': 'testSurname',
            'age': 11
        })
        assert(test_student.name, 'testName')
        print('success!')

    def test_student_compute_field(self):
        test_student = self.env['students.person'].create({
            'name': 'testName',
            'surname': 'testSurname',
            'age': 11
        })
        assert(test_student.age, 18)
        print('success!')

    def test_edit_student(self):
        test_student = self.env['students.person'].create({
            'name': 'testName',
            'surname': 'testSurname',
            'age': 11
        })
        test_student.write({'name': 'newName'})
        assert(test_student.name, 'newName')
        print('success!')

    def test_demo(self):
        x = "this"
        assert 'h' in x



