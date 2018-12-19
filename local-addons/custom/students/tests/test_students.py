from odoo.tests import common


class TestProject(common.TransactionCase):

    def test_create_student(self):
        test_student = self.env['students.person'].create({
            'name': 'testName',
            'surname': 'testSurname',
            'age': 11
        })
        self.assertEqual(test_student.name, 'testName')
        print('success!')