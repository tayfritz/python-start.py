# Columns: Name, Day/Month, Celebrates, Age
BIRTHDAYS = (
    ("James", "9/8", True, 9),
    ("Shawna", "12/6", True, 22),
    ("Amaya", "28/2", False, 8),
    ("Kamal", "29/4", True, 19),
    ("Sam", "16/7", False, 22),
    ("Xan", "14/3", False, 34),
)

# Problem 1: Celebrations
# Loop through all of the people in BIRTHDAYS
# If they celebrate their birthday, print out
# "Happy Birthday" and their name

print("Celebrations:")
for celebrate in BIRTHDAYS:
    if True in celebrate:
        print("Happy Birthday, {}".format(celebrate[0]))
print("-"*20)

# Problem 2: Half birthdays
# Loop through all of the people in BIRTHDAYS
# Calculate their half birthday (six months later)
# Print out their name and half birthday

print("Half birthdays:")

i = 0
for name in BIRTHDAYS:
    day = BIRTHDAYS[i][1]
    birth = day.split("/")
    half_birthdays = (int(birth[-1]) + 6)
    if half_birthdays > 12:
        half_birthdays -= 12
    half_birth = "{}/{}".format(int(birth[0]), half_birthdays)
    print("{} - {}".format(BIRTHDAYS[i][0], half_birth))
    i += 1

print("-"*20)

# Problem 3: Only school year birthdays
# Loop through the people in BIRTHDAYS
# If their birthday is between September (9)
# And June (6), print their name

print("School birthdays:")

i = 0

for name in BIRTHDAYS:
    day = BIRTHDAYS[i][1]
    birth = day.split("/")
    school_birthdays = int(birth[1])
    if school_birthdays in range(1,7) or school_birthdays in range(9,13):
        print(BIRTHDAYS[i][0])
    i += 1

print("-"*20)

# Problem 4: Wishing stars
# Loop through BIRTHDAYS
# If the person celebrates their birthday,
# AND their age is 10 or less,
# Print out their name and as many stars as their age

print("Stars:")

i = 0
for name in BIRTHDAYS:
    age = BIRTHDAYS[i][3]
    stars = "*"
    if True in name and age < 10:
        print("{}".format(BIRTHDAYS[i][0]))
        print("Stars: {}".format((stars)*age))
    i += 1
print("-"*20)