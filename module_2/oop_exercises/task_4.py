class Employee:
    def __init__(self, name, department, manager, skills, english_lvl, salary):
        self.name = name
        self.department = department
        self.manager = manager
        self.skills = skills
        self._english_lvl = english_lvl
        self.__salary = salary

    def get_info(self):
        return f"\nName: {self.name}\nDepartment: {self.department}\nManager: {self.manager}\nSkills: {self.skills}" \
               f"\nEnglish level: {self._english_lvl}\nSalary: {self.__salary}"

    def get_salary(self):
        return self.__salary


class Department:
    def __init__(self, employees: set):
        self.employees = employees

    def add_employee(self, employee):
        self.employees.add(employee)
        return f"\nA new employee '{str(employee.name)}' had hired"  # Use str(employee.name)

    def remove_employee(self, employee):
        self.employees.remove(employee)
        return f"{str(employee.name)} employee had fired"

    def display_employees(self):
        for employee in self.employees:
            print(employee.get_info())

    def average_salary(self):
        salaries = 0
        for employee in self.employees:
            salaries += employee.get_salary()
        return f"\nSum of the salaries is: {salaries}\nAn average salary is: {salaries // len(self.employees)}"


employee_1 = Employee("Maxim Kostenko", "IT", "Iryna Zaiets", "programming, basketball, swimming", "A2+", 3000)
employee_2 = Employee("Ura Perepelko", "Sailor", "OSM ", "cinephile, karate, gaming", "B1", 4000)
employee_3 = Employee("Sergiy Kucherenko", "YouTube Content Creation", "Isn't specified",
                      "video production, karate, polish language", "A2", 3500)

departament = Department({employee_1, employee_2, employee_3})
departament.display_employees()
print(departament.remove_employee(employee_1))
print(departament.add_employee(employee_1))
print(departament.average_salary())
