import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        """create an employee and custom raise amount for use in test case"""
        first = "Hans"
        last = "Zimmer"
        salary = 120000
        self.employee = Employee(first,last,salary)
    
    def test_give_custom_raise(self):
        self.employee.give_custom_raise(37000)
        self.assertEqual(self.employee.salary,157000)
    
    def test_give_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary,125000)

if __name__ == '__main__':
    unittest.main()