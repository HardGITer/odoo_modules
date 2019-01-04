from odoo.tests import common
from odoo.tests import tagged


@tagged('post_install')
class TestFunctions(common.TransactionCase):

    def test_calculate_students_with_delay(self):
        # self.cr.execute('delete from queue_job')
        job_instance = self.env['students.person'].with_delay().calculate_students_count()
        self.assertTrue(job_instance)
        result = job_instance.perform()
        self.assertEquals(
            result,
            len(self.env['students.person'].search([]))
        )
        print('queue_job function passed the tests')


