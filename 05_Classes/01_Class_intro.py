class Dog:
    animal_kind = "canine"  # Class Variable

    def make_noise(self):
        print(self.loud_bark())

    def bark(self, num_woofs=1):
        return (" Woof! I am an a " + self.animal_kind) * num_woofs

    def loud_bark(self):
        return self.bark().upper()


class Crab:
    animal_kind = "crustacean"

    def make_noise(self):
        print("Skitter!")

    def walk(self, num_steps):
        return "Waddle! " * num_steps

    def pinch(self, animal):
        animal.make_noise()
        return "I pinched a " + animal.animal_kind


fido = Dog()
print(fido, type(fido))
print(fido.animal_kind)
print(fido.bark(3))
print(fido.loud_bark())

lassie = Dog()  # Instantiate object
pluto = Dog()

lassie.animal_kind = "feline"

print(lassie.animal_kind)
print(pluto.animal_kind)

Dog.animal_kind = "arachnid"
print(fido.animal_kind)
