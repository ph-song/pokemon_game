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

    def attacked_by(self, attacker: Type[PokemonBase]) -> None:
        attacker_attack = attacker.attack
        attack_multiplier = self.damage_multiplier(self.poke_type, attacker.poke_type)
        attacker_attack *= attack_multiplier

        if attacker.attack > self.defence:
            self.hp -= attacker_attack
        else:
            self.hp -= attacker_attack//2
        self.check_faint()

class Bulbasaur(PokemonBase):
    def __init__(self)-> None:
        PokemonBase.__init__(self, "Grass", 9, "Bulbasaur")
        self.attack = 5
        self.defence = 5
        self.speed = 7 + self.level//2
    
    def __str__(self)->str:
        ret = "{Pokemon_Name}'s HP = {hp} and level = {level}"
        return ret.format(Pokemon_Name = self.name, hp = self.hp, level = self.level)

    def attacked_by(self, attacker: Type[PokemonBase])-> None:
        #multiple attack
        attacker_attack = attacker.attack
        attack_multiplier = self.damage_multiplier(self.poke_type, attacker.poke_type)
        attacker_attack *= attack_multiplier

        if attacker.attack > self.defence+5:
            self.hp -= attacker_attack
        else:
            self.hp -= attacker_attack//2
        self.check_faint()

class Squirtle(PokemonBase):
    def __init__(self)-> None:
        PokemonBase.__init__(self, "Water", 8, "Squirtle")
        self.attack = 4 + self.level//2
        self.defence = 6 + self.level
        self.speed = 7

    def __str__(self)->str:
        ret = "{Pokemon_Name}'s HP = {hp} and level = {level}"
        return ret.format(Pokemon_Name = self.name, hp = self.hp, level = self.level)

    def attacked_by(self, attacker: Type[PokemonBase])-> None:
        attacker_attack = attacker.attack
        attack_multiplier = self.damage_multiplier(self.poke_type, attacker.poke_type)
        attacker_attack *= attack_multiplier

        if attacker.attack > self.defence*2:
            self.hp -= attacker_attack
        else:
            self.hp -= attacker_attack//2
        self.check_faint()
