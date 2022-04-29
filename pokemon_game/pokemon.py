""" 
Filename: pokemon.py
Classes: Charmander, Bulbasaur, Squirtle, GlitchMon, MissingNo
"""

__author__ = "FIT1008 T03G06"

from pokemon_base import PokemonBase
from typing import Type 
from random import randint

class Charmander(PokemonBase):

    #Charmander attribute base value
    ATTACK = 6
    DEFENCE = 4
    SPEED = 7
    HP = 7
    POKE_TYPE = "Fire"
    NAME = "Charmander"

    def __init__(self) -> None:
        """ Charmander constructor

        :complexity: O(1), worst case = best case
        """
        PokemonBase.__init__(self, Charmander.HP, Charmander.POKE_TYPE)  #Calling the parent class PokemonBase constructor
        self.name = Charmander.NAME

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
    
    def get_attack(self) -> int:
        """ return Charmander attack

        :complexity: O(1), worst case = best case
        """
        return Charmander.ATTACK + self.get_level()
    
    def get_defence(self) -> int:
        """ return Charmander defence

        :complexity: O(1), worst case = best case
        """
        return Charmander.DEFENCE
    
    def get_speed(self) -> int:
        """ return Charmander speed

        :complexity: O(1), worst case = best case
        """
        return Charmander.SPEED + self.get_level()
    
    def has_fought(self) -> bool:
        """return ture if the Charmander has battled at least one round else false"""
        return self.get_hp() != Charmander.HP or self.get_level != 1


class Bulbasaur(PokemonBase):

    #Balbasaur attributes base value
    ATTACK = 5
    DEFENCE = 5
    SPEED = 7
    HP = 9
    POKE_TYPE = "Grass"
    NAME = "Bulbasaur"

    def __init__(self) -> None:
        """Bulbasaur constuctor 

        :complexity: O(1), best case = worst case
        """
        PokemonBase.__init__(self, Bulbasaur.HP, Bulbasaur.POKE_TYPE) #PokemonBase constructor
        self.name = Bulbasaur.NAME

    def attacked_by(self, attacker: Type[PokemonBase]) -> None:
        """ Bulbasaur attacked by pokemon and lose hp

        :param arg1: the attacker
        :complexity: O(1), worse case = best case
        """
        attacker_damage = attacker.get_attack() * attacker.damage_multiplier(self) #effective damage

        #actual damage caused
        if attacker_damage > self.get_defence() + 5 :
            self.set_hp(self.get_hp() - attacker_damage)
        else:
            self.set_hp(self.get_hp() - attacker_damage//2)
        
    def get_attack(self) -> int:
        """return Bulbasaur attack
        
        :complexity: O(1), best case = worst case
        """
        return Bulbasaur.ATTACK
    
    def get_defence(self) -> int:
        """return Bulbasaur defence
        
        :complexity: O(1), best case = worst case
        """
        return Bulbasaur.DEFENCE
    
    def get_speed(self) -> int:
        """return Bulbasaur speed
        
        :complexity: O(1), best case = worst case
        """
        return Bulbasaur.SPEED + self.get_level()//2

    def has_fought(self) -> bool:
        """return ture if the Bulbasaur has battled at least one round else false"""
        return self.get_hp() != Bulbasaur.HP or self.get_level != 1

class Squirtle(PokemonBase):

    #Squirtle attributes base value
    ATTACK = 4
    DEFENCE = 6
    SPEED = 7
    HP = 8
    POKE_TYPE = "Water"
    NAME = "Squirtle"

    def __init__(self) -> None:
        """ Squirtle constuctor

        :complexity: O(1), best case = worst case
        """
        PokemonBase.__init__(self, Squirtle.HP, Squirtle.POKE_TYPE) #calling the parent class PokemonBase constructor
        self.name = Squirtle.NAME

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

    def get_attack(self) -> int:
        """return Squirtle attack
        
        :complexity: O(1), best case = worst case
        """
        return Squirtle.ATTACK + self.get_level()//2
    
    def get_defence(self) -> int:
        """return Squirtle defence

        :complexity: O(1), best case = worst case
        """
        return Squirtle.DEFENCE + self.get_level()
    
    def get_speed(self) -> int:
        """return Squirtle speed

        :complexity: O(1), best case = worst case
        """
        return Squirtle.SPEED

    def has_fought(self) -> bool:
        """return ture if the Squirtle has battled at least one round else false"""
        return self.get_hp() != Squirtle.HP or self.get_level != 1


class GlitchMon(PokemonBase):
    POKE_TYPE = None

    def __init__(self, hp: int, name: str) -> None:
        """ GlitchMon constructor 

        :complexity: O(1), worst case = best case
        """
        PokemonBase.__init__(self, hp, GlitchMon.POKE_TYPE) #calling the parent class PokemonBase constructor
        self.name = name

    def attacked_by(self, attacker: Type[PokemonBase]) -> None:
        """GlitchMon attacked by pokemon and lose hp  

        :param arg1: the attacker
        :complexity: O(1), best case = worst case
        """
        if randint(1, 4) == 1: #1 out of 4 gives 25% probability
            self.super_power()
        self.set_hp(self.get_hp() - attacker.get_attack())

    def super_power(self) ->None:
        """GlitchMon superpower, increases GlitchMon hp or level or both by one

        :complexity: O(1), worst case = best case
        """
        i = randint(0, 2)
        if i == 0:
            self.set_hp(self.get_hp() + 1)
        elif i == 1:
            self.set_level(self.get_level() + 1)
        elif i == 2:
            self.set_hp(self.get_hp() + 1)
            self.set_level(self.get_level() + 1)


class MissingNo(GlitchMon):
    HP = (Charmander.HP + Bulbasaur.HP + Squirtle.HP)/3
    NAME = "MissingNo"

    def __init__(self) -> None:
        """MissingNo constuctor   

        :complexity: O(1), best case = worst case
        """
        # calling parent class GlitchMon constructor
        GlitchMon.__init__(self, MissingNo.HP, MissingNo.NAME)

    def get_attack(self) -> int:
        """return MissingNo attack
        
        :complexity: O(1), worst case = best case
        """
        sum = Charmander.ATTACK + self.get_level() + Bulbasaur.ATTACK + Squirtle.ATTACK + self.get_level()//2
        return sum/3 + self.get_level() - 1
    
    def get_defence(self) -> int:
        """return MissingNo defence
        
        :complexity: O(1), worst case = best case
        """
        sum = Charmander.DEFENCE + Bulbasaur.DEFENCE + Squirtle.DEFENCE + self.get_level()
        return sum/3 + self.get_level() - 1
    
    def get_speed(self) -> int:
        """return MissingNo speed
        
        :complexity: O(1), worst case = best case
        """
        sum = Charmander.SPEED + self.get_level() + Bulbasaur.SPEED + self.get_level()//2 + Squirtle.SPEED
        return sum/3 + self.get_level() - 1

    def has_fought(self) -> bool:
        """return ture if the MissingNo has battled at least one round else false
        
        :complexity: O(1)
        """
        return self.get_hp() != MissingNo.HP or self.get_level != 1