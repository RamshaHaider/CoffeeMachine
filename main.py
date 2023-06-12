from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

ask = True

while ask:
    items = Menu()
    guess = input(f"What would you like to have {Menu().get_items()}?")

    if guess == "report":
        c1 = CoffeeMaker().report()
        c2 = MoneyMachine().report()
    elif guess == "off":
        ask = False
    else:
        cof = Menu().find_drink(guess)
        if CoffeeMaker().is_resource_sufficient(cof) and MoneyMachine().make_payment(cof.cost):
            CoffeeMaker().make_coffee(cof)
