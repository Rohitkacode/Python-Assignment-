def my_decorator(func):
    def wrapper(a,b):
        result = func(a,b)
        return result
    return wrapper

@my_decorator
def add_numbers(x, y):
    return x + y

result = add_numbers(5, 5)
print(result)
