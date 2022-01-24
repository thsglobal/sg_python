pokedex = {'Bulbasaur', "Squirtle", "Charmander"}

print(pokedex, type(pokedex))

pokedex.add("Pikachu")
print(pokedex)

# Sets are mutable and unordered

pokedex.discard("Bulbasaur")
print(pokedex)

pokedex.add("Bulbasaur")
pokedex.add("Bulbasaur")
print(pokedex)

# Sets can remove the duplicate values in a list
l = [1, 2, 3, 4 ,3 ,2, 1, 2, 3, 4]
print(l)
print(set(l))

# Frozen Set: immutable set

x = frozenset(['let', 'it', 'go'])
print(x)