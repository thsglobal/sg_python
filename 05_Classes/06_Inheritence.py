# Inheritance & polymorphism

class Mammal:
    def __init__(self, name):
        self.warm_blooded = True
        self.name = name

    @staticmethod
    def reproduce():
        print("Giving birth to live young")


class Horse(Mammal):
    def __init__(self, name):
        super().__init__(name)  # Parent constructor, super() = parent
        self.legs = 4

    @staticmethod
    def reproduce():
        print("Giving birth to live foals")


class Platypus(Mammal):
    def __init__(self, name):
        super().__init__(name)
        self.poisonous_barbs = True

    @staticmethod
    def reproduce():
        print("Laying eggs")


m = Mammal("Harambe")
h = Horse("H.O.R.S.E.")
p = Platypus("Mr Quackers")

print(h.warm_blooded)
h.reproduce()
p.reproduce()
Mammal(p).reproduce()
