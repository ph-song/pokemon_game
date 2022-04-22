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
        PokemonBase.__init__(self, self.HP, self.POKE_TYPE)
        self.name = self.NAME 
        self.hp = self.HP
        self.defence = self.DEFENCE
        self.attack = self.ATTACK
        self.speed = self.SPEED

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
    
    def get_attack(self):
        """return pokemon attack"""
        return self.attack + self.get_level()
    
    def get_defence(self):
        """pokemon defence getter"""
        return self.defence 
    
    def get_speed(self):
        """return pokemon speed"""
        return self.speed + self.get_level()


class Bulbasaur(PokemonBase):

    ATTACK = 5
    DEFENCE = 5
    SPEED = 7
    HP = 9
    POKE_TYPE = "Grass"
    NAME = "Bulbasaur"

    def __init__(self)-> None:
        PokemonBase.__init__(self, self.HP, self.POKE_TYPE)
        self.name = self.NAME
        self.hp = self.HP
        self.defence = self.DEFENCE
        self.attack = self.ATTACK
        self.speed = self.SPEED

    def attacked_by(self, attacker: Type[PokemonBase]) -> None:
        """
        pokemon initiate attack, argument is defenser
        hp of attacker and defender both must be positive
        """
        attacker_damage = attacker.get_attack() * attacker.damage_multiplier(self)
        if attacker_damage > self.get_defence() + 5 :
            self.set_hp(self.get_hp() - attacker_damage)
        else:
            self.set_hp(self.get_hp() - attacker_damage//2)
        
    def get_attack(self):
        """return pokemon attack"""
        return self.attack
    
    def get_defence(self):
        """pokemon defence getter"""
        return self.defence 
    
    def get_speed(self):
        """return pokemon speed"""
        return self.speed + self.get_level()//2

class Squirtle(PokemonBase):

    ATTACK = 4
    DEFENCE = 6
    SPEED = 7
    HP = 8
    POKE_TYPE = "Water"
    NAME = "Squirtle"

    def __init__(self)-> None:
        PokemonBase.__init__(self, self.HP, self.POKE_TYPE)
        self.name = self.NAME
        self.hp = self.HP
        self.defence = self.DEFENCE
        self.attack = self.ATTACK
        self.speed = self.SPEED

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

    def get_attack(self):
        """return pokemon attack"""
        return self.attack + self.get_level()//2
    
    def get_defence(self):
        """pokemon defence getter"""
        return self.defence + self.get_level()
    
    def get_speed(self):
        """return pokemon speed"""
        return self.speed

    