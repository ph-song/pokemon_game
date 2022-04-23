from pokemon import Charmander, Bulbasaur, MissingNo, Squirtle
from queue_adt import CircularQueue
from array_sorted_list import ArraySortedList
from sorted_list import ListItem
from stack_adt import ArrayStack
from pokemon_base import PokemonBase
from typing import Type

class PokeTeam: 
    POKEMON_LIMIT = 6
    INITIAL_BATTLE_MODE = 0

    def __init__(self, trainer_name: str) -> None:
        self.battle_mode = self.INITIAL_BATTLE_MODE
        self.trainer_name = trainer_name
        self.team = None 
        self.criterion = None
        self.myst = False
     
    def __str__(self):
        return str(self.team)

    def get_trainer_name(self):
        """trainer_name getter"""
        return self.trainer_name

    def get_battle_mode(self):
        """battle_mode getter"""
        return self.battle_mode
    
    def set_battle_mode(self, battle_mode: int):
        if battle_mode not in range(3):
            raise Exception("unavailable battle mode")
        self.battle_mode = battle_mode
    
    def set_criterion(self, criterion: str):
        """criterion setter"""
        #####need to check validity of criterion
        self.criterion = criterion
    
    def get_criterion(self):
        """criterion getter"""
        return self.criterion
    
    def get_criterion_val(self, poke: Type[PokemonBase]):
        criterion_table = {
            'hp': poke.get_hp(),
            'level': poke.get_level(),
            'attack': poke.get_attack(),
            'defence': poke.get_defence(),
            'speed': poke.get_speed()
        }
        criterion = (self.get_criterion()).lower()
        return criterion_table[criterion]
    
    def choose_team(self, battle_mode: int, criterion: str = None) -> None:
        """choose number of pokemons and form a team"""
        
        self.set_battle_mode(battle_mode) #set battle mode
        self.set_criterion(criterion)

        #ask input from user 
        prompt = "Howdy Trainer! Choose your team as C B S M\nwhere \tC is the number of Charmanders \n\tB is the number of Bulbasaurs \n\tS is the number of Squirtles\n\tM is the number of Mystery Pokemon\n>"
        valid_input = False
        while not valid_input:
            try:
                user_input = input(prompt)
                charm, bulb, squir = int(user_input[0]), int(user_input[2]), int(user_input[4])
                
                myst = 0
                if len(user_input) >=6:
                    myst = int(user_input[6])

                self.assign_team(charm, bulb, squir, myst) #popoulate team
            except Exception:
                print("invalid input")
            else:
                valid_input = True

    def assign_team(self, charm: int, bulb: int, squir: int, myst: int = 0) -> None:
        """populate team"""
        pokemon_num = charm + bulb + squir + myst
        if pokemon_num > self.POKEMON_LIMIT or myst > 1:
            raise Exception("invalid pokemon number")
        
        #when battle_mode == 0 
        if self.get_battle_mode() == 0:
            self.populate_stack(charm, bulb, squir, myst)

        #when battle_mode == 1
        elif self.get_battle_mode() == 1:
            self.populate_queue(charm, bulb, squir, myst)

        #when battle_mode == 2
        elif self.get_battle_mode() == 2:
            self.populate_sorted_list(charm, bulb, squir, myst)
    
    def populate_stack(self, charm: int, bulb: int, squir: int, myst: int = 0):
        self.team = ArrayStack(self.POKEMON_LIMIT)
        if bool(myst):
            self.team.push(MissingNo())
        for i in range(squir):
            self.team.push(Squirtle())
        for i in range(bulb):
            self.team.push(Bulbasaur())
        for i in range(charm):
            self.team.push(Charmander())
        
    
    def populate_queue(self, charm: int, bulb: int, squir: int, myst: int = 0):
        self.team = CircularQueue(self.POKEMON_LIMIT)
        for i in range(charm):
            self.team.append(Charmander())
        for i in range(bulb):
            self.team.append(Bulbasaur())
        for i in range(squir):
            self.team.append(Squirtle())
        if bool(myst):
            self.team.append(MissingNo())

    def populate_sorted_list(self, charm: int, bulb: int, squir: int, myst: int = 0):
        self.team = ArraySortedList(self.POKEMON_LIMIT)
        for i in range(squir):
            value = Squirtle()
            key = self.get_criterion_val(value)
            self.team.add(ListItem(value, -key))
        for i in range(bulb):
            value = Bulbasaur()
            key = self.get_criterion_val(value)
            self.team.add(ListItem(value, -key))
        for i in range(charm):
            value = Charmander()
            key = self.get_criterion_val(value)
            self.team.add(ListItem(value, -key))
        if bool(myst):
            value = MissingNo()
            key = float('inf')
            self.team.add(ListItem(value, -key))

"""
a = PokeTeam("haha")
a.choose_team(0, None)
#a.populate_stack(1,1,1,1)
print(a)


a = PokeTeam('raidi1')
a.choose_team(0,None)
print(a)


a = PokeTeam('raidi1')
a.set_criterion('hp')
a.populate_sorted_list(2,2,1)
print(a)
# B B S C C

b = PokeTeam('raidi2') 
b.set_criterion('level')
b.populate_sorted_list(0,2,1)
print(b)
#S B B

a = PokeTeam('asd')
a.populate_stack(1,0,0)
a.team.push(Squirtle())
print(a)
a.team.pop()
print(a)
"""