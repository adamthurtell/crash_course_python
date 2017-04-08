def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('dog', 'nala')
describe_pet('dog', 'einstein')
#incorrect order of call
describe_pet('einstin', 'dog')
describe_pet(pet_name='einstein', animal_type='dog')

# Same thing but using a default value for dog:

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('toby')