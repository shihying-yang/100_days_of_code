MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def which_coffee(user_input):
    """decide which coffee the customer selects

    :param user_input: input from the customer
    :type user_input: string
    :return: coffee type
    :rtype: string
    """
    if user_input.lower().startswith("e"):
        return "espresso"
    elif user_input.lower().startswith("l"):
        return "latte"
    elif user_input.lower().startswith("c"):
        return "cappuccino"
    elif user_input.lower().startswith("r"):
        return "report"
    elif user_input.lower().startswith("o"):
        return "off"
    else:
        return "Invalid selection"


def print_report(contain_resources, money_earned):
    """print the report of the machine

    :param contain_resources: resources left in the machine
    :type contain_resources: dict
    :return: print the report
    :rtype: None
    """
    for k, v in contain_resources.items():
        if k in ["water", "milk"]:
            print(f"{k.title()}: {v}ml")
        else:
            print(f"{k.title()}: {v}g")
    print(f"Money: ${money_earned}")


def check_resources(selection, contain_resources):
    """check if the machine contains enough resource for the coffee

    :param selection: [description]
    :type selection: [type]
    :param contain_resources: [description]
    :type contain_resources: [type]
    :return: [description]
    :rtype: [type]
    """
    needed_resource = MENU[selection]["ingredients"]
    for k, v in needed_resource.items():
        if contain_resources[k] < v:
            print(f" Sorry, there is not enough {k}.")
            return False
    return True


def process_coins(selection):
    """Process input to get the amount

    :return: input amount
    :rtype: float
    """
    paid = 0
    # print the coin operations
    print("Please insert coins.")
    quarters = int(input("How may quarters? "))
    dimes = int(input("How may dimes? "))
    nickles = int(input("How may nickles? "))
    pennies = int(input("How may pennies? "))
    # get the amount paid
    paid = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    price = MENU[selection]["cost"]
    if paid >= price:
        print(f"Here is ${round(paid - price, 2)} in change.")
        return MENU[selection]["cost"]
    else:
        print(f" Sorry, that's not enough money. Money refunded.")
        return 0


def make_coffee(selection, contain_resources):
    """make coffee based on coffee and resources left

    :param selection: coffee kind
    :type selection: string
    :param contain_resources: resources left in the machine
    :type contain_resources: dict
    :return:
    :rtype:
    """
    needed_resource = MENU[selection]["ingredients"]
    for k, v in needed_resource.items():
        contain_resources[k] -= v
    print(f"Here is your {selection} ☕. Enjoy!")


if __name__ == "__main__":
    machine_resources = resources
    # continues making coffee until the user wants to quit (machine off)
    can_make_coffee = True
    amount = 0
    while can_make_coffee:
        # select coffee
        customer_input = which_coffee(input("  What would you like? (espresso/latte/cappuccino): "))
        if customer_input == "report":
            print_report(machine_resources, amount)
        elif customer_input == "off":
            print("Machine is shutting down . . .")
            print("Goodbye!")
            can_make_coffee = False
        elif customer_input != "Invalid selection":
            # check if the machine has enough resources first
            enough_resource = check_resources(customer_input, machine_resources)
            # make coffee if the machine has enough resources
            if enough_resource:
                enough_money = process_coins(customer_input)
                if enough_money:
                    amount += enough_money
                    make_coffee(customer_input, machine_resources)
        else:
            print("Invalid selection.")
