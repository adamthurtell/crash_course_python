my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

# this part: [:] makes friend_foods copy the my_foods list.
# If we omit that, it would point both variables to the same list

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

