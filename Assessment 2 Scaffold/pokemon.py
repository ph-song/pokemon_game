from pokemon_base import PokemonBase
from typing import Type 

class Charmander(PokemonBase):
    def __init__(self)-> None:
        PokemonBase.__init__(self, "Fire", 7, "Charmander")
        self.attack = self.level + 6
        self.defence = 4
        self.speed = 7 + self.level
    
    def __str__(self)->str:
        ret = "{Pokemon_Name}'s HP = {hp} and level = {level}"
        return ret.format(Pokemon_Name = self.name, hp = self.hp, level = self.level)

class Bulbasaur(PokemonBase):
    def __init__(self)-> None:
        PokemonBase.__init__(self, "Grass", 9, "Bulbasaur")
        self.attack = 5
        self.defence = 5
        self.speed = 7 + self.level//2
    
    def __str__(self)->str:
        ret = "{Pokemon_Name}'s HP = {hp} and level = {level}"
        return ret.format(Pokemon_Name = self.name, hp = self.hp, level = self.level)

class Squirtle(PokemonBase):
    def __init__(self)-> None:
        PokemonBase.__init__(self, "Water", 8, "Squirtle")
        self.attack = 4 + self.level//2
        self.defence = 6 + self.level
        self.speed = 7

    def __str__(self)->str:
        ret = "{Pokemon_Name}'s HP = {hp} and level = {level}"
        return ret.format(Pokemon_Name = self.name, hp = self.hp, level = self.level)
