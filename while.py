import time
# Problem 1: Warm the oven
# Write a while loop that checks to see if the oven
# is 350 degrees. If it is, print "The oven is ready!"
# If it's not, increase current_oven_temp by 25 and print
# out the current temperature.

current_oven_temp = 75
while current_oven_temp < 350:
    time.sleep(.75)
    current_oven_temp += 25
    print("The current temp: {}".format(current_oven_temp))

print("The oven is ready!!")

# Problem 2: Total and average
# Complete the following function so that it asks for
# numbers from the user until they enter 'q' to quit.
# When they quit, print out the list of numbers,
# the sum and the average of all of the numbers.
numbers = []

def total_and_average():
    total = sum(numbers)
    average = total/(len(numbers))
    print("Numbers: {}".format(numbers))
    print("SUM: {}".format(total))
    print("AVG: {}".format(average))

while True:
    num = input("Please provide a number or press 'q' to quit.   ")
    if num == "q":
        break
    numbers.append(int(num))

total_and_average()

# Problem 3: Missbuzz
# Write a while loop that increments current by 1
# If the new number is divisible by 3, 5, or both,
# print out the number. Otherwise, skip it.
# Break out of the loop when current is equal to 101.

current = 1

# Solution 3 here