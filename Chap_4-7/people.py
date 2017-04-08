person_0 = {
    'first_name': 'payal',
    'last_name': 'jain',
    'birthday': 'April 19, 1982',
    'height': '4\' 10"',
    'city': 'pasadena',
}

print(person_0['first_name'].title() + "'s stats: \n")

for info in person_0.values():
    print(info.title())