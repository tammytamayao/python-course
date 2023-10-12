print("Welcome to the Tip Calculator");
total_bill = input("What was the total bill? $");
percentage_tip = input("What percentage tip would you like to give? 10, 12, or 15? ");
num_of_people = input("How many people to split the bill? ");

bill_per_person = (float(total_bill) * (1+ float(percentage_tip)/100))/int(num_of_people)
print(f"Each person should pay ${round(float(bill_per_person),2)}");
