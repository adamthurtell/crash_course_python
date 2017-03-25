pizza_pies = ['Chicago deep dish', 'Sicilian thin crust', 'meat lover\'s']

for pizza in pizza_pies:
    print("I really love " + pizza + " pizza!\n")

print("I said god-DAMN! I love me a pizza.")

friend_pizzas = pizza_pies[:]

pizza_pies.append('vegetarian')

friend_pizzas.append('monkey balls')

print("\nMy favorite pizzas are:")
for pizza in pizza_pies:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)