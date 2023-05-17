import HigherLowerdata
import random
import os


score = 0
play = True
while play:
    os.system('cls')
    print(HigherLowerdata.logo)
    Compare1 = ""
    Compare2 = ""
    while Compare1 == Compare2:
        Compare1 = HigherLowerdata.data[random.randint(0, len(HigherLowerdata.data)-1)]
        Compare2 = HigherLowerdata.data[random.randint(0, len(HigherLowerdata.data)-1)]
    print("\nCompare A: ", Compare1["name"], ", a ", Compare1["description"], " from ", Compare1["country"])
    print(HigherLowerdata.vs)
    print("\nCompare B: ", Compare2["name"], ", a ", Compare2["description"], " from ", Compare2["country"])
    print("\nGuess which is higher: A or B")
    guess = input("\nEnter your guess: ").lower()
    if(Compare1["follower_count"] > Compare2["follower_count"]):
        correct = "a"
    elif(Compare1["follower_count"] < compare2["follower_count"]):
        correct = "b"
    else:
        print("Error")
    if guess == correct:
        score += 1
        print("Correct!")
    else:
        print("Wrong!")
        play = False
    print("Your score is ", score)