age = 67

if age < 2:
    stage = 'a baby'
if age >= 2 and age < 4:
    stage = 'a toddler'
if age >= 4 and age < 13:
    stage = 'a kid'
if age >= 13 and age < 20:
    stage = 'a teenager'
if age >= 20 and age < 65:
    stage = 'an adult'
if age > 65:
    stage = 'an elder'

print("This person is " + stage + ".")