# Set the values of the constants

yes = "Y"
no = "N"

min_range = 1
max_range = 10000

reset = "Reset"
invalid = "Invalid input!\n"

yes_no = "(" + yes + "/" + no + ")"
start_range = "(" + str(min_range) + "-" + str(max_range - 1) + ")"
end_range = "(" + str(min_range) + "-" + str(max_range) + ")"

question_range = "Would you like to set the range " + yes_no + "?\n"
question_start = "What number would you like to start from " + start_range + "?\n"
question_end = "What number would you like to end " + end_range + "?\n"

question_words = "Would you like to set the magic words " + yes_no + "?\n"
question_fizz = "What would you like the first word to be?\n"
question_buzz = "What would you like the second word to be?\n"

# Set the initial values of the variables

num_f = 3
num_b = 5

str_f = "Fizz"
str_b = "Buzz"

begin = 1
end = 100

# Ask for a custom range
ans = input(question_range)
while ans != yes and ans != no:
    ans = input(invalid + question_range)

# Set the custom range
if ans == yes:
    # Set the start
    ans = input(question_start)
    if ans.isnumeric():
        if int(ans) < min_range or int(ans) > max_range - 1:
            ans = reset
    while not ans.isnumeric():
        ans = input(invalid + question_start)
        if ans.isnumeric():
            if int(ans) < min_range or int(ans) > max_range - 1:
                ans = reset
    begin = int(ans)

    # Set the end
    ans = input(question_end)
    if ans.isnumeric():
        if int(ans) < min_range or int(ans) > max_range or int(ans) < begin:
            ans = reset
    while not ans.isnumeric():
        ans = input(invalid + question_end)
        if ans.isnumeric():
            if int(ans) < min_range or int(ans) > max_range or int(ans) < begin:
                ans = reset
    end = int(ans)

# Ask for a custom fizzbuzz words
ans = input(question_words)
while ans != yes and ans != no:
    ans = input(invalid + question_words)

# Set custom fizzbuzz words
if ans == yes:
    # Set the value of fizz
    ans = input(question_fizz)
    while not ans.isalpha():
        ans = input(invalid + question_fizz)
    str_f = ans

    # Set the value of buzz
    ans = input(question_buzz)
    while not ans.isalpha():
        ans = input(invalid + question_buzz)
    str_b = ans

# Find the FizzBuzz numbers

num_fb = num_f * num_b
str_fb = str_f + str_b

# Play FizzBuzz with the current values of the variables

for i in range(begin, end + 1):
    if i % num_fb == 0:
        print(str_fb)
    elif i % num_f == 0:
        print(str_f)
    elif i % num_b == 0:
        print(str_b)
    else:
        print(i)
