class Dog:
    def __init__(self, breed):  # Initialisation; (double underscore) init
        self.animal_kind = "canine"  # Class Variable
        self.legs = 4
        self.breed = breed
        self.sound = "Woof!"

    def make_noise(self):
        print(self.loud_bark())

    def bark(self, num_woofs=1):
        return self.sound * num_woofs

    def loud_bark(self):
        return self.bark().upper()


class Crab:
    def __init__(self, colour="Orange", legs=8, sound="Skitter!"):
        self.animal_kind = "crustacean"
        self.legs = legs
        self.colour = colour
        self.sound = sound

    def make_noise(self):
        print(self.sound)

    @staticmethod
    def walk(num_steps):
        return "Waddle! " * num_steps

    @staticmethod
    def pinch(animal):
        animal.make_noise()
        print("I pinched a " + animal.animal_kind)


fido = Dog("Dalmatian")
print(fido, type(fido))
print(fido.animal_kind)
print(fido.bark(3))
print(fido.loud_bark())

lassie = Dog("Corgi")  # Instantiate object
pluto = Dog("Poodle")

lassie.animal_kind = "feline"

print(lassie.animal_kind)
print(pluto.animal_kind)

Dog.animal_kind = "arachnid" # doesn't work if animal_kind is set in __init__
print(fido.animal_kind)

fido.legs = 3
print(fido.legs)

mr_krabs = Crab("Red",2,"Money!")
mr_krabs.pinch(fido)
mr_krabs.pinch(mr_krabs)
