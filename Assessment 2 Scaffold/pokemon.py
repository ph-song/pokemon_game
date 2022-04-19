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

    def attacked(self, defender: Type[PokemonBase]) -> None:
        """
        pokemon initiate attack, argument is defenser
        hp of attacker and defenser both must be positive
        """
        attacker_attack = int(self.get_attack() * self.damage_multiplier(defender))

        if self.attack > defender.defence:
            defender.set_hp(self.get_hp() - attacker_attack)
        else:
            defender.set_hp(self.get_hp() - attacker_attack//2)



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

    def attacked(self, defender: Type[PokemonBase]) -> None:
        """
        pokemon initiate attack, argument is defenser
        hp of attacker and defenser both must be positive
        """
        attacker_attack = int(self.get_attack() * self.damage_multiplier(defender))

        if self.attack > defender.get_defence() + 5:
            defender.set_hp(self.get_hp() - attacker_attack)
        else:
            defender.set_hp(self.get_hp() - attacker_attack//2)

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
    
    def attacked(self, defender: Type[PokemonBase]) -> None:
        """
        pokemon initiate attack, argument is defenser
        hp of attacker and defenser both must be positive
        """
        attacker_attack = int(self.get_attack() * self.damage_multiplier(defender))

        if self.attack > defender.get_defence() * 2:
            defender.set_hp(self.get_hp() - attacker_attack)
        else:
            defender.set_hp(self.get_hp() - attacker_attack//2)

c = Charmander()
b = Bulbasaur()
s = Squirtle()
