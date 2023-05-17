print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
total_person = int(input("How many people to split the bill? "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

total_tip = total_bill * (tip_percentage / 100)/total_person
print(total_tip)
print("Each person should pay: " + str(total_tip))
