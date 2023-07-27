import json

class Employee:
    def __init__(self, name: str, departament, manager: str, skills: list, english_level: str, salary: str):
        self.name = name
        self.departament = departament
        self.manager = manager
        self.skills = skills
        self._english_level = english_level
        self.__salary = salary


class Departament:
    def

