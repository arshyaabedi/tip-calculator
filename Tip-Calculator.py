print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? "))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
new_tip = (tip / 100) + 1
people = int(input("How many people to split the bill? ")) 
print(f"Each person should pay {round(((total_bill * new_tip) / people), 2)}")