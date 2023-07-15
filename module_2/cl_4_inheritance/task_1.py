class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def buy_product(self):
        return f"You have bought {self.quantity} {self.name}, price = {self.price}$\n"

    def change_the_name(self, new_name):
        return f"The new name of the product {self.name} = {new_name}\n"

    def change_the_price(self, new_price):
        return f"The new price of product {self.name} = {new_price}\n"

    def change_the_quantity(self, new_quantity):
        return f"The new quantity of product {self.name} = {new_quantity}\n"


class Electronic(Product):
    def __init__(self, name, price, quantity, pc):
        super().__init__(name, price, quantity)
        self.pc = pc

    def add_guarantee(self):
        final_price = self.price * 1.05
        return f"The final price of your {self.name} is {final_price}\n"


class Clothing(Product):
    def __init__(self, name, price, quantity, color):
        super().__init__(name, price, quantity)
        self.color = color

    def refund(self, refund_amount):
        if refund_amount == 1:
            return f"{refund_amount} of {self.color} {self.name} was returned\n"
        else:
            return f"{refund_amount} of {self.color} {self.name}s were returned\n"


class Books(Product):
    def __init__(self, name, price, quantity, rating):
        super().__init__(name, price, quantity)
        self.rating = rating

    def review(self):
        return f"The rating of a book {self.name} is {self.rating} / 10"


product = Product("tv", 100, 10)
print(product.change_the_name("blender"))
print(product.change_the_quantity(7))
print(product.change_the_price(15))

electronic = Electronic("Asus", 20000, 6, "G7")
print(electronic.add_guarantee())

clothes = Clothing("T-shirt", 10, 1, "blue")
print(clothes.buy_product())
print(clothes.refund(2))

books = Books("Harry Pother", 10, 14, 9)
print(books.review())
