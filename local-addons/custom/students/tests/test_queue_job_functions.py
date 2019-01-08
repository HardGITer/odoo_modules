from odoo.tests import common
from odoo.tests import tagged
from odoo.addons.queue_job.job import (
    Job,
)
from odoo.addons.queue_job.exception import (
    NoSuchJobError,
)


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
        print('queue_job function passed test_calculate_students_with_delay')

    def test_load(self):
        test_job = Job(self.env['students.person'].calculate_students_count,
                       args=('arg1', 'a'),
                       kwargs={'kwarg1': 'b'},
                       priority=15,
                       description="test description")
        test_job.user_id = 1
        test_job.store()
        job_read = Job.load(self.env, test_job.uuid)
        self.assertEqual(job_read.args, ('arg1', 'a'))
        self.assertEqual(job_read.kwargs, {'kwarg1': 'b'})
        self.assertEqual(job_read.description, "test description")
        self.assertEqual(job_read.priority, 15)
        print('queue_job function passed test_job_load')

    def test_unlink(self):
        test_job = Job(self.env['students.person'].calculate_students_count,
                       args=('arg1', 'a'),
                       kwargs={'kwarg1': 'b'},
                       priority=15,
                       description="test description")
        test_job.store()
        stored = self.env['queue.job'].search([('uuid', '=', test_job.uuid)])
        stored.unlink()
        with self.assertRaises(NoSuchJobError):
            Job.load(self.env, test_job.uuid)
        print('queue_job function passed test_unlink')

    def test_execute(self):
        self.cr.execute('delete from queue_job')
        test_job = Job(self.env['students.person'].calculate_students_count)
        result = test_job.perform()
        self.assertEqual(result, 1)
        print('queue_job function passed test_execute')