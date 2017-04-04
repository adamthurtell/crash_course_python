prompt = "What is your age?"
prompt += "\nEnter 'quit' any time to stop. "

age = input(prompt)
age = int(age)

while age != 'quit':
    if age < 3:
        ticket_price = 0
    elif age >=3 and age <= 12:
        ticket_price = 10
    else:
        ticket_price = 15

print("The price of your ticket is $" + str(ticket_price) + ".")
