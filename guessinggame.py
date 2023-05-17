import random

print("Welcome to the guessing game")
print("Guess a number between 1 and 100")
toguess = random.randint(1,100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
myguess=0
if difficulty == "easy":
    lives = 10
if difficulty == "hard":
    lives = 5
print(f"You have {lives} lives remaining")
while lives > 0 and myguess != toguess:
    myguess = int(input("Make a guess: "))
    if myguess > toguess:
        print("Too high")
        lives -= 1
        print(f"You have {lives} lives remaining")
    elif myguess < toguess:
        print("Too low")
        lives -= 1
        print(f"You have {lives} lives remaining")
    else:
        print("You got it!")
        break
