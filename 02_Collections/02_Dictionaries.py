# Dictionaries (hash maps)

# Key-Value Pairs

my_dict = {"Key": "value"}

table = {
    "name": "The Table",
    "Colour": "Light brown",
    "dimensions": {
        "Height": 120,
        "Length": 200,
        "Width": 150
    }
}

print(table)
print(table["Colour"])

table["dimensions"]["Height"] = 125
table["Price"] = 99.99
print(table)

table.update({"Price": 100, "name": "superTable"})
print(table)

table.get("Price")  # Cannot be used to alter the price
table["Price"] = 120
print(table["Price"])

table.pop("Colour")
print(table)

print(table.keys())
print(table.values())
print(table.items())