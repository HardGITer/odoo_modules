from odoo.tests import common
from odoo.tests import tagged
from odoo.addons.queue_job.job import (
    Job,
    RETRY_INTERVAL,
    PENDING,
    ENQUEUED,
    STARTED,
    DONE,
    FAILED,
    identity_exact,
)


@tagged('post_install')
class TestFunctions(common.TransactionCase):

    def setup(self):
        self.method = self.env['students.person'].calculate_students_count

    def test_new_job(self):
        test_job = Job(self.env['students.person'].calculate_students_count)
        self.assertEqual(test_job.func, self.env['students.person'].calculate_students_count)
        print('queue_job function passed the tests')

