# Black Jack game
import random

Money = 100


input("Welcome to Black Jack game. Press Enter to start")




def deal(cards):
    mycards = []
    for i in range(2):
        mycards.append(random.choice(list(cards.keys())))
        for card in mycards:
            cards[card] -= 1
    return  mycards

Score={
    "As": 11,
    "2": 2,
    "3": 3,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "7": 7,
    "8": 8,
    "9": 9,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
}

play = True
game = True
while play:
    cards = {
    "As": 4,
    "2": 4,
    "3": 4,
    "4": 4,
    "5": 4,
    "6": 4,
    "7": 4,
    "8": 4,
    "9": 4,
    "Jack": 4,
    "Queen": 4,
    "King": 4,
    }
    while game:
        mycards = deal(cards)
        bankcards = deal(cards)

        print("Your money is "+ str(Money) + " and your hand is :")
        for eachcard in mycards:
            print(eachcard)
        if Money <= 0:
            print("You are out of money")
            game = False 
        Money -= 1