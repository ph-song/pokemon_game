from pokemon_base import PokemonBase
from typing import Type 
from random import randint
from abc import abstractmethod


class Charmander(PokemonBase):

    #Charmander attribute base value
    ATTACK = 6
    DEFENCE = 4
    SPEED = 7
    HP = 7
    POKE_TYPE = "Fire"
    NAME = "Charmander"

    def __init__(self)-> None:
        """ Charmander constructor

        :complexity: O(1), worst case = best case
        """
        PokemonBase.__init__(self, self.HP, self.POKE_TYPE)
        self.name = self.NAME 

    def attacked_by(self, attacker: Type[PokemonBase]) -> None:
        """ Charmander attacked by pokemon and lose hp

        :param arg1: the attacker
        :complexity: O(1), worst case = best case
        """
        attacker_damage = attacker.get_attack() * attacker.damage_multiplier(self) #effective damage

        #actual damage caused
        if attacker_damage > self.get_defence():
            self.set_hp(self.get_hp() - attacker_damage)
        else:
            self.set_hp(self.get_hp() - attacker_damage//2)
    
    def get_attack(self):
        """ return Charmander attack

        :complexity: O(1), worst case = best case
        """
        return self.ATTACK + self.get_level()
    
    def get_defence(self):
        """ return Charmander defence

        :complexity: O(1), worst case = best case
        """
        return self.DEFENCE
    
    def get_speed(self):
        """ return Charmander speed

        :complexity: O(1), worst case = best case
        """
        return self.SPEED + self.get_level()


class Bulbasaur(PokemonBase):

    #Balbasaur attributes base value
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
        """ Bulbasaur attacked by pokemon and lose hp

        :param arg1: the attacker
        :complexity: O(1), worse case = best case
        """
        attacker_damage = attacker.get_attack() * attacker.damage_multiplier(self) # effective damage

        #actual damage caused
        if attacker_damage > self.get_defence() + 5 :
            self.set_hp(self.get_hp() - attacker_damage)
        else:
            self.set_hp(self.get_hp() - attacker_damage//2)
        
    def get_attack(self):
        """return Bulbasaur attack"""
        return self.ATTACK
    
    def get_defence(self):
        """return Bulbasaur defence"""
        return self.DEFENCE
    
    def get_speed(self):
        """return Bulbasaur speed"""
        return self.SPEED + self.get_level()//2

class Squirtle(PokemonBase):

    #Squirtle attributes base value
    ATTACK = 4
    DEFENCE = 6
    SPEED = 7
    HP = 8
    POKE_TYPE = "Water"
    NAME = "Squirtle"

    def __init__(self)-> None:
        """ Squirtle constuctor

        :raise : hp >= 0
        :complexity: O(1), best case = worst case
        """
        PokemonBase.__init__(self, self.HP, self.POKE_TYPE)
        self.name = self.NAME

    def attacked_by(self, attacker: Type[PokemonBase]) -> None:
        """ Squirtle attacked by pokemon and lose hp

        :param arg1: the attacker
        :complexity: O(1), best case = worst case
        """
        # calculates the effective damage
        attacker_damage = attacker.get_attack() * attacker.damage_multiplier(self)

         # check if attacker's damage is greater than two times the defender's defence
        if attacker_damage > self.get_defence() * 2:
            self.set_hp(self.get_hp() - attacker_damage)
        else:
            self.set_hp(self.get_hp() - attacker_damage//2)

    def get_attack(self):
        """return Squirtle attack"""
        return self.ATTACK + self.get_level()//2
    
    def get_defence(self):
        """return Squirtle defence"""
        return self.DEFENCE + self.get_level()
    
    def get_speed(self):
        """return Squirtle speed"""
        return self.SPEED


class GlitchMon(PokemonBase):
    POKE_TYPE = None

    def __init__(self, hp: int, name: str)-> None:
        """ GlitchMon constructor 

        :pre: hp >= 0
        :complexity: O(1), worst case = best case
        """
        PokemonBase.__init__(self, hp, self.POKE_TYPE)
        self.name = name

    def attacked_by(self, attacker: Type[PokemonBase]) -> None:
        if randint(1,4) == 1: #1 out of 4 gives 25% chance
            self.super_power()
        self.set_hp(self.get_hp() - attacker.get_attack())

    def super_power(self):
        """GlitchMon superpower, increases GlitchMon hp or level or both by one

        :complexity: O(1), worst case = best case
        """
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
        """return GlitchNo attack
        
        :complexity: O(1), worst case = best case
        """
        pass
    
    @abstractmethod
    def get_defence(self):
        """return GlitchNo defence
        
        :complexity: O(1), worst case = best case
        """
        pass
    
    @abstractmethod
    def get_speed(self):
        """return GlitchNo speed
        
        :complexity: O(1), worst case = best case
        """
        pass

class MissingNo(GlitchMon):
    HP = (Charmander.HP+Bulbasaur.HP+Squirtle.HP)/3
    MYST_NAME = "MissingNo"

    def __init__(self)-> None:
        GlitchMon.__init__(self, self.HP, self.MYST_NAME)

    def get_attack(self):
        """return MissingNo attack
        
        :complexity: O(1), worst case = best case
        """
        sum = Charmander.ATTACK + self.get_level() + Bulbasaur.ATTACK + Squirtle.ATTACK + self.get_level()//2
        return sum/3 + self.get_level() -1
    
    def get_defence(self):
        """return MissingNo defence
        
        :complexity: O(1), worst case = best case
        """
        sum = Charmander.DEFENCE + Bulbasaur.DEFENCE + Squirtle.DEFENCE + self.get_level()
        return sum/3 + self.get_level() -1
    
    def get_speed(self) -> int:
        """return MissingNo speed
        
        :complexity: O(1), worst case = best case
        """
        sum = Charmander.SPEED + self.get_level() + Bulbasaur.SPEED + self.get_level()//2 + Squirtle.SPEED
        return sum/3 + self.get_level() -1
