from typing import Type
from poke_team import PokeTeam
from pokemon_base import PokemonBase


class Battle:

    #task 3.1
    def __init__(self, trainer_one_name: str, trainer_two_name: str)->None :
        self.team1 = PokeTeam(trainer_one_name)
        self.team2 = PokeTeam(trainer_two_name)
        self.battle_mode = None
    
    def fight(self, poke1: Type[PokemonBase], poke2: Type[PokemonBase]):
        """2 pokemon fight"""
        #can be optimized by passing no argument 
        if poke1.speed > poke2.speed:
            poke1.attacked(poke2)
        elif poke2.speed > poke1.speed:
            poke2.attacked(poke1)
        elif poke1.speed == poke2.speed:
            poke1.attacked(poke2)
            poke2.attacked(poke1)
            #what if both faint? level up issue 

    #task 3.2 
    def set_mode_battle(self)-> None:
        """fight in battle mode 0, basic mode"""
        #choose team
        self.team1.choose_team(0)
        self.team2.choose_team(0)
        
        #serve
        team1_poke = self.team1.team.serve()
        team2_poke = self.team2.team.serve()

        #batle
        while not (self.team1.is_defeated() or self.team2.is_defeated()):
            if team1_poke.is_faint:
                self.team1.team.append(team1_poke)
                team1_poke = self.team1.team.serve()
            if team2_poke.is_faint: #both can fiant at the same time when speed are same
                self.team2.team.append(team2_poke)
                team2_poke = self.team2.team.serve()
            while not (team1_poke.is_faint or team2_poke.is_faint):
                self.fight(team1_poke, team2_poke)
 
        print(self.result())

    #task 4  
    def rotating_mode_battle(self) -> None:
        """fight in battle mode 1, rotating mode"""
        #choose team
        self.team1.choose_team(1)
        self.team2.choose_team(1)

        #battle
        while self.team1.is_defeated() or self.team2.team.is_defeated():
            team1_poke = self.team1.team.serve()
            team2_poke = self.team2.team.serve()

            team2_poke.attacked(team1_poke)
            if not team1_poke.is_faint:
                team1_poke = self.team1.append(team1_poke)
            if not team2_poke.is_faint:
                team2_poke = self.team2.append(team2_poke)
            

        print(self.result())
    

    #task 5
    def optimised_mode_battle(self, criterion_team1: str, criterion_team2: str) ->str:
        """fight in battle mode 2, optimised mode"""
        self.team1.choose_team(2, criterion_team1)
        self.team2.choose_team(2, criterion_team2)

        print(self.result())


    def result(self)-> str:
        """check winner"""
        if self.team1.is_defeated() and self.team2.is_defeated():
            return "Draw"
        elif self.team1.is_defeated():
            return self.team2.trainer_name
        elif self.team2.is_defeated():
            return self.team1.trainer_name
    

a = Battle('Ali', 'Ah Khaw')
a.set_mode_battle()
print(a.team1)
print(a.team2)

#b = Battle('Han Guang', 'Wing Sze')
#b.rotating_mode_battle

        
