import unittest
from task_1 import Employee, Department


class Test_Employee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("Maxim Kostenko", "IT", "Iryna Zaiets", "programming,"
                                                                         " basketball, swimming", "A2+", 3000)
        self.department = Department

    def get_salary_check(self):
        result = self.get_salary
        self.assertEqual(result, 3000)


test_employee = Test_Employee
print(test_employee)



