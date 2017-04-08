people = [{
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
},
    {
    'username': 'mcurie',
    'first': 'marie',
    'last': 'curie',
},
    {
    'username': 'aeinstein',
    'first': 'albert',
    'last': 'einstein',
}]

print(people)
for person in people:
    username = person['username']
    first_name = person['first']
    last_name = person['last']

    print("\nUsername: " + username)
    print("First name: " + first_name.title())
    print("Last name: " + last_name.title())
