import sys

MASTER_PASSWORD = "tayloristhebest"

# Don't use this for an actual password checker!! This is simply
# an example of how while loops work
password = input("Please enter the super secret password:   ")
attempt_count = 1
#We want to prompt the user for the password until they enter the correct password - use while
while password != MASTER_PASSWORD:
    if attempt_count > 3:
        sys.exit("ACCESS DENIED. TOO MANY FAILED ATTEMPTS")
    password = input("Invalid password... Please try again.    ")
    attempt_count += 1
print("Welcome to secret town!")
