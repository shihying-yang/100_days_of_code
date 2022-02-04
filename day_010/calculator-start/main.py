""" a text version of calculator """
from art import logo

# Calculator


# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        # return "You can't divide by zero!"
        return 0


# operations dictinoary
operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    print(logo)
    num1 = float(input("What's' the first number?: "))

    to_continue = True
    while to_continue:
        for symbol in operations:
            print(f"{symbol}")
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        to_continue = (
            input(f"Type 'y' to continue calculating with {answer} or type 'n' to repeat: ")
            .lower()
            .startswith("y")
        )
        if to_continue:
            num1 = answer  # set the num1 to answer, so the next iteration is correct
        else:
            print(f"The final answer is {answer}")
            print("\n" * 2)
            calculator()


calculator()
