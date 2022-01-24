# math

i = 375  # int
f = 3.75  # float
c = 3j + 2  # complex

add = 3 + 5
subtract = 3 - 5
mult = 3 * 5
divide = 3 / 5  # Always casts to float
power = 3 ** 5  # Can do roots
modulo = 3 % 5
integerDiv = 13 // 3

# string

single = 'Single quote'
double = "String in double quote"
# mixed quotes not allowed, useful if you want one of the quotes in the string
quotedQuote = "Quote's quoute"
both = "This is Tom's \"string\"" # \ is escape characters

# Index and slicing

hi = "Hello World!"
print(hi[0])  # zero indexed arrays
print(hi[-1]) # count from end of string
print(hi[0:6])  # slicing, non-inclusive of end num
print(hi[3:8])  # prints lo wo

# Methods

white_space = "    lots of white space..."
print(white_space.rstrip("."))
print(white_space.lstrip().capitalize())
print(white_space.strip().count(" "))
print(white_space.replace("o","oooooo").replace("i","@@@@@").replace("w","v"))

pi = 3.14159265359
print(pi)
print(f"Pi to 0dp: {pi:.0f}")
print(f"Pi to 3dp: {pi:.3f}")
print(f"Pi to 5dp: {pi:.5f}")

score = 16
max_score = 26
print(f"You scored {score/max_score}")
print(f"You scored {score/max_score:.2f}")
print(f"You scored {score/max_score:%}")
print(f"You scored {score/max_score:.2%}")
print(f"You scored {score/max_score:.0%}")

# Boolean

t = True
f = False

print(t, type(t))
print(3 + 2 == 5)
print(12 % 3 == 0)
print(5 != 5)
print(1 < 100)
print(5 < 5)
print(5 <= 5)
print(5 >= 5)

age = 16
drink = 'alcohol'

print(age > 18 and drink == 'alcohol')
print(age > 18 or drink == 'alcohol')

hi = "fooんbar";

print(hi)
print(hi.isalpha())
print(hi.islower())
print(hi.isupper())
print(hi.startswith("foo"))
print(hi.endswith("bar"))

# casting

print("booleans")
print(bool(1))
print(bool(0))
print(bool(2))
print(bool(3))
print(bool(""))
print(bool("test"))
print(bool(None))
print(bool(0.0))
print(bool(0.1))
print(bool(-1))
print(bool([]))

#None

n = None
print(n, type(n))
print(bool(None))
print(n is None)
print(type(15) is int)

