players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

print(players[1:4])

# without a starting index, python starts at the beginning of the list:
print(players[:4])

# without an ending index, python goes till the end:
print(players[2:])

# you can print the last x players by counting back from the end:
print(players[-3:])

# looping through a slice p. 66
print("\nHere are the first three players on my team:")
for player in players[:3]:
    print(player.title())
