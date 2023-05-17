import machine

Machine=machine.Machine()

def addmoney():
    quarters=int(input("How many quarters?: "))
    dimes=int(input("How many dimes?: "))
    nickles=int(input("How many nickles?: "))
    pennies=int(input("How many pennies?: "))
    return (quarters*float(Machine.change["quarters"]))+(dimes*float(Machine.change["dimes"]))+(nickles*float(Machine.change["nickles"]))+(pennies*float(Machine.change["pennies"]))

def check(drink):
    for item in drink:
        if item == "Money":
            continue
        if drink[item] > Machine[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def make(drink):     
    for item in drink:
        if item == "Money":
            continue
        Machine[item] -= drink[item]
    

print("Welcome to the cafe!")
money=0
while True:
    choice =  input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        break
    elif choice == "report":
        print("report : \nWater: " + str(Machine["Water"]) + "ml of water" + "\nMilk: " + str(Machine["Milk"]) + "ml of milk" + "\nCoffee: " + str(Machine["Coffee"]) + "g of coffee" + "\nMoney: $" + str(Machine["Money"]))
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        if check(Machine.Menu[choice]):
            money += addmoney()
            if(money>Machine.Menu[choice]["Money"]):
                Machine["Money"] += Machine.Menu[choice]["Money"]
                make(Machine.Menu[choice])
                print(f"Here is your {choice} Enjoy!")
                print("Here is your change: $" + str(money-Machine.Menu[choice]["Money"]))
                money = 0
            else:
                print("Sorry, not enough money")
                money = 0
        else:
            "Sorry, there is not enough ingredient"