print("\nQ1a\n")


# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:


def divisors_of(num: int) -> [int]:
    int_list = []
    for i in range(1, num + 1):
        if num % i == 0:
            int_list.append(i)
    return int_list


print(divisors_of(12))

print("\nQ1b\n")


# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:

# Two equivalent returns, more efficient not to use previous function
def is_factor(num1: int, num2: int) -> bool:
    return num2 in divisors_of(num1)
    # return num1 % num2 == 0 or num2 % num1 == 0


print(is_factor(2, 12))

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs its position in the alphabet
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a:


def letter_index(char: str) -> str:
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for index, letter in enumerate(alphabet):
        if char.lower() == letter:
            return str(index)
    return ""


print(letter_index('E'))

print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:


def create_id(name: str) -> str:
    retval = ""
    for letter in name:
        retval += letter_index(letter)
    return retval


print(create_id("Bob"))

print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:


def create_password(name: str) -> str:
    password = int(create_id(name))
    for letter in name:
        for digit in letter_index(letter):
            password -= int(digit)
    return str(password)


print(create_password("Bob"))

# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:


def is_prime(num: int) -> bool:
    lim = int((num ** 0.5) + 1)
    for i in range(2, lim):
        if num % i == 0:
            return False
    return True


print(is_prime(17))
print(is_prime(121))

print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:


def is_prime(num: int) -> bool:
    if type(num) != int:
        return None
    lim = int((num ** 0.5) + 1)
    for i in range(2, lim):
        if num % i == 0:
            return False
    return True


print(is_prime(17))
print(is_prime(121))
print(is_prime("Not a number"))
# -------------------------------------------------------------------------------------- #
