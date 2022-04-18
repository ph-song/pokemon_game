from abc import ABC, abstractmethod

from typing import Type

class PokemonBase(ABC):
    INITIAL_LEVEL = 1

    def __init__(self, poke_type: str, hp: int, name: str) -> None:
        self.poke_type = poke_type
        self.hp = hp
        self.level = self.INITIAL_LEVEL
        self.name = name
        self.is_faint = False
        #is it okay to initialize it to None

    @abstractmethod
    def __str__(self)->str:
        pass

    def get_type(self):
        """return pokemon type"""
        return self.poke_type

    def set_hp(self, hp: int) -> None:
        """set pokemon hp"""
        self.hp = hp

    def get_hp(self) ->int:
        """return pokemon hp"""
        return self.hp

    def set_level(self, level) -> None:
        """
        set pokemon level
        precondition: level >= 1
        """
        self.level = level

    def get_level(self) ->int:
        """return pokemon level"""
        return self.level

    def check_faint(self, defencer: 'PokemonBase'):
        """if hp <= 0 pokemon faint = True, else faint = False"""
        if defencer.hp <= 0:
            defencer.is_faint = True
            self.level += 1
        else:
            defencer.is_faint = False

    def attacked(self, defencer: "PokemonBase") -> None:
        attacker_attack = self.attack
        attack_multiplier = self.damage_multiplier(self.poke_type, defencer.poke_type)
        attacker_attack *= attack_multiplier

        if self.attack > defencer.defence:
            defencer.hp -= attacker_attack
        else:
            defencer.hp -= attacker_attack//2
        self.check_faint(defencer)

    def damage_multiplier(self, defencer_type: str, attacker_type: str) -> float:
        """reutrn multiplier of attack based on pokemon type of attacker and defencer"""
        effectiveness = {
            'Fire': {'Fire': 1, 'Water': 0.5, 'Grass': 2}, 
            'Water': {'Fire': 2, 'Water': 1, 'Grass': 0.5}, 
            'Grass': {'Fire': 0.5, 'Water': 2, 'Grass': 1}
            }

        return effectiveness[defencer_type][attacker_type]
