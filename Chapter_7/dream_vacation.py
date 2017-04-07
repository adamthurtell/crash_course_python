dream_vacation = {}

polling_active = True

while polling_active:
    name = input("What is your name? ")
    destination = input("Where would you go on your dream vacation? ")

    dream_vacation[name] = destination

    repeat = input("Would you like someone else to take the poll? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

print("POLL RESULTS:")
for name, destination in dream_vacation.items():
    print(name.title() + "'s dream vacation is to go to " + destination.title())
