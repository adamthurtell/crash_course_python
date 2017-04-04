prompt = "\nWhat topping would you like on your pizza?"
prompt += "\n(Enter 'quit' when you are finished adding toppings)"

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print("Great, we're adding " + message + " to your pizza.")