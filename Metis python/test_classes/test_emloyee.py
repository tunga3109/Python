#УПР 11.3 стр 235
import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.tunga = Employee('tunga','chan',300)
    
    def test_give_default_raise(self):
        self.tunga.give_raise(300)
        self.assertEqual(self.tunga.salary, 600)

    def test_give_custom_raise(self):
        self.tunga.give_raise()
        self.assertEqual(self.tunga.salary, 5300)
    

if __name__ == '__main__':
    unittest.main()