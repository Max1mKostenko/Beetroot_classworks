class Prize:
    def __init__(self, name_prize_1, name_prize_2, price_prize_1, price_prize_2):
        self.name_prize_1 = name_prize_1
        self.name_prize_2 = name_prize_2
        self.price_prize_1 = price_prize_1
        self.price_prize_2 = price_prize_2

    def __add__(self):
        return f"First prize: {self.name_prize_1}\nSecond prize: {self.name_prize_2}"

    def __eq__(self, other):
        if self.price_prize_1 == other:
            return "The prices of two gifts are the same"
        else:
            return "The prices of two gifts aren't the same"

    def __str__(self):
        return f"\nFirst prize: \nName: {self.name_prize_1}\nPrice: {self.price_prize_1} UAH\n" \
               f"\nSecond prize:\nName: {self.name_prize_2}\nPrice: {self.price_prize_2} UAH"


prize = Prize("Lamborghini LEGO", "Mustang LEGO", 4000, 5000)
print(prize.__add__())
print(prize.__str__())
print(prize.__eq__(prize.price_prize_2))
