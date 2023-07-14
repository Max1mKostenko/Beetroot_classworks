def decorator(func):
    def wrapper(arg):
        if type(arg) == int or type(arg) == float:
            return -arg
        else:
            return f"Ваше значення '{arg}', не є числом"
    return wrapper


@decorator
def function(arg):
    return f"Your answer is {arg}"


print(function(5))
