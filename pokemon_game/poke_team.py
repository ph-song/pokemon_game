""" 
Filename: poke_team.py
Class: PokeTeam
"""

__author__ = "FIT1008 T03G06"


from pokemon import Charmander, Bulbasaur, MissingNo, Squirtle
from queue_adt import CircularQueue
from array_sorted_list import ArraySortedList
from sorted_list import ListItem
from stack_adt import ArrayStack
from pokemon_base import PokemonBase
from typing import Type, Union


class PokeTeam: 
    POKEMON_LIMIT = 6
    INITIAL_BATTLE_MODE = 0

    def __init__(self, trainer_name: str) -> None:
        """ PokeTeam constructor

        :complexity: O(1), worst case = best case
        """
        self.battle_mode = PokeTeam.INITIAL_BATTLE_MODE
        self.trainer_name = trainer_name
        self.team = None 
        self.criterion = None
  
    def __str__(self) -> str:
        """ PokeTeam string method

        :complexity: O(n), where n = number of elements in team
                     worst case = best case
        """
        return str(self.team)

    def get_trainer_name(self) -> str:
        """return team's trainer_name

        :complexity: O(1), best worst case = best case
        """
        return self.trainer_name

    def get_battle_mode(self) -> int:
        """return team's battle_mode

        :complexity: O(1), worst case = best case
        """
        return self.battle_mode
    
    def set_battle_mode(self, battle_mode: int) -> None:
        """set team battle_mode

        :raise ValueError: if battle_mode not in range(3)
        :complexity: O(1), worst case = best case
        """
        # checks validity of battle_mode
        if battle_mode not in range(3):
            raise ValueError("unavailable battle mode")

        self.battle_mode = battle_mode
    
    def set_criterion(self, criterion: str) -> None:
        """set team criterion

        :raise ValueError: if criterion is invalid
        :complexity: O(1), worst case = best case
        """
        #check validity of criterion 
        if criterion not in [None, 'hp', 'lvl', 'attack', 'defence', 'speed']:
            raise ValueError("invalid criterion")
        self.criterion = criterion
    
    def get_criterion(self) -> str:
        """return team's criterion

        :complexity: O(1), worst case = best case
        """
        return self.criterion
    
    def get_crit_val(self, poke: Type[PokemonBase]) -> Union[str, int, float]:
        """return pokemon's criterion value

        :param arg1: pokemon to get its criterion value
        :complexity: O(1), worst case = best case
        """
        criterion_table = {
            'hp': poke.get_hp(),
            'lvl': poke.get_level(),
            'attack': poke.get_attack(),
            'defence': poke.get_defence(),
            'speed': poke.get_speed()
        }
        criterion = (self.get_criterion()).lower()
        return criterion_table[criterion]
    
    def choose_team(self, battle_mode: int, criterion: str = None) -> None:
        """take input from user to set up team

        :param arg1: team battle mode
        :param arg2: team criterion 
        :pre: invalid user input
        :post: valid user input
        :complexity: best O(N*n) if assign_team() best case happened,
                     worst O(N*n^2) if assign_team() worst case happened,
                     where  N = number of user incorrect input + 1
                            n = sum(charm, bulb, squir, myst)
        """
        
        self.set_battle_mode(battle_mode) #sets battle mode
        self.set_criterion(criterion) #sets the criterion

        #ask input from user 
        prompt = "Howdy Trainer! Choose your team as C B S M\nwhere \tC is the number of Charmanders \n\tB is the number of Bulbasaurs \n\tS is the number of Squirtles\n\tM is the number of MissingNo\n>"
        valid_input = False

        while not valid_input: #exit while loop only if user gives valid input
            try:
                user_input = input(prompt) #take input from user
                charm, bulb, squir = int(user_input[0]), int(user_input[2]), int(user_input[4]) #extract value from input

                #check MissingNo
                myst = 0
                if len(user_input) >= 6:
                    myst = int(user_input[6])
                    
                self.assign_team(charm, bulb, squir, myst) #popoulate team
            except Exception:
                print("invalid input")
            else:
                valid_input = True

    def assign_team(self, charm: int, bulb: int, squir: int, myst: int = 0) -> None:
        """ populate team based on battle_mode

        :param arg1: number of Charmander
        :param arg2: number of Bulbasaur
        :param arg3: number of Squirtle 
        :param arg4: number of MissingNo
        :complexity: best O(n), if mode_battle == 0 or 1
                     worst O(n^2), if mode_battle == 2
                     and populate_sorted_list() worst case happened
                     where  n = sum(charm, bulb, squir, myst)
        """
        pokemon_num = charm + bulb + squir + myst # total number of pokemons

        #check pokemon number validity 
        if pokemon_num > PokeTeam.POKEMON_LIMIT or myst > 1:
            raise ValueError("invalid pokemon number")
        
        #when battle_mode == 0 
        if self.get_battle_mode() == 0:
            self.populate_stack(charm, bulb, squir, myst)

        #when battle_mode == 1
        elif self.get_battle_mode() == 1:
            self.populate_queue(charm, bulb, squir, myst)

        #when battle_mode == 2
        elif self.get_battle_mode() == 2:
            self.populate_sorted_list(charm, bulb, squir, myst)
            
    def populate_stack(self, charm: int, bulb: int, squir: int, myst: int = 0) -> None:
        """ populate team with Stack

        :param arg1: number of Charmander
        :param arg2: number of Bulbasaur
        :param arg3: number of Squirtle 
        :param arg4: number of MissingNozs
        :complexity: O(n), best case = worst case
                     where n = sum(charm, squir, bulb, myst)
        """
        self.team = ArrayStack(PokeTeam.POKEMON_LIMIT) #instantiate ArrayStack

        #populate stack with pokemons
        #MissingNp
        if bool(myst):
            self.team.push(MissingNo())
        #Squirtle
        for _ in range(squir):
            self.team.push(Squirtle())
        #Bulbasaur
        for _ in range(bulb):
            self.team.push(Bulbasaur())
        #Charmander
        for _ in range(charm):
            self.team.push(Charmander())
        
    def populate_queue(self, charm: int, bulb: int, squir: int, myst: int = 0) -> None:
        """ populate team with CircularQueue

        :param arg1: number of Charmander
        :param arg2: number of Bulbasaur
        :param arg3: number of Squirtle 
        :param arg4: number of MissingNo
        :complexity: O(n), best case = worst casezs
                     where n = sum(charm, squir, bulb, myst)
                     
        """
        self.team = CircularQueue(PokeTeam.POKEMON_LIMIT) #instantiate CircularQueue

        #populate CircularQueue withh pokemons
        #Charmander
        for _ in range(charm):
            self.team.append(Charmander())
        #Bulbasaur
        for _ in range(bulb):
            self.team.append(Bulbasaur())
        #Squirtle
        for _ in range(squir):
            self.team.append(Squirtle())
        #MisingNo
        if bool(myst):
            self.team.append(MissingNo())

    def populate_sorted_list(self, charm: int, bulb: int, squir: int, myst: int = 0) -> None:
        """ populate team with SortedArrayList

        :param arg1: number of Charmander
        :param arg2: number of Bulbasaur
        :param arg3: number of Squirtle 
        :param arg4: number of MissingNo
        :complexity: best O(n), if index to add is always at the middle
                     worst O(n^2), if index to add is always at 0
                     where  n = sum(charm, squir, bulb, myst)
        """
        self.team = ArraySortedList(PokeTeam.POKEMON_LIMIT) #instantiate ArraySortedList

        #populate ArraySortedList with pokemons
        #Squirtle
        for _ in range(squir):
            value = Squirtle()
            key = self.get_crit_val(value)
            self.team.add(ListItem(value, key))
        #Bulbasaur
        for _ in range(bulb):
            value = Bulbasaur()
            key = self.get_crit_val(value)
            self.team.add(ListItem(value, key))
        #Charmander
        for _ in range(charm):
            value = Charmander()
            key = self.get_crit_val(value)
            self.team.add(ListItem(value, key))
        #MissingNo
        if bool(myst):
            value = MissingNo()
            key = float('inf')
            self.team.add(ListItem(value, -key))
    