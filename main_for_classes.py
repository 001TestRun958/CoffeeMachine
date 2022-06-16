from class_menu import Menu, MenuItem
from class_coffee_maker import CoffeeMaker
from class_money_machine import MoneyMachine

menu=Menu()
coffee_maker=CoffeeMaker() 
money_machine=MoneyMachine()

device_on=True

while device_on:
    choice=input(f"What would you like to drink? {menu.get_items()}: ")
    if choice=="off":
        device_on=False
    elif choice=="report":
        print(coffee_maker.report())
        print(money_machine.report())
    else:
        drink=menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
