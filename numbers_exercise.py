print("Will this break it?")
for value in range(1,101):
    print(value)
print("no, but will this?")

numbers = list(range(1,101))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

print("\nCreating a list of odd numbers by starting at '1' and adding two\n")

odd_numbers = list(range(1,21,2))
print(odd_numbers)

print("\nCreating a list of multiples of three with a range of 3-30 by starting at '3' and adding three\n")

multiples_three = list(range(3,31,3))
for multiple in multiples_three:
    print(multiple)

print("\nCubes:\n")

cubes = []
for value in range(1,11):
    cube = value**3
    cubes.append(cube)

print(cubes)

print("\nCubes using 'list comprehension'\n")

cubes = [value**3 for value in range(1,11)]
for cube in cubes:
    print(cube)