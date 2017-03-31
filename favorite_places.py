favorite_places = {
    'payal': ['spain', 'mexico'],
    'adam': ['san franciso', 'poop'],
    'abe': ['new york city'],
}

for name, places in favorite_places.items():
    if len(places) > 1:
        print("\n" + name.title() + "'s favorite places are:")
    else:
        print("\n" + name.title() + "'s favorite place is:")
    for place in places:
        print("\t" + place.title())