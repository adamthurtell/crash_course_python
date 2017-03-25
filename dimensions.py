dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

print("\n")

for dimension in dimensions:
    print(dimension)

# Writing over a tuple, p 71

dimensions = (200, 50)
print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)


dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
