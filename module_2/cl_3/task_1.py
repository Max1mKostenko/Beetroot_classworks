class Person:
    def __init__(self, name, age, faculty, grades: dict, **grade):
        self.name = name
        self.age = age
        self.faculty = faculty
        self.grades = grades
        self.grade = grade

    def display_info(self):
        return f"Information about Student\n" \
               f"Name: {self.name}\n" \
               f"Age: {self.age}\n" \
               f"Faculty: {self.faculty}\n" \
               f"Grades: {self.grades}\n" \
               f"Grades: {self.grade}"

    def calculate_average_grade(self):
        """
        Do it with a dictionary
        """
        # sum_of_grades = sum(self.grades.values())
        # quantity_of_grades = len(self.grades)
        # average_grade = sum_of_grades / quantity_of_grades
        # return f"An average grade: {sum_of_grades} / {quantity_of_grades} = {average_grade}"

        """
        Do it with a **kwargs
        """
        sum_of_grades = sum(self.grade.values())
        quantity_of_grades = len(self.grade)
        average_grade = sum_of_grades / quantity_of_grades
        return f"An average grade: {sum_of_grades} / {quantity_of_grades} = {average_grade}"


person = Person("Maxim", 15, "Computer Science", {"math": 87, "science": 91, "biology": 43, "pe": 83},
                math=87, science=91, biology=43, pe=83)
print(person.display_info())
print(person.calculate_average_grade())
