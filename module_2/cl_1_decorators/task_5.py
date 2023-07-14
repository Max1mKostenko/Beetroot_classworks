def split_str(your_string):
    for item in your_string.split(" "):
        print(f"The first letter of the word '{item}', is '{item[0]}'.")


split_str("hello my name is max")
