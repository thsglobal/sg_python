# For Loops

l = ['a', 'b', 'c']

for letter in l:
    if letter == 'b':
        print(letter.upper())
    else:
        print(letter)

for i in range(1,11):
    for letter in l:
        print(i, letter)

dict = {"name" : "Tom", "Age" : 29, "Job": "Graduate"}

for entry in dict:
    print(dict[entry])

for key, val in dict.items():
    print(key, val)

for val in dict.values():
    print(val)

for index, letter in enumerate(l):
    print(index, letter)

for char in "Hello World!":
    print(char)