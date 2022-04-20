from matplotlib.cbook import Stack
from pokemon import Charmander, Bulbasaur, Squirtle
from queue_adt import CircularQueue
from array_sorted_list import SortedList
from stack_adt import ArrayStack

class PokeTeam: 
    POKEMON_LIMIT = 6
    INITIAL_BATTLE_MODE = 0

    def __init__(self, trainer_name: str) -> None:
        self.battle_mode = self.INITIAL_BATTLE_MODE
        self.trainer_name = trainer_name
        self.team = None
    
    def __str__(self):
        ret = ""
        if type(self.team) is ArrayStack:
            for i in range(len(self.team)):
                ret += str(self.team.array[i]) + ", "

        elif type(self.team) is CircularQueue:
            for i in range(len(self.team)):
                front = self.team.front
                length = len(self.team.array)
                if front + i < length:
                    ret += str(self.team.array[i+front]) + ", "
                else:
                    ret += str(self.team.array[i+front-length]) + ", "

        return ret[:-2] #remove excess ", "

    def _str_(self) -> str:
        string = ""
        if self.battle_mode == 0:
            for i in range(len(self.team)):
                if not i:
                    string = self.team.array[i]._str_() + string
                else:
                    string = self.team.array[i]._str_() + ", " + string
        elif self.battle_mode == 1:
            index = self.team.front
            for i in range(self.team._len_()):
                pokemon = self.team.array[index]
                if i == self.team._len_() - 1:
                    string += str(pokemon)
                else:
                    string += str(pokemon) + ", "
                index = (index + 1) % len(self.team.array)
        return string

        

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
    
    def choose_team(self, battle_mode: int, criterion: str = None) -> None:
        """choose number of pokemons and form a team"""

        self.set_battle_mode(battle_mode) #set battle mode

        #ask input from user 
        prompt = "Howdy Trainer! Choose your team as C B S \nwhere \tC is the number of Charmanders \n\tB is the number of Bulbasaurs \n\tS is the number of Squirtles\n>"
        valid_input = False
        while not valid_input:
            try:
                user_input = input(prompt)
                charm, bulb, squir = int(user_input[0]), int(user_input[2]), int(user_input[4])
                self.assign_team(charm, bulb, squir) #popoulate team
            except Exception:
                print("invalid input")
            else:
                valid_input = True

    def assign_team(self, charm: int, bulb: int, squir: int) -> None:
        """populate team"""
        pokemon_num = charm + bulb + squir
        if pokemon_num > self.POKEMON_LIMIT:
            raise Exception("exceed team pokemon limit")
        
        #when battle_mode == 0 
        if self.get_battle_mode() == 0:
            self.team = ArrayStack(pokemon_num)
            for num in range(charm):
                self.team.push(Charmander())
            for num in range(bulb):
                self.team.push(Bulbasaur())
            for num in range(squir):
                self.team.push(Squirtle())
            
        #when battle_mode == 0 
        elif self.get_battle_mode() == 1:
            self.team = CircularQueue(pokemon_num)
            for num in range(charm):
                self.team.append(Charmander())
            for num in range(bulb):
                self.team.append(Bulbasaur())
            for num in range(squir):
                self.team.append(Squirtle())

        #when battle_mode == 2
        elif self.get_battle_mode() == 2:
            self.team = SortedList(pokemon_num)
            pass
    
