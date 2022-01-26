class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):  # Representation of object, returns string. Ideally; copy and paste it to init a copy
        return f"Location(latitude={self.latitude}, longitude={self.longitude})"

    def __str__(self):  # Representation of object as a string, human readable
        return f"({self.latitude},{self.longitude})"


bham = Location(52.488647, -1.887249)

print(repr(bham))
print(bham)
print(f"The Birmingham academy is located at coordinates {bham}")


class Dog:
    def __init__(self, age):
        self.age = age

    def __repr__(self):  # for logging
        return f"Dog(age={self.age})"

    def __str__(self):  # for getting strings
        return f"A {self.age} year old Dog"

    def __format__(self, format_spec):
        if format_spec == "dog":
            return  f"A {self.age * 7} dog-years old Dog"
        else:
            return self.__str__()


fido = Dog(5)
print(fido)
print(f"{fido:dog}")