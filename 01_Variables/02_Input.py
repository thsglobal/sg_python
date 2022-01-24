name = input("What is your name?\n")

print("Hello, " + name)
day = ""
while not day.isnumeric():
    day = input("What day were you born on\n")
day = int(day)

month = ""
while not month.isnumeric():
    month = input("What month were you born on\n")
month = int(month)

year = ""
while not year.isnumeric():
    year = input("What year were you born on\n")
year = int(year)

print(f"The day after your birthday is: {day + 1}/{month}/{year}")
