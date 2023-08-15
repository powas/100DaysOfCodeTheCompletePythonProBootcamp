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
    }
}


def report(report_resources, report_profit):
    """Returns a list of the current resources."""
    print(f"Water: {report_resources['water']}ml")
    print(f"Milk: {report_resources['milk']}ml")
    print(f"Coffee: {report_resources['coffee']}g")
    print(f"Money: ${report_profit}")


def sufficient_resources(check_resources, check_drink_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in check_drink_ingredients:
        if check_drink_ingredients[item] > check_resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    else:
        return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def check_transaction(check_payment, check_drink_cost):
    """Returns the amount of the payment."""
    if check_payment < check_drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return 0
    elif check_payment == check_drink_cost:
        return check_drink_cost
    else:
        change = round(check_payment - check_drink_cost, 2)
        print(f"Here is ${change} dollars in change.")
        return check_drink_cost


def make_coffee(coffee_resources, coffee_drink_ingredients):
    """Returns the updated resources."""
    for item in coffee_drink_ingredients:
        coffee_resources[item] -= coffee_drink_ingredients[item]
    return coffee_resources


def machine():
    profit = 0
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }
    is_running = True
    while is_running:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "off":
            is_running = False
        elif choice == "report":
            report(resources, profit)
        elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
            drink = MENU[choice]
            if sufficient_resources(resources, drink["ingredients"]):
                payment = process_coins()
                sell = check_transaction(payment, drink["cost"])
                profit += sell
                if sell != 0:
                    resources = make_coffee(resources, drink["ingredients"])
                    print(f"Here is your {choice} ☕️. Enjoy!")


machine()
