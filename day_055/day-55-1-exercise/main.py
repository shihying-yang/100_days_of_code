# Create the logging_decorator() function 👇
def logging_decorator(func):
    def wrapper(*args):
        print(f"You called {func.__name__}{args}")
        result = func(*args)
        print(f"It returned: {result}")

    return wrapper


# Use the decorator 👇
@logging_decorator
def add(*args):
    return sum(args)


if __name__ == "__main__":
    add(1, 2, 3)
