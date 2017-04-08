age = 19

if age < 4:
    price = 0

elif age < 18:
    price = 5

elif age < 65:
    price = 10

elif age >= 65:
    price = 5

# this last elif block replaced an else block (else:). It's clearer to write it this way.

print("Your admission cost is $" + str(price) + ".")