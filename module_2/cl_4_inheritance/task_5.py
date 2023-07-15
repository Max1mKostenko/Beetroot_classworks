class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def buy_product(self):
        return f"You have bought {self.quantity} of {self.name}, price = {self.price}$ each"


class Electronic(Product):
    def __init__(self, name, price, quantity, pc):
        super().__init__(name, price, quantity)
        self.pc = pc

    def add_guarantee(self):
        final_price = self.price * 1.05
        return f"The final price of your {self.name} is {final_price}"


electronic = Electronic("Asus", 20000, 6, "G7")
print(electronic.add_guarantee())


class Clothing(Product):
    def __init__(self, name, price, quantity, color):
        super().__init__(name, price, quantity)
        self.color = color

    def refund(self, refund_amount):
        if refund_amount == 1:
            return f"{refund_amount} of {self.color} {self.name} was returned"
        else:
            return f"{refund_amount} of {self.color} {self.name}s were returned"


clothes = Clothing("T-shirt", 10, 1, "blue")
print(clothes.buy_product())
print(clothes.refund(1))


class Books(Product):
    def __init__(self, name, price, quantity, rating):
        super().__init__(name, price, quantity)
        self.rating = rating

    def review(self):
        return f"The book {self.name} is {self.rating} / 10"


books = Books("Harry Pother", 10, 14, 9)
print(books.review())

