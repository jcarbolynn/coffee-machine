from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money = MoneyMachine()
machine = CoffeeMaker()

is_on = True
while is_on:
    choice = input(f"What would you like? {menu.get_items()}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        machine.report()
        money.report()
    else:
        drink = menu.find_drink(choice)
        if machine.is_resource_sufficient(drink): 
            if money.make_payment(drink.cost):
                machine.make_coffee(drink)

# accomplished this project with very few lines of code and very easy to understand
# don't need to understand how each thing works to use them (BUT YOU SHOULD)

# # latte = MenuItem(Menu("latte"))

# myMenu = Menu()
# # returns memory location that menu item is stored at if no menu item object
# # print(myMenu.find_drink("latte"))
# myCoffeeMaker = CoffeeMaker()
# myCoffeeMaker.report()


# order = input(f"What do you want to order? {myMenu.get_items()}: ").lower()

# # check if order is an option
# print(order)
# print(myMenu.find_drink(order).name)

# if order == myMenu.find_drink(order).name:
#   print("drink exists")
#   # myCoffeeMaker.is_resource_sufficient(myMenu.find_drink(order).name)
