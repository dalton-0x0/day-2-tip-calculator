print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What % tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people would split the bill? "))

tip_factor = (tip / 100) + 1
bill_with_tip = bill * tip_factor
bill_per_person = bill_with_tip / people
# each_to_pay = round(bill_per_person 2)
each_to_pay = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${each_to_pay}")