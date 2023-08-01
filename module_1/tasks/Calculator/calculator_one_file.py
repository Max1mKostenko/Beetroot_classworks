def calculator(num_1, num_2, operator):
    try:
        num_1 = float(num_1)
    except ValueError:
        return f"Your first number: '{num_1}', isn't correct. You should enter only digits!"

    try:
        num_2 = float(num_2)
    except ValueError:
        return f"Your second number: '{num_2}', isn't correct. You should enter only digits!"

    if operator in ("+", "-", "*", "/", "**", "//", "%"):
        if operator == "+":
            return f"Your answer is: {num_1 + num_2}"
        elif operator == "-":
            return f"Your answer is: {num_1 - num_2}"
        elif operator == "*":
            return f"Your answer is: {num_1 * num_2}"
        elif operator == "**":
            return f"Your answer is: {num_1 ** num_2}"

        elif operator == "/":
            try:
                return f"Your answer is: {num_1 / num_2}"
            except ZeroDivisionError:
                return "You can't divide by zero!"

        elif operator == "//":
            try:
                return f"Your answer is: {num_1 // num_2}"
            except ZeroDivisionError:
                return "You can't divide by zero!"

        elif operator == "%":
            try:
                return f"Your answer is: {num_1 % num_2}"
            except ZeroDivisionError:
                return "You can't divide by zero!"
    else:
        return f"Your operator: '{operator}', isn't correct. You should enter only valid operators: " \
               f"(+, -, *, /, **, //, %)"


print(calculator(input("Please enter the first number: "),
                 input("Please enter the second number: "),
                 input("Please enter an operator(+, -, *, /, **, //, %) to solve 2 numbers: ")))
