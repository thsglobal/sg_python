def woof(n):
    print("WOOF!" * n)


def greeting(name):
    print(f"Good morning {name}!")


# Type hints are a suggestion and are not enforced!
def double_plus_num(num1: int, num2: int =2) -> int:
    """
    Double the first number and adds it to the second

    :param num1: The integer to be doubled
    :param num2: The integer to add
    :return: The result of the equation
    """
    ans = (num1 * 2) + num2
    return ans


def shopping(name: str, *items: str, shout=False):  # multiple args given by *, taken as tuple
    print(items, type(items))
    if shout:
        name = name.upper()
    for item in items:
        print(f"{name}! Don't forget to buy an {item}")


greeting("Tom")
woof(double_plus_num(5))

shopping("Tom", "Banana", "Apple", "Orange", shout=True)
double_plus_num()