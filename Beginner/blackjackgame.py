# Black Jack game
import random

Money = 100


input("Welcome to Black Jack game. Press Enter to start")

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


def deal(mycards,cards,number):

    game = True
    if number == 0:
        game = False
    else:
        for i in range(number):
            mycards.append(random.choice(list(cards.keys())))
            for card in mycards:
                cards[card] -= 1
    return  mycards,game



def bet(Money):
    bet = int(input("How much do you want to bet ? Maximum bet is " + str(Money) + ". Minimum bet is 5. "))
    if Money <5:
        bet = Money
    elif bet < 5:
        bet=5
    elif bet > Money:
        bet = Money
    print("You bet " + str(bet) + " dollars")
    return bet

def printgame(Money,card):
    print("Your money is "+ str(Money))
    printgamecards(card,"My")
    score = scoring(card)
    print("total score is :  " + str(score))
    return score

def printgamecards(cards,who):
    print( who + " cards are : ")
    for eachcard in cards:
        print(eachcard)

def scoring(card):
    score = 0
    numberofAce = 0
    for eachcard in card:
        if eachcard == "As":
            numberofAce += 1
        score += Score[eachcard]
    while score > 21 and numberofAce > 0:
        score -= 10
        numberofAce -= 1   
    return score

play = True

while play:
    mycards = []
    bankcards=[]
    game = True
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
    bankcards,game = deal(bankcards,cards,2)
    mycards,game = deal(mycards,cards,2)
    printgame(Money,mycards)
    Pot = bet(Money)
    Money -= Pot
    lose=False
    #My game
    while game:
        mycards,game = deal(mycards,cards,int(input("How many cards do you want to draw?")))
        
        if printgame(Money,mycards) > 21:
            print("You lose")
            game = False 
            lose = True
        
    # Bank game
    printgamecards(bankcards,"Bank")
    while scoring(bankcards)<21 and scoring(bankcards)<=scoring(mycards) and lose == False:
        bankcards,game = deal(bankcards,cards,1)
        if(scoring(bankcards)>=21):
            Money += Pot*2
            printgame(Money,mycards)
            printgamecards(bankcards,"Bank")
            print("You win")
            
    if scoring(bankcards)<21 and scoring(bankcards)>scoring(mycards):
        printgame(Money,mycards)
        printgamecards(bankcards,"Bank")
        print("You lose")
    if Money > 0:
        print("You have " + str(Money) + " dollars left")
        playing = input("Do you want to play again ? Y/N")
    else:
        print("You have no money left")
        playing = "N"
    if playing == "N" or Money==0:
        play = False
        print("Thank you for playing")