from abc import ABC, abstractmethod

from typing import Type

class PokemonBase(ABC):
    INITIAL_LEVEL = 1
    TYPE_EFFECTIVENESS = {
        'Fire': {'Fire': 1, 'Water': 0.5, 'Grass': 2}, 
        'Water': {'Fire': 2, 'Water': 1, 'Grass': 0.5}, 
        'Grass': {'Fire': 0.5, 'Water': 2, 'Grass': 1}
        }

    def __init__(self, hp: int, poke_type: str) -> None:
        self.poke_type = poke_type
        self.hp = hp
        self.level = self.INITIAL_LEVEL
        
    def __str__(self)->str:
        """string method of PokemonBase"""
        return f"{self.get_name()}'s HP = {self.get_hp()} and level = {self.get_level()}"

    def get_type(self):
        """pokemon type getter"""
        return self.poke_type

    def get_name(self):
        """pokemon name getter"""
        return self.name

    def set_hp(self, hp: int) -> None:
        """pokemon hp setter"""
        self.hp = hp

    def get_hp(self) ->int:
        """pokemon hp getter"""
        return self.hp

    def set_level(self, level) -> None:
        """
        pokemon level setter
        :precondition: level >= 1
        """
        self.level = level

    def get_level(self) ->int:
        """return pokemon level"""
        return self.level

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

    def is_fainted(self):
        """check if pokemon is fainted"""
        return self.hp<=0

    @abstractmethod
    def attacked_by(self, attacker: "PokemonBase") -> None:
        """
        pokemon initiate attack, argument is defenser
        hp of attacker and defenser both must be positive
        """
        pass

    def damage_multiplier(self, defender: 'PokemonBase') -> float:
        """reutrn multiplier of attack based on pokemon type of attacker and defender"""
        return self.TYPE_EFFECTIVENESS[self.get_type()][defender.get_type()]
