Machine = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money": 0
}

espresso = {
    "Water": 50,
    "Coffee": 18,
    "Money": 1
}


latte = {
    "Water": 200,
    "Milk": 150,
    "Coffee": 24,
    "Money": 2
}

cappuccino = {
    "Water": 250,
    "Milk": 100,
    "Coffee": 24,
    "Money": 3
}
Menu={
    "espresso": espresso,
    "latte": latte,
    "cappuccino": cappuccino
}
change = {
    
    "quarters":  0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}

def addmoney():
    quarters=int(input("How many quarters?: "))
    dimes=int(input("How many dimes?: "))
    nickles=int(input("How many nickles?: "))
    pennies=int(input("How many pennies?: "))
    return (quarters*float(change["quarters"]))+(dimes*float(change["dimes"]))+(nickles*float(change["nickles"]))+(pennies*float(change["pennies"]))

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
        if check(Menu[choice]):
            money += addmoney()
            if(money>Menu[choice]["Money"]):
                Machine["Money"] += Menu[choice]["Money"]
                make(Menu[choice])
                print(f"Here is your {choice} Enjoy!")
                print("Here is your change: $" + str(money-Menu[choice]["Money"]))
                money = 0
            else:
                print("Sorry, not enough money")
                money = 0
        else:
            "Sorry, there is not enough ingredient"