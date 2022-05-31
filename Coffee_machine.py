MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
"""Returns True when order can be made, False if ingredients are insufficient."""
def is_resources_sufficient(drink_ingredients):
    for item in drink_ingredients:
        if drink_ingredients[item]<=resources[item]:
            return True
        else:    
            print(f"Sorry, there is not enough {item}")
            return False

"""Returns the total calculated from coins inserted."""
def received_coins():
    print("Please insert coins: ")
    total=int(input("How many quarters: "))*0.25
    total+=int(input("How many dimes: "))*0.1
    total+=int(input("How many nickels: "))*0.05
    total+=int(input("How many pennies: "))*0.01
    return total

"""Return True when the payment is accepted, or False if money is insufficient."""
def check_payment(drink_cost,payment):
    if drink_cost<=payment:
        change=round(payment-drink_cost,2)
        global profit
        profit+=drink_cost
        return True
    else:
        print("It's not enought money")
        return False

"""Deduct the required ingredients from the resources."""
def make_coffee(drink_name, drink_ingredients):
    for item in drink_ingredients:
        resources[item]-=drink_ingredients[item]
    print(f"Enjoy your {drink_name}")

device_on=True

while device_on:
    """1. Ask user "What would you like?"""
    choice=input("What would you like to drink? 'espresso/latte/cappuccino': ")
    """2. Turn machine off by entering "off" """
    if choice=="off":
        device_on=False
        """3. Print report of all coffee machine resources."""
    elif choice=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink=MENU[choice]
        """4. Check resources sufficient?"""
        drink_ingredients=drink["ingredients"]
        if is_resources_sufficient(drink["ingredients"]):
            """ 5. Process coins."""
            payment=received_coins()
            drink_cost=drink["cost"]
            """ 6. Check transaction successful?"""
            if check_payment(drink_cost,payment):
                """ 7. Make coffee."""
                make_coffee(choice,drink["ingredients"])