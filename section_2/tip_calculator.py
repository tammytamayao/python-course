print("Welcome to the Tip Calculator");
# get user input for total bill
total_bill = input("What was the total bill? $");
# get user input for tip amount
percentage_tip = input("What percentage tip would you like to give? 10, 12, or 15? ");
# determine number of people included for bill split
num_of_people = input("How many people to split the bill? ");
# calculating bill per person
bill_per_person = (float(total_bill) * (1+ float(percentage_tip)/100))/int(num_of_people)
# print output
print(f"Each person should pay ${round(float(bill_per_person),2)}");
