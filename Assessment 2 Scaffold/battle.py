from typing import Type
from poke_team import PokeTeam
from pokemon_base import PokemonBase


class Battle:

    #task 3.1
    def __init__(self, trainer_one_name: str, trainer_two_name: str)->None :
        self.player1 = PokeTeam(trainer_one_name)
        self.player2 = PokeTeam(trainer_two_name)
        self.battle_mode = None

    
    
    def fight(self, poke1: Type[PokemonBase], poke2: Type[PokemonBase]):
        """2 pokemon fight"""
        #can be optimized by passing no argument
        
        if poke1.get_speed() != poke2.get_speed():
            if poke1.get_speed() > poke2.get_speed():
                attacker = poke1
                defender = poke2
            elif poke1.get_speed() < poke2.get_speed():
                defender = poke1
                attacker = poke2
            attacker.attacked(defender)
            if not defender.is_fainted():
                defender.attacked(attacker)
        else:
            #print('check', poke1, poke2)
            poke1.attacked(poke2)
            #print('check 1', poke1, poke2)
            poke2.attacked(poke1)
            #print('check 2', poke1, poke2)
        
        if not poke1.is_fainted() and not poke2.is_fainted():
            #print('check 4', poke1.get_hp(), poke2.get_hp())
            poke1.set_hp(poke1.get_hp()-1)
            poke2.set_hp(poke2.get_hp()-1)
            #print('check', poke1.get_hp(), poke2.get_hp())
             
        if poke1.is_fainted() and poke2.is_fainted():
            return 
        
        elif poke1.is_fainted():
            poke2.set_level(poke2.get_level() +1)
        elif poke2.is_fainted():
            poke1.set_level(poke1.get_level() +1)

    #task 3.2 
    def set_mode_battle(self)-> str:
        """fight in battle mode 0, basic mode"""
        #choose team
        self.player1.choose_team(0)
        self.player2.choose_team(0)
    
        #batle
        while not (self.player1.team.is_empty() or self.player2.team.is_empty()):
            poke1 = self.player1.team.pop()        
            poke2 = self.player2.team.pop()
            self.fight(poke1, poke2)
            if not poke1.is_fainted():
                self.player1.team.push(poke1)
                #print(poke1.is_fainted(), 'check')
            if not poke2.is_fainted():
                self.player2.team.push(poke2)
                #print(poke2.is_fainted(), 'check')
        return self.result()

    #task 4  
    def rotating_mode_battle(self) -> None:
        """fight in battle mode 1, rotating mode"""
        #choose team
        self.player1.choose_team(1)
        self.player2.choose_team(1)

        #battle
        while not (self.player1.team.is_empty() or self.player2.team.is_empty()):
            poke1 = self.player1.team.serve()
            poke2 = self.player2.team.serve()
            self.fight(poke1, poke2)
            if not poke1.is_fainted():
                #print(poke1.is_fainted(), 1)
                self.player1.team.append(poke1)
            if not poke2.is_fainted():
                #print(poke2.is_fainted(), 2)
                self.player2.team.append(poke2)
        return self.result()
    

    #task 5
    def optimised_mode_battle(self, criterion_team1: str, criterion_team2: str) ->str:
        """fight in battle mode 2, optimised mode"""
        self.player1.choose_team(2, criterion_team1)
        self.player2.choose_team(2, criterion_team2)

        while not (self.player1.team.is_empty() or self.player2.team.is_empty()):
            pass

        return self.result()


    def result(self)-> str:
        """check winner"""
        p1_is_defeated = self.player1.team.is_empty()
        p2_is_defeated = self.player2.team.is_empty()
        #print(p1_is_defeated,p2_is_defeated)
        if p1_is_defeated and p2_is_defeated:
            return "Draw"
        elif p1_is_defeated: #and not team2_is_empty????
            return self.player2.get_trainer_name()
        elif p2_is_defeated:
            return self.player1.get_trainer_name()
    

a = Battle('Han Guang', 'Wing Sze')
a.rotating_mode_battle()
print(a.player1)
print(a.player2)
#2 2 1 # 0 2 1

#b = Battle("Brock", "Gary")
#result = b.rotating_mode_battle()
#2 2 1 #0 2 1 #'Brock' 
