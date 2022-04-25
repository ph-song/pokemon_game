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
        """ Initialiser method of PokeTeam class.

        :complexity: O(1), all assignments have constant cost
                     Best case = Worst case because no element properties can change this
        """
        self.battle_mode = self.INITIAL_BATTLE_MODE
        self.trainer_name = trainer_name
        self.team = None 
        self.criterion = None
  
    def __str__(self) ->str:
        """ String method of PokeTeam class.

        :complexity: O(n), where n = number of elements in team,
                     iterating each element in team to convert them into str,
                     Best case = Worst case because no element properties can change this
        """
        return str(self.team)

    def get_trainer_name(self) ->str:
        """ Attribute trainer_name getter.

        :complexity: O(1), return statements have constant cost,
                     Best case = Worst case because no element properties can change this
        """
        return self.trainer_name

    def get_battle_mode(self) ->int:
        """ Attribute battle_mode getter.

        :complexity: O(1), return statements have constant cost,
                     Best case = Worst case because no element properties can change this
        """
        return self.battle_mode
    
    def set_battle_mode(self, battle_mode: int) ->None:
        """ Attribute battle_mode setter.

        :pre: battle_mode can either only be 0,1,2
        :complexity: O(1), raising exceptions and assignments have constant cost,
                     checking whether battle_mode in range(3) has constant cost as well,
                     Best case = Worst case because no element properties can change this
        """
        # checks validity of battle_mode
        if battle_mode not in range(3):
            raise ValueError("unavailable battle mode")
        self.battle_mode = battle_mode
    
    def set_criterion(self, criterion: str) ->None:
        """ Attribute criterion setter.

        :complexity: O(1), all assignments have constant cost
                     Best case = Worst case because no element properties can change this
        """
        if criterion not in [None, 'hp', 'level', 'attack', 'defence', 'speed']:
            raise Exception("invalid critereon")
        self.criterion = criterion
    
    def get_criterion(self) ->str:
        """ Attribute criterion getter.

        :complexity: O(1), return statements have constant cost
                     Best case = Worst case because no element properties can change this
        """
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
        """ Choose number of pokemons for each type to form a team.

        :complexity:
        """
        
        self.set_battle_mode(battle_mode) #set battle mode
        self.set_criterion(criterion) # sets the criterion 

        #ask input from user 
        prompt = "Howdy Trainer! Choose your team as C B S M\nwhere \tC is the number of Charmanders \n\tB is the number of Bulbasaurs \n\tS is the number of Squirtles\n\tM is the number of Mystery Pokemon\n>"
        valid_input = False

        while not valid_input: #exit while loop only if user gives valid input
            try:
                user_input = input(prompt)
                charm, bulb, squir = int(user_input[0]), int(user_input[2]), int(user_input[4])

                #check MissingNo
                myst = 0
                if len(user_input) >=6:
                    myst = int(user_input[6])

                self.assign_team(charm, bulb, squir, myst) #popoulate team

            except Exception:
                print("invalid input")
            else:
                valid_input = True

    def assign_team(self, charm: int, bulb: int, squir: int, myst: int = 0) -> None:
        """ Populates the team according to the battle mode.

        :complexity:
        """
        pokemon_num = charm + bulb + squir + myst # total number of pokemon

        #raise error if pokemon number exceed limit
        if pokemon_num > self.POKEMON_LIMIT or myst > 1:
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
            
    def populate_stack(self, charm: int, bulb: int, squir: int, myst: int = 0) ->None:
        """ Populates the team using stack. Last in first out for battle mode 0.

        :complexity: O(n), where n = charm/bulb/squir,
                     Best case = Worst case because no element properties can change this
        """
        self.team = ArrayStack(self.POKEMON_LIMIT) #instantiate ArrayStack

        #populate stack
        if bool(myst):
            self.team.push(MissingNo())
        for i in range(squir):
            self.team.push(Squirtle())
        for i in range(bulb):
            self.team.push(Bulbasaur())
        for i in range(charm):
            self.team.push(Charmander())
        
    def populate_queue(self, charm: int, bulb: int, squir: int, myst: int = 0) ->None:
        """ Populates the team using circular queue. First in first out for battle mode 1.

        :complexity: O(n), where n = charm/bulb/squir,
                     Best case = Worst case because no element properties can change this
        """
        self.team = CircularQueue(self.POKEMON_LIMIT) #instantiate CircularQueue

        #populate CircularQueue
        for i in range(charm):
            self.team.append(Charmander())
        for i in range(bulb):
            self.team.append(Bulbasaur())
        for i in range(squir):
            self.team.append(Squirtle())
        if bool(myst):
            self.team.append(MissingNo())


    def populate_sorted_list(self, charm: int, bulb: int, squir: int, myst: int = 0) ->None:
        """ Populates the team using circular queue. First in first out for battle mode 1.

        :complexity: O(n), where n = charm/bulb/squir,
                     Best case = Worst case because no element properties can change this
        """
        self.team = ArraySortedList(self.POKEMON_LIMIT) #instantiate ArraySortedList

        #populate ArraySortedList
        for i in range(squir):
            value = Squirtle()
            key = self.get_criterion_val(value)
            self.team.add(ListItem(value, key))
        for i in range(bulb):
            value = Bulbasaur()
            key = self.get_criterion_val(value)
            self.team.add(ListItem(value, key))
        for i in range(charm):
            value = Charmander()
            key = self.get_criterion_val(value)
            self.team.add(ListItem(value, key))
        if bool(myst):
            value = MissingNo()
            key = float('inf')
            self.team.add(ListItem(value, -key))
            
