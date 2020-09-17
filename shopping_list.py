shopping_list = []

def show_help():
    print("What do we need to pick up at the grocery store?   ")
    print("""
Enter 'DONE' to stop adding items to the grocery list
Enter 'HELP' for this help.
Enter 'SHOW' to view your list.
""")


def add_to_list(item):
    shopping_list.append(item)
    print("{} was added to the grocery list! You now have {} items on the list.".format(item, len(shopping_list)))


def show_list():
    print("Here's your shopping list:")
    for item in shopping_list:
        print(item)


show_help()
while True:
    new_item = input(">>>   ")
    if new_item == "DONE":
        break
    elif new_item == "HELP":
        show_help()
        continue
    elif new_item == "SHOW":
        show_list()
        continue
    add_to_list(new_item)

show_list()