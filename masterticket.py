import sys
SERVICE_CHARGE = 2
TICKET_PRICE = 10

tickets_remaining = 100  

def calculate_price(number_of_tickets):
    cost = (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE
    return cost


#Use the truthiness of tickets_remainig. A 0 = false.. So when it gets to 0 tickets, it will stop running
while tickets_remaining >= 1:
    print("There are {} tickets remaining! Act fast!".format(tickets_remaining))
    name = input("What is your name?   ")
    
    number_of_tickets = input("Hello {}! How many tickets do you wish to purchase?     ".format(name))
    try:
        number_of_tickets = int(number_of_tickets)
        if number_of_tickets > tickets_remaining:
            raise ValueError("We only have {} tickets left. Please try again.".format(tickets_remaining))
    except ValueError as err:
        print("Sorry, we ran into an issue. {}".format(err))
        sys.exit()
    else:
        estimated_price = calculate_price(number_of_tickets)
        print("{}, the cost of {} tickets will be ${}".format(name, number_of_tickets, estimated_price))
        confirm_order = input("Would you like to proceed with purchasing {} ticket(s), {}? (Y/N?)    ".format(number_of_tickets, name))
        if confirm_order.lower() != "n":
            print("SOLD! {}, you just purchased {} tickets!".format(name, number_of_tickets))
            tickets_remaining -= number_of_tickets
            print("There are {} tickets remaining for the event".format(tickets_remaining))
        else:
            print("{}, thank you for your interest in our event! Please come back if you would like to purchase a ticket!".format(name))

print("Sorry, we have no more tickets left for the event!")
