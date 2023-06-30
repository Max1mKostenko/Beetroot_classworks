def list_products(list_of_products):
    return f"\nThe list of products:\n{list_of_products}"


def add_products(products):
    while True:
        product = input("\nPlease enter a product to add: ").capitalize()
        if not product.isalpha():
            print('Please enter...')
        else:
            break

    while True:
        quantity = input("\nEnter the quantity of new product: ")
        if not quantity.isdigit():
            print('Please enter the quantity in digits! ')
        else:
            break

    while True:
        price = input("Enter the price of new product: ")
        if not price.isdigit():
            print('Please enter the price in digits! ')
        else:
            break

    if product:
        if product not in products.keys():
            products.update({product: {"quantity": quantity, "price": price}})
            return f"\nThe new list of products:\n{products}"
        else:
            return f"\nThe {product} is already in list of products. Please enter another one to add."


def change_product(products, particular_product, action):
    if particular_product == 1:
        particular_product = list(products.keys())[0]
    elif particular_product == 2:
        particular_product = list(products.keys())[1]
    elif particular_product == 3:
        particular_product = list(products.keys())[2]
    elif particular_product == 4:
        particular_product = list(products.keys())[3]
    else:
        return f"\nYour penultimate input '{particular_product}' isn't correct. You should choose only 1 | 2 | 3 | 4."

    if action == 1:
        products[particular_product]["quantity"] = int(input(f"\nEnter the new quantity of {particular_product}: "))
        products[particular_product]["price"] = int(input(f"Enter the new price of {particular_product}: "))
        return f"\nThe new list of products:\n{products}"
    elif action == 2:
        products[particular_product]["quantity"] = int(input(f"\nEnter the new quantity of {particular_product}: "))
        return f"\nThe new list of products:\n{products}"
    elif action == 3:
        products[particular_product]["price"] = int(input(f"\nEnter the new price of {particular_product}: "))
        return f"\nThe new list of products:\n{products}"
    else:
        print(f"\nYour last input: '{action}', isn't correct!. You should choose only 1 | 2 | 3.")


def add_the_new_criterion(products, new_criterion):
    if new_criterion.isalpha():
        if new_criterion not in products["Banana"].keys():
            for i in products.keys():
                products[i].update({new_criterion: int(input(f"\nPlease enter the value of new criterion for {i}: "))})
        else:
            return f"\nThe criterion {new_criterion} is already exists. Please enter another one to add."
        return f"\nThe new list of products:\n{products}"
    else:
        return f"\nYour input: '{new_criterion}', isn't correct. You should enter only letters without spaces"


def del_product(products, delete_product):
    if delete_product == 1:
        delete_product = list(products.keys())[0]
    elif delete_product == 2:
        delete_product = list(products.keys())[1]
    elif delete_product == 3:
        delete_product = list(products.keys())[2]
    elif delete_product == 4:
        delete_product = list(products.keys())[3]
    else:
        return f"\nYour penultimate input '{delete_product}' isn't correct. You should choose only 1 | 2 | 3 | 4."
    products.pop(delete_product)
    return f"\nThe new list of products:\n{products}"


def main():
    products = {"Apple": {"quantity": 72, "price": 20},
                "Banana": {"quantity": 35, "price": 40},
                "Pineapple": {"quantity": 10, "price": 70},
                "Potato": {"quantity": 50, "price": 30}}

    while True:
        try:
            user = int(input("Please enter 1 - (to see the product list)"
                             "\n\t\t   / 2 - (to add the new product)"
                             "\n\t\t   / 3 - (to change someone product)"
                             "\n\t\t   / 4 - (to add the new criterion for all products)"
                             "\n\t\t   / 5 - (to del someone product): "))
            assert 0 < user < 6  # asserting the answer
        except ValueError:
            print("\nNot a digit. Please enter a digit from: 1 - 5 only.\n")
        except AssertionError:
            print("Please enter a digit from: 1 - 5 only.")
        else:
            break


    if user == 1:
        print(list_products(products))
    elif user == 2:
        print(add_products(products))
    elif user == 3:
        print(change_product(products,
                             int(input("\nPlease enter 1 - (Apple) | 2 - (Banana) | 3 - (Pineapple) | 4 - (Potato) "
                                       "to change info about these products: ")),
                             int(input(
                                 "\n Please enter 1 to change the product which you have selected(quantity and "
                                 "price),"
                                 "\n\t\t\t 2 to change only the quantity,"
                                 "\n\t\t\t 3 to change only the price: "))))
    elif user == 4:
        print(add_the_new_criterion(products,
                                    input("\nPlease enter the name of new criterion: ").lower()))
    elif user == 5:
        print(del_product(products,
                          int(input("\nPlease enter 1 - (Apple) | 2 - (Banana) | 3 - (Pineapple) | 4 - (Potato) "
                                    "to delete one of these products: "))))
    else:
        print(f"\nYour input: '{user}', isn't correct!. You should choose only 1 | 2 | 3 | 4 | 5.")


if __name__ == '__main__':
    main()
