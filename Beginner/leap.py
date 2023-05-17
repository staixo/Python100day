year = int(input("Enter a year: "))
if(year % 400 == 0):
    print("Leap year")
elif(year % 100 == 0):
    print("Not a leap year")
elif(year % 4 == 0):
    print("Leap year")
else:
    print("Not a leap year")