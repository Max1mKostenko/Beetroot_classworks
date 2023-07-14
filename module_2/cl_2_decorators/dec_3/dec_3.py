import time
print(time.strftime("%Y-%m-%d %H:%M:%S"))


def decorator_of_time(func):
    def wrapper(_time):
        with open("date_time.txt", "a") as file:
            file.write(f"Час коли була викликана функція: {_time}\n")
        return func(_time)
    return wrapper


@decorator_of_time
def function(_time):
    return _time


print(function(time.strftime("%Y-%m-%d %H:%M:%S")))


