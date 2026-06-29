from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True
while is_on:
    option = menu.get_items()
    order=input(f"What would you like?({option})")
    if order == "off":
        is_on = False
        print("Welcome,come back soon")
    elif order == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        drink=menu.find_drink(order)
        if coffe_maker.is_resource_sufficient(drink)==True:
           if money_machine.make_payment(drink.cost):
               coffe_maker.make_coffee(drink)
        else:
            is_on = False