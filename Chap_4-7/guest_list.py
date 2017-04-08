dead_people = ['hunter s. thompson', 'paul newman', 'steve jobs', 'benjamin franklin']
print(dead_people)

message = "Yo " + dead_people[0].title() + ", you wanna come to dinner?"
print(message)

message = "Yo " + dead_people[1].title() + ", you wanna come to dinner?"
print(message)

message = "Yo " + dead_people[2].title() + ", you wanna come to dinner?"
print(message)

message = "Yo " + dead_people[3].title() + ", you wanna come to dinner?"
print(message)

not_coming = dead_people.pop(2)
print("\nActually, " + not_coming.title() + " can't make it.")

dead_people.insert(2, 'winston churchill')

message = "\nYo " + dead_people[0].title() + ", you wanna come to dinner?"
print(message)

message = "Yo " + dead_people[1].title() + ", you wanna come to dinner?"
print(message)

message = "Yo " + dead_people[2].title() + ", you wanna come to dinner?"
print(message)

message = "Yo " + dead_people[3].title() + ", you wanna come to dinner?"
print(message)

print("\nWe found a bigger table! That means we can invite more guests! We're going to find some guests to invite.")

dead_people.insert(0, 'benjamin franklin')

dead_people.insert(2, 'albert einstein')

dead_people.append('johnny carson')

print(dead_people)

message = "\nYo " + dead_people[0].title() + ", you wanna come to dinner?"
print(message)

message = "Yo " + dead_people[1].title() + ", you wanna come to dinner?"
print(message)

message = "Yo " + dead_people[2].title() + ", you wanna come to dinner?"
print(message)

message = "Yo " + dead_people[3].title() + ", you wanna come to dinner?"
print(message)

message = "Yo " + dead_people[4].title() + ", you wanna come to dinner?"
print(message)

message = "Yo " + dead_people[5].title() + ", you wanna come to dinner?"
print(message)

message = "Yo " + dead_people[6].title() + ", you wanna come to dinner?"

len(dead_people)

print(message)
print("\nAt the moment, we are inviting " + str(len(dead_people)) + " guests.")

print("\nShoot! It looks like not everyone can come, we're gonna have to disinvite some of you dead guys.")

popped_guy = dead_people.pop()
print("\nSorry " + popped_guy.title() + ", we don't have room for you anymore.")

popped_guy = dead_people.pop()
print("Sorry " + popped_guy.title() + ", we don't have room for you anymore.")

popped_guy = dead_people.pop()
print("Sorry " + popped_guy.title() + ", we don't have room for you anymore.")

popped_guy = dead_people.pop()
print("Sorry " + popped_guy.title() + ", we don't have room for you anymore.")

popped_guy = dead_people.pop()
print("Sorry " + popped_guy.title() + ", we don't have room for you anymore.")

message = "\nYo " + dead_people[0].title() + ", we still want you there."
print(message)

message = "\nYo " + dead_people[1].title() + ", we still want you there."
print(message)

del dead_people[0]

del dead_people[0]

print(dead_people)

print(len(dead_people))


