prompt = "\nWhat is your age?"
prompt += "\nEnter 'quit' any time to stop. "

while True:
    age = input(prompt)

    if age == 'quit':
        break
    else:
        age = int(age)

        if age < 3:
            ticket_price = 0
        elif age >= 3 and age <= 12:
            ticket_price = 10
        else:
            ticket_price = 15

        print("\nThe price of your ticket is $" + str(ticket_price) + ".")