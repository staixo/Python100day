import random
import string
password = ""
number_of_letter = int(input("How many letter do you want to have in your password? "))
symbols = int(input("How many symbols do you want to have in your password? "))
numbers = int(input("How many numbers do you want to have in your password? "))
symbolssave = symbols
numberssave = numbers
#Full random
for i in range(number_of_letter):
    if(symbols<=0 and numbers<=0):
        value = random.choice(string.ascii_letters)
    elif(numbers>0 and symbols<=0):
        value = random.choice(string.ascii_letters + string.digits)
    elif(symbols>0 and numbers<=0):
        value = random.choice(string.ascii_letters + string.punctuation)
    else:
        value = random.choice(string.ascii_letters + string.digits + string.punctuation )
    if(value in string.punctuation):
        symbols -= 1
    if(value in string.digits):
        numbers -= 1
    password += value
print("Here is your password: ", password)

#init
password = ""
iter = 0
symbols = symbolssave
numbers = numberssave
#Random with symbols and numbers
if(symbols + numbers <= number_of_letter):
    for i in range(number_of_letter):
        value = random.choice(string.ascii_letters)
        password += value
    intlist = random.sample(range(0, len(password)), symbols + numbers)
    print(intlist)
    for j in range(numbers):
        value = random.choice(string.digits)
        password = password[:intlist[iter]] + value + password[intlist[iter]+1:]
        iter += 1
    for j in range(symbols):
        value = random.choice(string.punctuation)
        password = password[:intlist[iter]] + value + password[intlist[iter]+1:]
        iter += 1

    print("Here is your password: ", password)
else:
    print("error")