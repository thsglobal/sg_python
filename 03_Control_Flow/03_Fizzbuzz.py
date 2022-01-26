import math

# Set the values of the constants
min_range = 1
max_range = 10000

default_begin = 1
default_end = 100

default_fizz = "Fizz"
default_buzz = "Buzz"

default_first = 3
default_second = 5

# Set the text to be displayed to the user
yes = "Y"
no = "N"

reset = "Reset"
invalid = "Invalid input!\n"

yes_no = "(" + yes + "/" + no + ")"
start_range = "(" + str(min_range) + "-" + str(max_range - 1) + ")"
end_range = "(" + str(min_range) + "-" + str(max_range) + ")"

confirm_range = "Would you like to set the range " + yes_no + "?\n"
question_start = "What number would you like to start from " + start_range + "?\n"
question_end = "What number would you like to end " + end_range + "?\n"

confirm_words = "Would you like to set the magic words " + yes_no + "?\n"
question_fizz = "What would you like the first word to be?\n"
question_buzz = "What would you like the second word to be?\n"

confirm_primes = "Would you like to set the magic numbers " + yes_no + "?\n"
question_first = "What would you like the first number to be?\n"
question_second = "What would you like the second number to be?\n"


# Define useful condition checks
def is_string(answer: str) -> bool:
    return answer.isalpha()


def is_number(answer: str) -> bool:
    return answer.isdigit()


def is_yes_no(answer: str) -> bool:
    return answer == yes or answer == no


# Helper function to ask a question to the user
def ask_question(input_func, question, condition) -> str:
    answer = input_func(question)
    while not condition(answer):
        answer = input_func(invalid + question)
    return answer


# Helper function to ask a yes-no question to the user
def ask_confirm(question: str) -> bool:
    return ask_question(input, question, is_yes_no) == yes


# Function for setting the custom range
def set_range():
    # Internal helper function for asking for a value in a range
    def input_range(question: str, _lower: int, _upper: int):
        answer = input(question)
        if answer.isdigit():
            if int(answer) < _lower or int(answer) > _upper:
                answer = reset
        return answer

    if ask_confirm(confirm_range):
        def input_start(question: str):
            return input_range(question, min_range, max_range - 1)
        lower = int(ask_question(input_start, question_start, is_number))

        def input_end(question: str):
            return input_range(question, lower, max_range)
        upper = int(ask_question(input_end, question_end, is_number))

        return lower, upper
    else:
        return default_begin, default_end


# Function for setting custom fizzbuzz words
def set_words():
    if ask_confirm(confirm_words):
        return ask_question(input, question_fizz, is_string), ask_question(input, question_buzz, is_string)
    else:
        return default_fizz, default_buzz


# Function for setting custom fizzbuzz numbers
def set_primes():
    if ask_confirm(confirm_primes):
        first = int(ask_question(input, question_first, is_number))

        def input_second(question: str):
            answer = input(question)
            if answer.isdigit():
                if math.gcd(int(answer), first) != 1:
                    answer = reset
            return answer
        second = int(ask_question(input_second, question_first, is_number))
        return first, second
    else:
        return default_first, default_second


# Function for playing fizzbuzz
def play_fizzbuzz():
    begin, end = set_range()
    fizz, buzz = set_words()
    num_f, num_b = set_primes()
    num_fb = num_f * num_b
    fizzbuzz = fizz + buzz

    for i in range(begin, end + 1):
        if i % num_fb == 0:
            print(fizzbuzz)
        elif i % num_f == 0:
            print(fizz)
        elif i % num_b == 0:
            print(buzz)
        else:
            print(i)


# Play a game of fizzbuzz
play_fizzbuzz()