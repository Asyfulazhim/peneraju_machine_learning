import random

class Pokemon:
    def __init__(self, name, health, element):
        self.name = name
        self.health = health
        self.element = element

    def doMove(self):
        print("Pokemon Move:")
        
    def doEat(self):
        print("Pokemon Eat")
        

class Jigglypuff(Pokemon):
    def __init__(self,name, health, element, lungCapacity):
        super().__init__(name, health, element)
        self.lungCapacity = lungCapacity
    
    def doMove(self):
        super().doMove()
        print("Jigglypuff can Float")

    def __str__(self):
        return f"Name: {self.name}\nHealth: {self.health}\nElement: {self.element}\nLung Capacity: {self.lungCapacity}"
    
class Pikachu(Pokemon):
    def __init__(self, name, health, element, electricity):
        super().__init__(name, health, element)
        self.electricity = electricity

    def doMove(self):
        super().doMove()    # override mode
        print("Pikachu can Jump")

    def __str__(self):
        return f"Name: {self.name}\nHealth: {self.health}\nElement: {self.element}\nElectricity: {self.electricity}"

# pokemon = Jigglypuff("J1", 75, "fairy", 92)
# pokemon.doMove()
class Game:

    def __init__(self):
        self.elements = ["Thunder", "Fire", "Water", "Ghost"]
        self.pokemons = {
            "jigglypuff":[Jigglypuff(f"J{i}", random.randint(50,100),self.elements[random.randint(0,len(self.elements) - 1)], random.randint(50,100)) for i in range (0,random.randint(3,15))],
            "pikachu":[Pikachu(f"P{i}", random.randint(50,100),self.elements[random.randint(0,len(self.elements)-1)], random.randint(50,100)) for i in range (0,random.randint(5,20))]
        }
        
    def __str__(self):
        message = ""
        for pokemonname, pokemonlist in self.pokemons.items():
            for pokemon in pokemonlist:
                message = message + pokemon.__str__() + "\n" + ("-"*20) + "\n"
        return message

game = Game()
print(game)

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Thunderbolt(Weapon):
    def __init__(self):
        super().__init__()

class Fireball(Weapon):
    def __init__(self):
        super().__init__()