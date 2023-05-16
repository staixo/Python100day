import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer = random.randint(0,2)

if choose == 0:
    print(rock)
elif choose == 1:
    print(paper)
else:
    print(scissors)

if computer == 0:
    print(rock)
    if computer == choose:
        print("Draw")
    elif choose == 1:
        print("You win")
    else:
        print("You lose")
elif computer == 1:
    print(paper)
    if computer == choose:
        print("Draw")
    elif choose == 2:
        print("You win")
    else:
        print("You lose")
else:
    print(scissors)
    if computer == choose:
        print("Draw")
    elif choose == 0:
        print("You win")
    else:
        print("You lose")