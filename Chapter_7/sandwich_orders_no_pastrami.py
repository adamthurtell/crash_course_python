# Start with two lists, one with the list of sandwiches to be made,
# another empty list with finished sandwiches:
sandwich_orders = ['pastrami','poor boy', 'rueben', 'pastrami', 'philly cheesesteak',
                   'pastrami', 'roast beef']
finished_sandwiches = []

print("Sorry! We have run out of pastrami!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# While there are sandwiches in sandwich_orders, pop off a sandwich and hold it
# in the variable current_sandwich
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    # Print each sandwich as it's made, then append it onto the list of finished
    # sandwiches:
    print("\nMaking your " + current_sandwich.title() + " right now.")
    finished_sandwiches.append(current_sandwich)

# Finally, print all the finished sandwiches:
print("\nThe following sandwiches have been made: ")
for finished_sandwich in finished_sandwiches:
    print("\t" + finished_sandwich.title())