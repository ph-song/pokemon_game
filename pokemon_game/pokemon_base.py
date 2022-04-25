from abc import ABC, abstractmethod

from typing import Type

class PokemonBase(ABC):
    INITIAL_LEVEL = 1
    TYPE_EFFECTIVENESS = {
        'Fire': {'Fire': 1, 'Water': 0.5, 'Grass': 2}, 
        'Water': {'Fire': 2, 'Water': 1, 'Grass': 0.5}, 
        'Grass': {'Fire': 0.5, 'Water': 2, 'Grass': 1},
        None: {'Fire': 1, 'Water': 1, 'Grass': 1}
        }

    def __init__(self, hp: int, poke_type: str) -> None:
        """ Initialiser method of PokemonBase class.

        :pre: hp >= 0
        :complexity: O(1), numerical comparison, 
                     raising exception and assignments have constant cost,
                     best case = worst case as no element properties can change this
        """
        # Check validity of pre-condition
        if hp < 0:
            raise ValueError("HP can't be negative")
    
        self.poke_type = poke_type
        self.hp = hp
        self.level = self.INITIAL_LEVEL
        
    def __str__(self) ->str:
        """ Attribute poke_type getter.

        :complexity: O(1), return statements have constant cost,
                     Best case = Worst case because no element properties can change this
        """
        return f"{self.get_name()}'s HP = {self.get_hp()} and level = {self.get_level()}"

    def get_type(self) ->str:
        """ Attribute poke_type getter.

        :complexity: O(1), return statements have constant cost,
                     Best case = Worst case because no element properties can change this
        """
        return self.poke_type

    def get_name(self) ->str:
        """Attribute name getter.

        :complexity: O(1), return statements have constant cost,
                     Best case = Worst case because no element properties can change this
        """
        return self.name

    def set_hp(self, hp: int) -> None:
        """ Attribute hp setter.

        :complexity: O(1), numerical comparison, raising exception and assignments have constant cost,
                     Best case = Worst case because no element properties can change this
        """
        self.hp = hp

    def get_hp(self) ->int:
        """ Attribute hp getter.

        :complexity: O(1), return statements have constant cost
                     Best case = Worst case because no element properties can change this
        """
        return self.hp

    def set_level(self, level) -> None:
        """ Attribute level setter.

        :pre: level >= 1
        :complexity: O(1), numerical comparison, raising exception and assignments have constant cost,
                     Best case = Worst case because no element properties can change this
        """
        if level < 1:
            raise ValueError("Level must be greater than zero")
        self.level = level

    def get_level(self) ->int:
        """ Attribute level getter.

        :complexity: O(1), return statements have constant cost
                     Best case = Worst case because no element properties can change this
        """
        return self.level

    @abstractmethod
    def get_attack(self) ->int:
        """return pokemon attack"""
        pass
    
    @abstractmethod
    def get_defence(self) ->int:
        """return pokemon defence"""
        pass
    
    @abstractmethod
    def get_speed(self) ->int:
        """return pokemon speed"""
        pass

    def is_fainted(self) ->bool:
        """ Check if pokemon is fainted.

        :complexity: O(1), numerical comparison, return statements have constant cost
                     Best case = Worst case because no element properties can change this
        """
        return self.hp<=0

    @abstractmethod
    def attacked_by(self, attacker: "PokemonBase") -> None:
        """ Pokemon initiates attack.

        :param arg1: the attacker
        """
        pass

    def damage_multiplier(self, defender: 'PokemonBase') -> float:
        """ Returns multiplier of attack based on pokemon type of attacker and defender.

        :param arg1: the defender
        :complexity: O(1), accessing element in a dictionary has constant cost
                     Best case = Worst case because no element properties can change this
        """
        return self.TYPE_EFFECTIVENESS[self.get_type()][defender.get_type()]


