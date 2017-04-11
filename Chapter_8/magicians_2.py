def show_magicians(magicians):
    print("\nThe names of the magicians are:")
    for magician in magicians:
        print(magician)

def make_great(magicians, great_magicians):
    """Add 'the Great' to Magicians names"""
    while magicians:
        great_magician = magicians.pop()

        print("\n" + great_magician + " is becoming great...")
        great_magician = great_magician + " the Great"
        great_magicians.append(great_magician)

magicians = ['David Copperfield', 'David Blaine', 'Houdini']
poopheads = ['poophead1', 'poophead2', 'poophead3']
great_magicians = []
great_poopheads = []
show_magicians(magicians)
make_great(magicians[:], great_magicians)
show_magicians(great_magicians)
show_magicians(magicians)
make_great(poopheads, great_poopheads)
show_magicians(great_poopheads)