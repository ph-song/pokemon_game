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
        """ Initialiser method of Charmander class.

        :pre: hp >= 0
        :complexity: O(1), __init__ method of parent class PokemonBase is O(1),
                     assignments have constant cost,
                     Best case = Worst case because no element properties can change this
        """
        PokemonBase.__init__(self, self.HP, self.POKE_TYPE)
        self.name = self.NAME 

    def attacked_by(self, attacker: Type[PokemonBase]) -> None:
        """ Pokemon initiates attack.

        :param arg1: the attacker
        :complexity: O(1), numerical comparison, numerical arithmetic and assignments have constant cost,
                     get_hp(), get_attack(), damage_multiplier(), get_defence(), set_hp() are all O(1),
                     Best case = Worst case because no element properties can change this
        """
        # calculates the effective damage
        attacker_damage = attacker.get_attack() * attacker.damage_multiplier(self)

        # check if attacker's damage is greater than defender's defence
        if attacker_damage > self.get_defence():
            self.set_hp(self.get_hp() - attacker_damage)
        else:
            self.set_hp(self.get_hp() - attacker_damage//2)
    
    def get_attack(self):
        """ Attribute attack getter.

        :complexity: O(1), return statements and numerical arithmetic have constant cost,
                     get_level() is O(1),
                     Best case = Worst case because no element properties can change this
        """
        return self.ATTACK + self.get_level()
    
    def get_defence(self):
        """ Attribute defence getter.

        :complexity: O(1), return statements have constant cost,
                     Best case = Worst case because no element properties can change this
        """
        return self.DEFENCE
    
    def get_speed(self):
        """ Attribute speed getter.

        :complexity: O(1), return statements and numerical arithmetic have constant cost,
                     get_level() is O(1),
                     Best case = Worst case because no element properties can change this
        """
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
        """ Pokemon initiates attack.

        :param arg1: the attacker
        :complexity: O(1), numerical comparison, numerical arithmetic and assignments have constant cost,
                     get_hp(), get_attack(), damage_multiplier(), get_defence(), set_hp() are all O(1),
                     Best case = Worst case because no element properties can change this
        """
        # calculates the effective damage
        attacker_damage = attacker.get_attack() * attacker.damage_multiplier(self)

        # check if attacker's damage is greater than defender's defence + 5
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
        """ Initialiser method of Squirtle class.

        :pre: hp >= 0
        :complexity: O(1), __init__ method of parent class PokemonBase is O(1),
                     assignments have constant cost,
                     Best case = Worst case because no element properties can change this
        """
        PokemonBase.__init__(self, self.HP, self.POKE_TYPE)
        self.name = self.NAME

    def attacked_by(self, attacker: Type[PokemonBase]) -> None:
        """ Pokemon initiates attack.

        :param arg1: the attacker
        :complexity: O(1), numerical comparison, numerical arithmetic and assignments have constant cost,
                     get_hp(), get_attack(), damage_multiplier(), get_defence(), set_hp() are all O(1),
                     Best case = Worst case because no element properties can change this
        """
        # calculates the effective damage
        attacker_damage = attacker.get_attack() * attacker.damage_multiplier(self)

         # check if attacker's damage is greater than two times the defender's defence
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


class GlitchMon(PokemonBase):
    POKE_TYPE = None

    def __init__(self, hp: int, name: str)-> None:
        """ Initialiser method of GlitchMon class.

        :pre: hp >= 0
        :complexity: O(1), __init__ method of parent class PokemonBase is O(1),
                     assignments have constant cost,
                     Best case = Worst case because no element properties can change this
        """
        PokemonBase.__init__(self, hp, self.POKE_TYPE)
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

