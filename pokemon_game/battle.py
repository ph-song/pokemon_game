""" 
Filename: battle.py
Class: Battle
"""

__author__ = "FIT1008 T03G06"

from typing import Type
from poke_team import PokeTeam
from pokemon_base import PokemonBase
from array_sorted_list import ArraySortedList
from sorted_list import ListItem
from pokemon import MissingNo


class Battle:

    def __init__(self, trainer_one_name: str, trainer_two_name: str) -> None:
        """Battle constructor

        :complexity: O(1), worst case = best case
        """
        self.team1 = PokeTeam(trainer_one_name)
        self.team2 = PokeTeam(trainer_two_name)
        self.battle_mode = None 

    def fight(self, poke1: Type[PokemonBase], poke2: Type[PokemonBase]) -> None:
        """2 pokemon fight with each other
        
        :complexity: O(1), worst case = best case
        """
        #pokemon with higher speed initialize attack
        if poke1.get_speed() != poke2.get_speed():
            if poke1.get_speed() > poke2.get_speed():
                attacker = poke1
                defender = poke2
            elif poke1.get_speed() < poke2.get_speed():
                defender = poke1
                attacker = poke2
            defender.attacked_by(attacker)

            #defender retort if not fainted
            if not defender.is_fainted():
                attacker.attacked_by(defender)
        
        #poke1 and poke2 attack each other if both have equal speed
        else:
            poke1.attacked_by(poke2)
            poke2.attacked_by(poke1)
        
        #lose one hp if both are still not fainted
        if not poke1.is_fainted() and not poke2.is_fainted():
            poke1.set_hp(poke1.get_hp() - 1)
            poke2.set_hp(poke2.get_hp() - 1)

        #return if both fainted
        if poke1.is_fainted() and poke2.is_fainted():
            return

        #not fainted pokemon level up if another pokemon fainted
        elif poke1.is_fainted():
            poke2.set_level(poke2.get_level() + 1)
        elif poke2.is_fainted():
            poke1.set_level(poke1.get_level() + 1)

    #task 3
    def set_mode_battle(self) -> str:
        """battle in basic mode
        
        :pre: both team array are not empty
        :post: one of the team array is empty
        :complexity: O(n),worst case = best case
                     where n = battle round
        """
        #choose team
        self.team1.choose_team(0)
        self.team2.choose_team(0)
    
        #batle
        while not (self.team1.team.is_empty() or self.team2.team.is_empty()):
            #pop pokemon from stack
            poke1 = self.team1.team.pop()        
            poke2 = self.team2.team.pop()

            self.fight(poke1, poke2) # two pokemons fight
            
            #push not fainted pokemon back to stack
            if not poke1.is_fainted(): 
                self.team1.team.push(poke1)
            if not poke2.is_fainted():
                self.team2.team.push(poke2)
        
        return self.result() #return result

    #task 4 
    def rotating_mode_battle(self) -> str:
        """battle in rotating mode
        
        :pre: both team array are not empty
        :post: one of the team array is empty
        :complexity: O(n),worst case = best case
                     where n = battle round
        """
        #choose team
        self.team1.choose_team(1)
        self.team2.choose_team(1)

        #battle
        while not (self.team1.team.is_empty() or self.team2.team.is_empty()):
            #serve pokemon from queue
            poke1 = self.team1.team.serve()
            poke2 = self.team2.team.serve()

            self.fight(poke1, poke2) #pokemon fight with each other

            #append not fainted pokemon back to queue
            if not poke1.is_fainted():
                self.team1.team.append(poke1)
            if not poke2.is_fainted():
                self.team2.team.append(poke2)

        return self.result() #return result
    
    #task 5
    def optimised_mode_battle(self, criterion_team1: str, criterion_team2: str) -> str:
        """battle in optimised mode

        :pre: both team array is not empty
        :post: one of the team array is empty
        :complexity:
        """
        self.team1.choose_team(2, criterion_team1)
        self.team2.choose_team(2, criterion_team2)

        #battle
        while not (self.team1.team.is_empty() or self.team2.team.is_empty()):
            
            #remove last pokemon in team
            poke1 = (self.team1.team.delete_at_index(len(self.team1.team) - 1)).value
            poke2 = (self.team2.team.delete_at_index(len(self.team2.team) - 1)).value
            
            #check MissingNo
            #if hte pokemon is MissingNo and not all pokemon have fought at least once
            if type(poke1) is MissingNo and not all([i.has_battle() for i in self.team1.team]):
                #summon another pokemon and add MissingNo back to team
                temp = poke1
                poke1 = (self.team1.team.delete_at_index(len(self.team1.team) - 1)).value
                key = self.team1.get_crit_val(temp)
                self.team1.team.add(ListItem(temp, key))
            if type(poke2) is MissingNo and not all([i.has_battle() for i in self.team2.team]):
                temp = poke2
                poke2 = (self.team2.team.delete_at_index(len(self.team2.team) - 1)).value
                key = self.team2.get_crit_val(temp)
                self.team1.team.add(ListItem(temp, key))
           
            self.fight(poke1, poke2) #pokemon fight with each other

            #add not fainted pokemon back to sorted list
            if not poke1.is_fainted():
                key = self.team1.get_crit_val(poke1)
                self.team1.team.add(ListItem(poke1, key))
            if not poke2.is_fainted():
                key = self.team2.get_crit_val(poke2)
                self.team2.team.add(ListItem(poke2, key)) 

        return self.result() #return result

    def result(self) -> str:
        """return trainer_name of won team
        
        :complexity: O(1), worst case = best case
        """
        #check if the team is defeated
        p1_is_defeated = self.team1.team.is_empty()
        p2_is_defeated = self.team2.team.is_empty()

        #return result
        if p1_is_defeated and p2_is_defeated:
            return "Draw"
        elif p1_is_defeated:
            return self.team2.get_trainer_name()
        elif p2_is_defeated:
            return self.team1.get_trainer_name()
