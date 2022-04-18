from typing import Type
from poke_team import PokeTeam
from pokemon_base import PokemonBase

class Battle:

    #task 3.1
    def __init__(self, trainer_one_name: str, trainer_two_name: str)->None :
        self.team1 = PokeTeam(trainer_one_name)
        self.team2 = PokeTeam(trainer_two_name)
        self.battle_mode = None

    #task 3.2
    def set_mode_battle(self)-> None:
        #choose team
        self.team1.choose_team(0)
        self.team2.choose_team(0)
        
        #serve
        team1_poke = self.team1.serve()
        team2_poke = self.team2.serve()

        #batle
        while self.team1.is_empty() or self.team2.is_empty():
            if team1_poke.faint:
                team1_poke = self.team1.serve()
            elif team2_poke.faint:
                team2_poke = self.team2.serve()
            team1_poke.attacked(team2_poke)
        
        print(self.result())

     #task 4   
    def rotating_mode_battle(self) -> None:
        #choose team
        self.team1.choose_team(1)
        self.team2.choose_team(1)

        #battle
        while self.team1.is_empty() or self.team2.is_empty():
            team1_poke = self.team1.serve()
            team2_poke = self.team2.serve()

            team1_poke.attacked(team2_poke)
            if not team1_poke.faint:
                team1_poke = self.team1.append(team1_poke)
            if not team2_poke.faint:
                team2_poke = self.team2.append(team2_poke)
            

        print(self.result())
    
    def fight(poke1: Type[PokemonBase], poke2: Type[PokemonBase]):
        if poke1.speed > poke2.spee:
            poke2.attacked_by(poke1)
        elif poke2.speed >poke1:
            poke1.a
        pass

    #task 5
    def optimised_mode_battle(self, criterion_team1: str, criterion_team2: str) ->str:
        self.team1.choose_team(2, criterion_team1)
        self.team2.choose_team(2, criterion_team2)

        print(self.result())


    def result(self)-> str:
        """check winner"""
        if self.team1.is_empty() and self.team2.is_empty():
            return "Draw"
        elif self.team1.is_empty():
            return self.team2_poke.trainer_name
        elif self.team2.is_empty():
            return self.team1_poke.trainer_name
    


        
