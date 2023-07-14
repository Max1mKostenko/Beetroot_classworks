def decorator_of_len(func):
    def wrapper(arg):
        if len(arg) > 10:
            print(f"Your argument: '{arg}', more then 10 symbols!")
            return func(arg)
        else:
            print(f"Your argument: '{arg}', less then 10 symbols!")
            return func(arg)
    return wrapper


def decorator_of_alpha(func):
    def wrapper(arg):
        try:
            arg = str(arg)
        except ValueError:
            print(f"Your argument: '{arg}', isn't a string!")
            return func(arg)

        if str(arg).isalpha():
            print(f"Your argument: '{arg}', have only letters!")
            return func(arg)
        else:
            print(f"Your argument: '{arg}', haven't only letters!")
            return func(arg)
    return wrapper


@decorator_of_len
@decorator_of_alpha
def function(arg):
    print(arg)


function()
