python_glossary0 = {
    'for loop': 'def for loop',
    'dictionary': 'def dictionary',
    'if statements': 'def if statements',
    'elif statements': 'def elif statements',
    'else statements': 'def else statements',
    'list': 'def list',
    'while loops': 'while loops not yet defined',
    'functions': 'functions not yet defined',
    'classes': 'classes not yet defined',
}

print("Glossary of Python Terms:")

for k, v in sorted(python_glossary0.items()):
    print("\n" + k.title() + ":")
    print(v)

python_glossary0['git'] = 'def of git'
print(python_glossary0)

for k, v in sorted(python_glossary0.items()):
    print("\n" + k.title() + ":")
    print(v)
