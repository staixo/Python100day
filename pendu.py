import random

wordlist = ["cat", "dog", "rabbit"]
randomword = random.sample(wordlist, 1)

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

list_of_chars = list(str(randomword[0]))
list_of_charsempty = list_of_chars.copy()
for i in range(len(list_of_chars)):
    list_of_charsempty[i] = "_"
number = 0
end = 0
live = 6
print(list_of_chars)
print(list_of_charsempty)
while end == 0 :
    
    letter = str(input("Enter a letter: "))
    
    if(letter in str(randomword[0])):
        print("Correct")
        for i in range(0,len(randomword[0])):
            if(letter == randomword[0][i]):
                list_of_charsempty[i] = letter
    else:
        print("Wrong")
        live -=1
        stages[live]
    
    print(list_of_charsempty)
    if(list_of_charsempty == list_of_chars):
        print("You win")
        end = 1
    elif(live == 0):
        print("You lose")
        end = 1 
