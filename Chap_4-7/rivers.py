rivers0 = {
    'nile': 'egypt',
    'yangtze': 'china',
    'ganges': 'india',
    'mississippi': 'united states',
    'amazon river': 'brazil',
    'danube': 'europe',
    'euphrates': 'western asia',
    'congo': 'africa',
    'indus': 'south asia',
    'yukon': 'north america',
}

for k, v in sorted(rivers0.items()):
    print("\nThe " + k.title() + " River runs through " + v.title() + ".")

print("\nThe rivers on our list are: \n")
for k, v in sorted(rivers0.items()):
    print(k.title())

print("\nThe countries and regions with rivers on our list are: \n")
for k, v in sorted(rivers0.items()):
    print(v.title())