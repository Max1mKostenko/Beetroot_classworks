class Employee:
    def __init__(self, name, position, salary, days_attended):
        self.name = name
        self.position = position
        self.salary = salary
        self.days_attended = days_attended

    def employee_reports(self):
        print(f'Name: {self.name} \nPosition: {self.position} \nSalary per year: {self.salary}')

    def tracking_attendance(self, days_attended):
        if days_attended < 20:
            print(f'{self.name} has low work attendance!')
        else:
            print(f'{self.name} has a great work attendance!')


class Manager(Employee):
    def __init__(self, name, position, salary, days_attended, current_projects):
        super().__init__(name, position, salary, days_attended)
        self.current_projects = current_projects

    def work_load(self):
        print(f'He currently has {self.current_projects} projects')

    def salary_bonuses(self):
        if self.current_projects > 3:
            salary_bonus = self.salary * .5
            print(f'{self.name} salary_bonuses is: {salary_bonus}')


class Developer(Employee):
    def __init__(self, name, position, salary, days_attended, tech_stack):
        super().__init__(name, position, salary, days_attended)
        self.tech_stack = tech_stack

    def full_tech_stack(self):
        print(f'This is {self.name}, he is a {self.position}. His tech stack is:')
        for item in self.tech_stack:
            print(item)

    def salary_bonuses(self):
        if len(self.tech_stack) >= 5:
            salary_bonus = self.salary * .5
            print(f'{self.name} salary_bonuses is: {salary_bonus}')


class Salesperson(Employee):
    def __init__(self, name, position, salary, days_attended, amount_of_leads, revenue):
        super().__init__(name, position, salary, days_attended)
        self.amount_of_leads = amount_of_leads
        self.revenue = revenue

    def avg_revenue_per_lead(self):
        avg_revenue = self.revenue / self.amount_of_leads
        print(f'For {self.name}: Average revenue per lead is {round(avg_revenue, 2)} $')

    def salary_bonuses(self):
        if self.revenue > 150000:
            salary_bonus = self.salary * .5
            print(f'{self.name} salary_bonuses is: {salary_bonus}')


manager = Manager('Adam', 'PM', 71000, 25, 4)
manager.employee_reports()
manager.work_load()
manager.salary_bonuses()
developer = Developer('Tom', 'Python Developer', 92000, 23, ['HTML', 'CSS', 'AJAX', 'jQuery', 'Django'])
developer.employee_reports()
developer.full_tech_stack()
developer.salary_bonuses()
salesperson = Salesperson('John', 'Salesperson', 55000, 24, 18, 354000)
salesperson.employee_reports()
salesperson.avg_revenue_per_lead()
salesperson.salary_bonuses()
