print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1a:
for i in range(5):
    print(x[i])


print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1b:
for i in range(len(x)):
    if x[i] % 2 == 0:
        print(x[i])


print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1c:
for i in range(5):
    if x[i] % 2 == 0:
        print(x[i])

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2a:
letters = []
for name in names:
    letters.append(name[0])
print(letters)

print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2b:
indices = []
for name in names:
    indices.append(name.index(" "))
print(indices)

print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2c:
initials = []
for name in names:
    initials.append(name[0] + name[name.index(" ") + 1])
print(initials)

# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = [[1,5,7,3,44,4,1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]


# A3a:
for sublist in list_of_lists:
    if len(sublist) == len(set(sublist)):
        print(sublist)

# -------------------------------------------------------------------------------------- #

print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

# A4a:
question = "Please input a number greater than 100:\n"
num = 0
ans = ""

while num < 100:
    ans = input(question)
    if ans.isdigit():
        num = int(ans)

print(f"The number you entered is {num}!\n")

print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise

# A4b:
isPrime = True
lim = int((num ** 0.5) + 1)
for i in range(2, lim):
    if num % i == 0:
        isPrime = False
        break

if isPrime:
    print("Prime!")
else:
    print("Not Prime!")
