import unittest
import testwork
import datetime as dt


class WorkTest(unittest.TestCase):
    def test_base(self):
        self.assertEqual(testwork.count_hours('test.xml'),
                         {'21-12-2011': dt.timedelta(hours=18, minutes=26, seconds=25),
                          '22-12-2011': dt.timedelta(hours=4, minutes=28, seconds=15),
                          '23-12-2011': dt.timedelta(hours=12, minutes=25, seconds=20)
                         })

    def test_employees(self):
        self.assertEqual(testwork.count_hours('test.xml', by_employee=True),
                         {'21-12-2011': {'i.ivanov':    dt.timedelta(hours=8, minutes=48, seconds=15),
                                         'a.stepanova': dt.timedelta(hours=9, minutes=38, seconds=10)},
                          '22-12-2011': {'i.ivanov': dt.timedelta(hours=4, minutes=28, seconds=15)},
                          '23-12-2011': {'a.petrova': dt.timedelta(hours=6, minutes=23, seconds=5),
                                         'i.ivanov': dt.timedelta(hours=6, minutes=2, seconds=15)}
                         })

    def test_extended(self):
        self.assertEqual(testwork.count_hours('test.xml', by_employee=True, start_date='22-12-2011', end_date='22-12-2011'),
                         {'22-12-2011': {'i.ivanov': dt.timedelta(hours=4, minutes=28, seconds=15)}})


if __name__ == '__main__':
    unittest.main()
