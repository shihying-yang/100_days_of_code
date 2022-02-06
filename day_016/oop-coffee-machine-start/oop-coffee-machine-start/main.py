from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# create objects for this to work
store_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

if __name__ == "__main__":
    machine_on = True
    # make this continuous, until user manually turn off machine
    while machine_on:
        # get user selection
        customer_input = input("  What would you like? (espresso/latte/cappuccino): ").lower()
        # check if user wants to see the report
        if customer_input.startswith("r"):
            coffee_maker.report()
            money_machine.report()
        # check if the user wants to turn off the machine
        elif customer_input.startswith("o"):
            print("Machine is shutting down . . .")
            print("Goodbye!")
            machine_on = False
        # now it's making coffee
        else:
            # associate the drink correctly (lazy typing)
            if customer_input.startswith("e"):
                customer_input = "espresso"
            elif customer_input.startswith("l"):
                customer_input = "latte"
            elif customer_input.startswith("c"):
                customer_input = "cappuccino"
            # consider the case where wrong input is give, just skip
            else:
                continue
            # get the correct MenuItem from the selection
            to_make_coffee = store_menu.find_drink(customer_input)
            # check if the coffee maker has the resource to make the drink
            enough_resource = coffee_maker.is_resource_sufficient(to_make_coffee)
            if enough_resource:
                # Now check if the customer can afford the drink
                enough_money = money_machine.make_payment(to_make_coffee.cost)
                if enough_money:
                    coffee_maker.make_coffee(to_make_coffee)
