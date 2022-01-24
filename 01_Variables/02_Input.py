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


# tree
class Tree:
    def __init__(self, value, left, right):
        Tree.value = value
        Tree.left = left
        Tree.right = right

    def binarySearch(self, value):
        if (Tree.value is None or type(value) != int):
            return False
        elif (Tree.value == value):
            return True
        elif (Tree.value > value):
            if (Tree.left is None):
                return False
            else:
                return Tree.left.binarySearch(value)
        elif (Tree.value < value):
            if (Tree.right is None):
                return False
            else:
                return Tree.right.binarySearch(value)
        else:
            return False


root = Tree(5, Tree(3, Tree(1, None, None), Tree(4, None, None)), Tree(8, Tree(6, None, None), Tree(9, None, None)))
print("Search for 3: ", root.binarySearch((3)))
print("Search for 7: ", root.binarySearch((7)))
