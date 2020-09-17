import sys

# TODO Create an empty list to maintain the player names
roster = []

# TODO Ask the user if they'd like to add players to the list.
# If the user answers "Yes", let them type in a name and add it to the list.
# If the user answers "No", print out the team 'roster'

def add_to_roster():
    add_player = input("Please type the player's name to add it to the list.   ")
    roster.append(add_player)
    print("Great! We've added {} to the roster!".format(add_player))


user_answer = input("Would you like to add players to the roster? (Yes/No)       ")
if user_answer.upper() == "YES":
    add_to_roster()
    more_players = input("Would you like to add more players to the roster? (Yes/No)    ")
    while more_players.upper() == "YES":
        add_to_roster()
        more_players = input("Would you like to add more players to the roster? (Yes/No)    ")
else:
    print("That's okay. Here's the team roster:")
    print(roster)

# TODO print the number of players on the team
number_of_players = len(roster)
print("There are {} players on the team currently.".format(len(roster)))

# TODO Print the player number and the player name
# The player number should start at the number one


def player_list(player_number):
    for item in roster:
        print("Player {}: {}".format((player_number + 1), item))
        player_number += 1

player_list(0)


# TODO Select a goalkeeper from the above roster

goalkeeper = int(input("Please select a goalkeeper from the roster. Choose a goal keeper by providing their player number. (1-{})    ".format(number_of_players)))


# TODO Print the goal keeper's name
# Remember that lists use a zero based index

print("You have chosen {} to be the goalkeeper! Great choice!".format(roster[goalkeeper - 1]))
