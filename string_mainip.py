# Step 1:
# Make two strings, each should be 8 characters long, made up of Xs and Os.
# First string should start with X, second string should start with O.
# Both strings should alternate between the two characters.
# You can use multiplication for this.

string_one = "XO"*4
string_two = "OX"*4

# Step 2:
# Make a list
# Add 1 of the X-started strings.
# Add 1 of the O-started strings.
# Repeat until you have 8 items total in the list.
# You can use multiplication for this, too.

strings = []
def add_strings():
  strings.append(string_one)
  strings.append(string_two)
  strings.append(string_one) 
  strings.append(string_two)
  strings.append(string_one) 
  strings.append(string_two)
  strings.append(string_one) 
  strings.append(string_two)

add_strings()

# OR: 
# xoxo = [xo, ox] * 4



# Step 3:
# Print out the list of strings, joined with newlines \n.

i = 0
while i < len(strings):
    checker_board = strings[i]
    checker_board.join("/n")
    print(checker_board)
    i += 1

# OR "/n".join(xoxo)