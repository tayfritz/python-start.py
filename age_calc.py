# Step 1
# Ask the user for their name and the year they were born.
name = input("What is your name?    ")

# TODO input a try and except to test if the user provided a valid number
while True:
    year = input("What year were you born?    ")
    try:
        year = int(year)
    except ValueError:
        print("You must provide a valid number in the format of YYYY.")
        continue
    else:
        break


# Step 2
# Calculate and print the year they'll turn 25, 50, 75, and 100.

twenty_five = int(year) + 25
fifty = int(year) + 50
seventy_five = int(year) + 75
one_hundred = int(year) + 100


# Step 3
# If they're already past any of these ages, skip them.
current_age = 2020 - int(year)
if current_age < 25:
    print("{} you will turn 25 in the year {}".format(name, twenty_five))

if current_age < 50:
    print("{} you will turn 50 in the year {}".format(name, fifty))

if current_age < 75:
    print("{} you will turn 75 in the year {}".format(name, seventy_five))

if current_age < 100:
    print("{} you will turn 50 in the year {}".format(name, one_hundred))