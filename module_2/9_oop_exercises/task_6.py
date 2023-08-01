class FitnessTracker:
    def __init__(self, name, age, weight, height, daily_step_count, total_calories_burned):
        self.name = name
        self.age = age
        self._weight = weight
        self._height = height
        self.daily_step_count = daily_step_count
        self.__total_calories_burned = total_calories_burned

    def daily_activity(self):
        return f"{str(self.name).capitalize()} steps today: {self.daily_step_count}"

    def daily_burned_calories(self):
        return f"{str(self.name).capitalize()} burned calories today: {self.__total_calories_burned}"

    def info(self):
        return f"Name: {str(self.name).capitalize()}\nAge: {self.age}\nWeight: {self._weight}\nHeight: {self._height}\n"


user_1 = FitnessTracker("Max", 15, 63, 175, 2000, 2500)
user_2 = FitnessTracker("Ura", 15, 59, 169, 2400, 2900)

print(user_1.info())
print(user_2.info())

print(user_1.daily_activity())
print(user_2.daily_activity())

print(user_1.daily_burned_calories())
print(user_2.daily_burned_calories())
