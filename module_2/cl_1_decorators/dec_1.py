def decorator(func):
    def wrapper(num):
        if type(num) == int or type(num) == float:
            return "Твій інпут є числом"
        else:
            return "Твій інпут: } не є числом"
    return wrapper


@decorator
def some_func(num):
    return num


print(some_func('dff'))
