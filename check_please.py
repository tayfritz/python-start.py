import math

def split_check(number_of_people, total_due):
    if number_of_people <= 1:
        raise ValueError("You need more than one person to split a check.")
    return math.ceil(total_due / number_of_people)

try:
    total_due = float(input("What is the total?   "))     #float = a decimal!
    number_of_people = int(input("How many people are splitting the total bill?   "))      #int = integer or whole number!
    amount_due = split_check(number_of_people, total_due)
except ValueError as err:
    print("Oh no, that's not a valid value. Try again...")
    print("({})".format(err))
else:
    print("Each person owes ${}".format(amount_due))