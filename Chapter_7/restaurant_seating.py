group_size = input("How many people are in your party? ")
group_size = int(group_size)

if group_size > 8:
    print("\nPlease have a seat in our lounge, we'll call you as soon as your "
          "table is ready.")
else:
    print("\nYour table is ready, right this way...")