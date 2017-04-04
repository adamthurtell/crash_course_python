number = input("Enter a number and I'll tell you whether it's a multiple of"
               "ten or not:")
number = int(number)

if number % 10 == 0:
    print("\nYep, your number is a multiple of ten!")
else:
    print("\nNope, not a multiple of ten. But you probably knew that.")