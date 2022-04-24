from pokemon_base import PokemonBase
from typing import Type 
from random import randint
from abc import ABC, abstractmethod


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

    def attacked_by(self, attacker: Type[PokemonBase]) -> None:
        """
        pokemon initiate attack, argument is defender
        hp of attacker and defenser both must be positive
        """
        attacker_damage = attacker.get_attack() * attacker.damage_multiplier(self)
        if attacker_damage > self.get_defence():
            self.set_hp(self.get_hp() - attacker_damage)
        else:
            self.set_hp(self.get_hp() - attacker_damage//2)
    
    def get_attack(self):
        """return pokemon attack"""
        return self.ATTACK + self.get_level()
    
    def get_defence(self):
        """pokemon defence getter"""
        return self.DEFENCE
    
    def get_speed(self):
        """return pokemon speed"""
        return self.SPEED + self.get_level()


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
        return self.ATTACK
    
    def get_defence(self):
        """pokemon defence getter"""
        return self.DEFENCE
    
    def get_speed(self):
        """return pokemon speed"""
        return self.SPEED + self.get_level()//2

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
        return self.ATTACK + self.get_level()//2
    
    def get_defence(self):
        """pokemon defence getter"""
        return self.DEFENCE + self.get_level()
    
    def get_speed(self):
        """return pokemon speed"""
        return self.SPEED


class GlitchMon(PokemonBase): #is ABC nessesary
    POKE_TYPE = None

    def __init__(self, hp: int, name: str)-> None:
        PokemonBase.__init__(self, hp, self.POKE_TYPE) #downcasting?
        self.name = name

    def attacked_by(self, attacker: Type[PokemonBase]) -> None:
        if randint(1,4) == 1: #1 out of 4 gives 25% chance
            self.super_power()
        self.set_hp(self.get_hp() - attacker.get_attack())

    def super_power(self):
        i = randint(0,2)
        if i == 0:
            self.set_hp(self.get_hp() +1)
        elif i == 1:
            self.set_level(self.get_level()+1)
        elif i == 2:
            self.set_hp(self.get_hp() +1)
            self.set_level(self.get_level()+1)

    @abstractmethod
    def get_attack(self):
        """return pokemon attack"""
        pass
    
    @abstractmethod
    def get_defence(self):
        """pokemon defence getter"""
        pass
    
    @abstractmethod
    def get_speed(self):
        """return pokemon speed"""
        pass

class MissingNo(GlitchMon):
    HP = (Charmander.HP+Bulbasaur.HP+Squirtle.HP)/3
    MYST_NAME = "MissingNo"

    def __init__(self)-> None:
        GlitchMon.__init__(self, self.HP, self.MYST_NAME)

    def get_attack(self):
        """return pokemon attack"""
        sum = Charmander.ATTACK + self.get_level() + Bulbasaur.ATTACK + Squirtle.ATTACK + self.get_level()//2
        return sum/3 + self.get_level() -1
    
    def get_defence(self):
        """pokemon defence getter"""
        sum = Charmander.DEFENCE + Bulbasaur.DEFENCE + Squirtle.DEFENCE + self.get_level()
        return sum/3 + self.get_level() -1
    
    def get_speed(self) -> int:
        """return pokemon speed"""
        sum = Charmander.SPEED + self.get_level() + Bulbasaur.SPEED + self.get_level()//2 + Squirtle.SPEED
        return sum/3 + self.get_level() -1


"""
m = MissingNo()



print(m.get_hp(), m.get_level(), m.get_type(), m.get_name())
c =Charmander()

print('before fight\n', m.get_attack(), m.get_defence(), m.get_speed(), m.get_hp())

m.attacked_by(c)
print('after fight\n', m.get_attack(), m.get_defence(), m.get_speed(), m.get_hp())

m = MissingNo()
print('before level up\n', m.get_attack(), m.get_defence(), m.get_speed())

m.set_level(m.get_level() +1 )
print('after level up\n', m.get_attack(), m.get_defence(), m.get_speed())

m.set_level(m.get_level() +1 )
print('after level up\n', m.get_attack(), m.get_defence(), m.get_speed())
"""