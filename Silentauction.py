import os

print("Welcome to silent auction.")
bid = True
bidderlist = []
bidderprice = []
while bid == True:
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))
    bidderlist.append(name)
    bidderprice.append(price)
    bid = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if bid == "no":
        bid = False
    os.system("cls||clear")
price = max(bidderprice)
name = bidderlist[bidderprice.index(price)]

print("The highest bidder is: "+ name + " with a bid of $" + str(price))