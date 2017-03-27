favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("Sarah's favorite language is " + favorite_languages['sarah'].title() +
      ".\n")

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")

print("\n")

for name in favorite_languages.keys():
    print(name.title())

print("\n")

# looping through the keys is actually the default behavior when looping through
    #  a dictionary, so the following words the same:

for name in favorite_languages:
    print(name.title())

# sometimes using the heys() method makes code easier to read

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if __name__ == '__main__':
        if name in friends:
            print(" Hi " + name.title() + ", I see your favorite language is " +
                  favorite_languages[name].title() + "!")

# you can also use the keys() method to find out if a particular person was
# polled

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

print("\n")

# use sorted() to loop through keys in order

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

print("\n")

# looping through values in a dictionary, w/o checking for repeats:

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# to use a list that doesn't use repeats, use a set:

print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

print("\n")

poll_candidates = ['erin', 'sarah', 'bob', 'jebediah']

for candidate in poll_candidates:
    if candidate not in favorite_languages.keys():
        print(candidate.title() + " you should take our poll!")
    elif candidate in favorite_languages.keys():
        print(candidate.title() + " thank you for taking our poll!")