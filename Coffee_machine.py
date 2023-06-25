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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(requirements):
    for items in requirements:
        if requirements[items] >= resources[items]:
            print(f"Sorry there is not enough {items}")
            return False
        return True

def check_transaction(money_inserted, drink_cost):
    global profit
    if money_inserted < drink_cost:
        print(f"Sorry that's not enough money, Money refunded.")
        return False
    elif money_inserted == drink_cost:
        profit += money_inserted
        return True
    elif money_inserted > drink_cost:
        profit += drink_cost
        change = round(money_inserted - drink_cost, 2)
        print(f"Here is ${change} in change.")
        return True

def process_coins():
    total = 0
    print("Please insert coins. ")
    total += float(input("How many quarters?: ")) * 0.25
    total += float(input("How many dimes?: ")) * 0.10
    total += float(input("How many nickels?: ")) * 0.05
    total += float(input("How many pennies?: ")) * 0.25
    return total

def  make_coffee(drink_name, order_ingredients):
    for items in order_ingredients:
        resources[items] -= order_ingredients[items]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

machine = True

while machine:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        machine = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if check_transaction(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])
