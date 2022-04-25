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
        """ constructor of PokemonBase

        :pre: hp >= 0
        :complexity: O(1), worst case = best case
        """
        # Check validity of hp
        if hp < 0:
            raise ValueError("HP can't be negative")
    
        self.poke_type = poke_type
        self.hp = hp
        self.level = self.INITIAL_LEVEL
        
    def __str__(self) ->str:
        """ PokemonBase constructor

        :complexity: O(1), worst case = best case
        """
        return f"{self.get_name()}'s HP = {self.get_hp()} and level = {self.get_level()}"

    def get_type(self) ->str:
        """ return pokemon poke_type

        :complexity: O(1), worst case = best case
        """
        return self.poke_type

    def get_name(self) ->str:
        """return pokemon's name

        :complexity: O(1), worst case = best case
        """
        return self.name

    def set_hp(self, hp: int) -> None:
        """set pokemon's hp

        :complexity: O(1), worst case = best case
        """
        self.hp = hp

    def get_hp(self) ->int:
        """ return pokemon's hp

        :complexity: O(1), worst case = best case
        """
        return self.hp

    def set_level(self, level) -> None:
        """set level

        :raises ValueError: if level <= 0
        :complexity: O(1), worst case = best case
        """
        if level < 1:
            raise ValueError("level must be positive value")
        self.level = level

    def get_level(self) ->int:
        """return pokemon level

        :complexity: O(1), worst case = best case
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
        """return True is pokemon hp <= 0 else False

        :complexity: O(1), worst case = best case
        """
        return self.hp<=0

    @abstractmethod
    def attacked_by(self, attacker: "PokemonBase") -> None:
        """ pokemon attacked by another pokemon

        :param arg1: the attacker
        """
        pass

    def damage_multiplier(self, defender: 'PokemonBase') -> float:
        """ Returns multiplier of attack based on pokemon type of attacker and defender.

        :param arg1: the defender
        :complexity: O(1), worst case = best case
        """
        return self.TYPE_EFFECTIVENESS[self.get_type()][defender.get_type()]



