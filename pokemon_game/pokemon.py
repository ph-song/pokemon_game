from pokemon_base import PokemonBase
from typing import Type 
from random import randint
from abc import ABC, abstractclassmethod, abstractmethod


class Charmander(PokemonBase):

    CHAR_ATTACK = 6
    CHAR_DEFENCE = 4
    CHAR_SPEED = 7
    CHAR_HP = 7
    CHAR_POKE_TYPE = "Fire"
    CHAR_NAME = "Charmander"

    def __init__(self)-> None:
        PokemonBase.__init__(self, self.CHAR_HP, self.CHAR_POKE_TYPE)
        self.name = self.CHAR_NAME 

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
        return self.CHAR_ATTACK + self.get_level()
    
    def get_defence(self):
        """pokemon defence getter"""
        return self.CHAR_DEFENCE
    
    def get_speed(self):
        """return pokemon speed"""
        return self.CHAR_SPEED + self.get_level()


class Bulbasaur(PokemonBase):

    BULB_ATTACK = 5
    BULB_DEFENCE = 5
    BULB_SPEED = 7
    BULB_HP = 9
    BULB_POKE_TYPE = "Grass"
    BULB_NAME = "Bulbasaur"

    def __init__(self)-> None:
        PokemonBase.__init__(self, self.BULB_HP, self.BULB_POKE_TYPE)
        self.name = self.BULB_NAME

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
        return self.BULB_ATTACK
    
    def get_defence(self):
        """pokemon defence getter"""
        return self.BULB_DEFENCE
    
    def get_speed(self):
        """return pokemon speed"""
        return self.BULB_SPEED + self.get_level()//2

class Squirtle(PokemonBase):

    SQUIR_ATTACK = 4
    SQUIR_DEFENCE = 6
    SQUIR_SPEED = 7
    SQUIR_HP = 8
    SQUIR_POKE_TYPE = "Water"
    SQUIR_NAME = "Squirtle"

    def __init__(self)-> None:
        PokemonBase.__init__(self, self.SQUIR_HP, self.SQUIR_POKE_TYPE)
        self.name = self.SQUIR_NAME

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
        return self.SQUIR_ATTACK + self.get_level()//2
    
    def get_defence(self):
        """pokemon defence getter"""
        return self.SQUIR_DEFENCE + self.get_level()
    
    def get_speed(self):
        """return pokemon speed"""
        return self.SQUIR_SPEED


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
    HP = (7+9+8)/3
    MYST_NAME = "MissingNo"

    def __init__(self)-> None:
        GlitchMon.__init__(self, self.HP, self.MYST_NAME)
        self.name = self.MYST_NAME

    def get_attack(self):
        """return pokemon attack"""
        sum = 6 + self.get_level() + 5 + 4 + self.get_level()//2
        return sum/3 + self.get_level() -1
    
    def get_defence(self):
        """pokemon defence getter"""
        sum = 4 + 5 + 6 + self.get_level()
        return sum/3 + self.get_level() -1
    
    def get_speed(self) -> int:
        """return pokemon speed"""
        sum = 7 + self.get_level() + 7 + self.get_level()//2 + 7
        return sum/3 + self.get_level() -1



'''
class GlitchMon(Charmander, Squirtle, Bulbasaur): #is ABC nessesary
    POKE_TYPE = None

    def __init__(self)-> None:
        PokemonBase.__init__(self, self.HP, self.POKE_TYPE) #downcasting?
        self.name = self.MYST_NAME

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
    HP = (Charmander.CHAR_HP + Bulbasaur.BULB_HP + Squirtle.SQUIR_HP)/3
    MYST_NAME = "MissingNo"

    def __init__(self)-> None:
        GlitchMon.__init__(self)
        self.name = self.MYST_NAME

    def get_attack(self):
        """return pokemon attack"""
        sum = Charmander.get_attack(self) +Squirtle.get_attack(self) + Bulbasaur.get_attack(self)
        return sum/3 + self.get_level() -1
    
    def get_defence(self):
        """pokemon defence getter"""
        sum = Charmander.get_defence(self) +Squirtle.get_defence(self) + Bulbasaur.get_defence(self)
        return sum/3 + self.get_level() -1
    
    def get_speed(self) -> int:
        """return pokemon speed"""
        sum = Charmander.get_speed(self) +Squirtle.get_speed(self) + Bulbasaur.get_speed(self)
        return sum/3 + self.get_level() -1

    def get_hp(self) -> int:
        return self.hp
'''    


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