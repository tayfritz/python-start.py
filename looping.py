name = input("What's your name? ")

# TODO: Ask the user by name if they understand Python while loops

understand_python = input("{}, do you understand Python while loops? (Enter yes/no)   ".format(name))

# TODO: Write a while statement that checks if the user doesn't understand while loops
# TODO: Since the user doesn't understand while loops, let's explain them.
# TODO: Ask the user again, by name, if they understand while loops.

while understand_python != "yes":
    print("{}, while loops in Python are used to loop through code until a Boolean condition has been met.".format(name))
    understand_python = input("{}, Do you understand Python while loops now? (Enter yes/no)     ".format(name)   )
    
# TODO: Outside the while loop, congratulate the user for understanding while loops
 
print("Congratulations {}, for understanding while loops!".format(name))
