class Student:
    def __init__(self, name, year, average_score):
        self.name = name
        self.year = year
        self.average_score = average_score

    def __lt__(self, other):
        if self.average_score == other.average_score:
            pass





