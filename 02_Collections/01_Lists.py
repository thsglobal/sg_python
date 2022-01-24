# Lists

shopping_list = ["eggs", "bread", "bananas", "tea"]
print(shopping_list, type(shopping_list))

print(len(shopping_list))

print(shopping_list[0])
print(shopping_list[-1])

shopping_list[2] = "milk"
print(shopping_list)

shopping_list.append("biscuits")
print(shopping_list)

shopping_list.append("bread")
shopping_list.append("bread")
shopping_list.append("bread")
shopping_list.append("bread")
print(shopping_list)
print(shopping_list.count("bread"))

shopping_list.remove("bread")
print(shopping_list)

print(shopping_list.pop(-1))
print(shopping_list)

# Mixed lists

mixed = [1, 2, "three", True, None, ["another", "list"]]
print(mixed)

mixed[1] = 2.0  # lists are mutable
print(mixed)

print(mixed[2:4])
print(mixed[2:])
print(mixed[2:-1])
print(mixed[:0:-1])  # format is [begin:end:step] blank for default(0/last/1)

print(mixed[5][::-1])  # indexing for nested lists

sublist = mixed[5]  # makes a shallow copy / reference
sublist = mixed[5][:]  # makes a deep copy .copy() works too
print(sublist)
sublist[0] = '2'  # shallow copy
print(sublist)

# Tuples

colours = ("red", "blue", "green")
print(colours, type(colours))

# colours[0] = "maroon" does not work : Tuples are immutable

list_in_tuple = (
    [1,2,3],
    [4,5,6],
    [7,8,9]
)

print(len(list_in_tuple))
print(list_in_tuple[0][-1])
list_in_tuple[0][-1] = 4
print(list_in_tuple[0])