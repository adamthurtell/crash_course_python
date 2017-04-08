cars = ['bmw', 'audi', 'toyota', 'subaru']

cars.sort()
print(cars)

# .sort() permanently changes the order of a list

cars.sort(reverse=True)
print(cars)

# We re-did the original order:

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("\nHere is the orginal list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))
# sorted() temporarily changes the order of the list

print("\nHere is the original list again:")
print(cars)

print("\nNow I'm going to reverse the list:")
cars.reverse()
# .reverse() doesn't sort backward alphabetically; it simply reverses the order of the list
print(cars)

# So we have the sort() method, which is permanent and which you can reverse by
# passing the argument list.sort(reverse=True)).
# Then you have the sorted() function, which is temporary.
# Then you have the reverse() method, which doesn't sort alphabetically but simply reverses the order of the list.
print("\n")
print(len(cars))

print("\n")

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())