my_motorcycles = ['BMW', 'KTM', 'Honda', 'Yamaha', 'Triumph']

message = "My first choice for a motorcycle is a " + my_motorcycles[1] + "."

print(message)

message = "My second choice for a motorcycle is probably a " + my_motorcycles[0] + "."

print(message)

message = "But I just saw the " + my_motorcycles[2] + " dual-sport, and it might be the best bang for the buck."

print(message)

print("The first three motorcycles are:")
for motorcycle in my_motorcycles[:3]:
    print(motorcycle)

print("\nThe three items from the middle of the list are:")
for motorcycle in my_motorcycles[1:4]:
    print(motorcycle)

print("\nThe last three motos on my list are:")
for motorcycle in my_motorcycles[2:]:
    print(motorcycle)