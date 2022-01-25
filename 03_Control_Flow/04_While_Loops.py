i = 1
flag = True
break_for = False

while flag:
    if i == 4:
        print("FOUR!")
        flag = False
    else:
        print(i)
    i += 1

print("Loop Finished")

for x in ['a','b','c','d','e']:
    i = 100
    while i < 110:
        print(x ,i)
        if x == 'b' and i == 105:
            break_for = True
            break
        i += 1
    if break_for:
        break

max_age = 119

age = input("What is your age?\n")
while True:
    while not age.isdigit():
        print("Please enter your age in digits")
        age = input("What is your age?\n")
    if int(age) > max_age:
        print("The age entered is to large")
        age = "?"
    else:
        break

int_age = int(age)
print(f"In ten years time you will be {int_age+10}!")