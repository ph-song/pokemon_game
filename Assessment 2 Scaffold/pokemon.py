from pokemon_base import PokemonBase
from typing import Type 

class Charmander(PokemonBase):

    ATTACK = 6
    DEFENCE = 4
    SPEED = 7
    HP = 7
    POKE_TYPE = "Fire"
    NAME = "Charmander"

    def __init__(self)-> None:
        PokemonBase.__init__(self, self.POKE_TYPE, self.HP, self.NAME, self.ATTACK, self.DEFENCE, self.SPEED)
        self.attack = self.level + self.ATTACK
        self.defence = self.DEFENCE
        self.speed = self.speed + self.level

    def attacked_by(self, attacker: Type[PokemonBase]) -> None:
        """
        pokemon initiate attack, argument is defenser
        hp of attacker and defenser both must be positive
        """
        attacker_damage = attacker.get_attack() * attacker.damage_multiplier(self)
        if attacker_damage > self.get_defence():
            self.set_hp(self.get_hp() - attacker_damage)
        else:
            self.set_hp(self.get_hp() - attacker_damage//2)



class Bulbasaur(PokemonBase):

    ATTACK = 5
    DEFENCE = 5
    SPEED = 7
    HP = 9
    POKE_TYPE = "Grass"
    NAME = "Bulbasaur"

    def __init__(self)-> None:
        PokemonBase.__init__(self, self.POKE_TYPE, self.HP, self.NAME, self.ATTACK, self.DEFENCE, self.SPEED)
        self.attack = self.attack
        self.defence = self.defence
        self.speed = self.speed + self.level//2

    def attacked_by(self, attacker: Type[PokemonBase]) -> None:
        """
        pokemon initiate attack, argument is defenser
        hp of attacker and defenser both must be positive
        """
        attacker_damage = attacker.get_attack() * attacker.damage_multiplier(self)
        if attacker_damage > self.get_defence() + 5 :
            self.set_hp(self.get_hp() - attacker_damage)
        else:
            self.set_hp(self.get_hp() - attacker_damage//2)

class Squirtle(PokemonBase):

    ATTACK = 4
    DEFENCE = 6
    SPEED = 7
    HP = 8
    POKE_TYPE = "Water"
    NAME = "Squirtle"

    def __init__(self)-> None:
        PokemonBase.__init__(self, self.POKE_TYPE, self.HP, self.NAME, self.ATTACK, self.DEFENCE, self.SPEED)
        self.attack = self.attack + self.level//2
        self.defence = self.defence + self.level
        self.speed = self.speed
    
    def attacked_by(self, attacker: Type[PokemonBase]) -> None:
        """
        pokemon initiate attack, argument is defenser
        hp of attacker and defenser both must be positive
        """
        attacker_damage = attacker.get_attack() * attacker.damage_multiplier(self)
        if attacker_damage > self.get_defence() * 2:
            self.set_hp(self.get_hp() - attacker_damage)
        else:
            self.set_hp(self.get_hp() - attacker_damage//2)


b1 = Bulbasaur()
b2 = Bulbasaur()
print(b1)
b1.attacked_by(b2)
print(b1)