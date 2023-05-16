import random

wordlist = ["cat", "dog", "rabbit"]
randomword = random.sample(wordlist, 1)
guess = ""
list_of_chars = list(str(randomword[0]))
list_of_charsempty = list_of_chars.copy()
for i in range(len(list_of_chars)):
    list_of_charsempty[i] = "_"
number = 0
print(list_of_chars)
print(list_of_charsempty)
while guess not in wordlist:
    
    letter = str(input("Enter a letter: "))
    
    if(letter in str(randomword[0])):
        print("Correct")
        for i in range(0,len(randomword[0])):
            if(letter == randomword[0][i]):
                list_of_charsempty[i] = letter
                number -=1
    print(list_of_charsempty)
    if(list_of_charsempty == list_of_chars):
        print("You win")
    elif(number > 6):
        print("Game Over")
    else:
        number +=1
