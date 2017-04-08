favorite_numbers0 = {
    'freddie': [10],
    'payal': [4],
    'adam': [3, 19],
    'abe': [27],
    'jack': [3],
}

for person, numbers in favorite_numbers0.items():
    if len(numbers) > 1:
        print("\n" + person.title() + "'s favorite numbers are:")
    else:
        print("\n" + person.title() + "'s favorite number is:")
    for number in numbers:
        print(str(number))