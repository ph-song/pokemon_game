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
    
    #task 2.6
    def __str__(self):
        ret = ""
        for i in range(len(self.team)):
            ret += self.team.array[i].__str__() 
            if i != len(self.team) -1:
                ret += ", "
        return ret

    def get_trainer_name(self):
        return self.trainer_name

    def get_battle_mode(self):
        return self.battle_mode

    def get_batle_mode(self):
        return self.battle_mode
    
    def set_battle_mode(self, battle_mode: int):
        if battle_mode not in range(3):
            raise Exception("unavailable battle mode")
        self.battle_mode = battle_mode
    
    #task 2.3
    def choose_team(self, battle_mode: int, criterion: str = None) -> None:
        #choose battle mode
        self.set_battle_mode(battle_mode)
        #prompt
        prompt = "Howdy Trainer! Choose your team as C B S \nwhere \tC is the number of Charmanders \n\tB is the number of Bulbasaurs \n\tS is the number of Squirtles\n>"
        valid_input = False
        
        while not valid_input:
            try:
                user_input = input(prompt)
                charm, bulb, squir = int(user_input[0]), int(user_input[2]), int(user_input[4])
                self.assign_team(charm, bulb, squir)
            except Exception:
                print("invalid input")
            else:
                valid_input = True

    #task 2.4
    def assign_team(self, charm: int, bulb: int, squir: int) -> None:
        pokemon_num = charm + bulb + squir
        if pokemon_num > self.POKEMON_LIMIT:
            raise Exception("exceed team pokemon limit")
        
        #battle_mode == 0 
        if self.get_batle_mode() == 0:
            self.team = ArrayStack(pokemon_num)
            for num in range(charm):
                self.team.push(Charmander())
            for num in range(bulb):
                self.team.push(Bulbasaur())
            for num in range(squir):
                self.team.push(Squirtle())
            
        #battle_mode == 0 
        elif self.get_battle_mode() == 1:
            self.team = CircularQueue(pokemon_num)
            for num in range(charm):
                self.team.append(Charmander())
            for num in range(bulb):
                self.team.append(Bulbasaur())
            for num in range(squir):
                self.team.append(Squirtle())

        #battle_mode == 2
        elif self.get_battle_mode() == 2:
            self.team = SortedList(pokemon_num)
            #populate team
            pass
    
