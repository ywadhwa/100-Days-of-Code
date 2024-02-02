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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def calculate_change(choice):
    print("Please insert coins.")
    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickles = int(input("How many nickles?"))
    pennies = int(input("How many pennies?"))
    money_given = pennies * 0.01 + nickles * 0.05 + dimes * 0.1 + quarters * 0.25
    change = money_given - MENU[choice]["cost"]
    return money_given,change


def check_resources(choice):
    for ingredient in MENU[choice]["ingredients"]:
        if MENU[choice]["ingredients"][ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return True
    return False


def update_resources(choice, money_given, change):
    for ingredient in MENU[choice]["ingredients"]:
        resources[ingredient] = resources[ingredient] - MENU[choice]["ingredients"][ingredient]
    resources["money"] = resources["money"] + money_given - change


coffee_machine_on = True

while coffee_machine_on:

    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "report":
        print(f'Water:{resources["water"]} \n Milk:{resources["milk"]} \n Coffee:{resources["coffee"]} \n '
              f'Money:{resources["money"]}')
    elif choice in ["latte", "espresso", "cappuccino"]:
        check_pass = check_resources(choice)
        if check_pass:
            continue
        money_given,change = calculate_change(choice)
        if money_given < MENU[choice]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
            continue
        else:
            print(f'{change:.2f}')
        print(f"Here is you {choice}. Enjoy.")
        update_resources(choice, money_given, change)

    elif choice == "off":
        coffee_machine_on = False




