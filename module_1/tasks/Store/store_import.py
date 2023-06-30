from store_def import products, main, list_products, add_products, change_product, add_the_new_criterion, del_product
if __name__ == "__main__":
    print(main(int(input("Please enter 1 - (to see the product list)"
                         "\n\t\t   / 2 - (to add the new product)"
                         "\n\t\t   / 3 - (to change someone product)"
                         "\n\t\t   / 4 - (to add the new criterion for all products)"
                         "\n\t\t   / 5 - (to del someone product): "))))
