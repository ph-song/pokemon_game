""" 
Filename: pokemon_base.py
Class: PokemonBase
"""

__author__ = "FIT1008 T03G06"

from abc import ABC, abstractmethod
from typing import Type, Union

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
        # Check hp validity
        if hp < 0:
            raise ValueError("HP can't be negative")
    
        self.poke_type = poke_type
        self.hp = hp
        self.level = PokemonBase.INITIAL_LEVEL
        
    def __str__(self) -> str:
        """ PokemonBase string method

        :complexity: O(1), worst case = best case
        """
        return f"{self.get_name()}'s HP = {int(self.get_hp())} and level = {self.get_level()}"

    def get_type(self) -> str:
        """ return pokemon poke_type

        :complexity: O(1), worst case = best case
        """
        return self.poke_type

    def get_name(self) -> str:
        """return pokemon name

        :complexity: O(1), worst case = best case
        """
        return self.name

    def set_hp(self, hp: Union[int, float]) -> None:
        """set pokemon hp

        :complexity: O(1), worst case = best case
        """
        self.hp = hp

    def get_hp(self) -> Union[int, float]:
        """ return pokemon hp

        :complexity: O(1), worst case = best case
        """
        return self.hp

    def set_level(self, level) -> None:
        """set pokemon level

        :raises ValueError: if level <= 0
        :complexity: O(1), worst case = best case
        """
        if level < 1:
            raise ValueError("level must be positive value")
        self.level = level

    def get_level(self) -> int:
        """return pokemon level

        :complexity: O(1), worst case = best case
        """
        return self.level

    @abstractmethod
    def get_attack(self) -> int:
        """return pokemon attack"""
        pass
    
    @abstractmethod
    def get_defence(self) -> int:
        """return pokemon defence"""
        pass
    
    @abstractmethod
    def get_speed(self) -> int:
        """return pokemon speed"""
        pass

    def is_fainted(self) -> bool:
        """return True is pokemon hp <= 0 else False

        :complexity: O(1), worst case = best case
        """
        return self.hp <= 0

    @abstractmethod
    def attacked_by(self, attacker: "PokemonBase") -> None:
        """ pokemon attacked by another pokemon

        :param arg1: the attacker
        """
        pass

    @abstractmethod
    def has_fought(self) -> bool:
        """return ture if pokemon has battled at least one round else false"""
        pass

    def damage_multiplier(self, defender: "PokemonBase") -> Union[int, float]:
        """returns multiplier of attack based on pokemon type of attacker and defender

        :param arg1: the defender
        :complexity: O(1), worst case = best case
        """
        return PokemonBase.TYPE_EFFECTIVENESS[self.get_type()][defender.get_type()]


