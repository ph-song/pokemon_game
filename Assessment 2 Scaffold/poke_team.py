from pokemon import Charmander, Bulbasaur, Squirtle
from queue_adt import CircularQueue
from array_sorted_list import SortedList

class PokeTeam:
    POKEMON_LIMIT = 6

    def __init__(self, trainer_name: str) -> None:
        self.battle_mode = 0
        self.trainer_name = trainer_name
        #self.team = CircularQueue()

    #task 2.6
    def __str__(self):
        ret = ""
        for i in range(len(self.team)):
            ret += self.team.array[i].__str__() 
            if i != len(self.team) -1:
                ret += ", "
        return ret
    
    #task 2.5 
    def choose_battle_mode(self, battle_mode)-> None:
        if battle_mode not in range(3):
            raise Exception("unavailable battle mode")
        self.battle_mode = battle_mode
        pass
    
    #task 2.3
    def choose_team(self, battle_mode: int, criterion: str = None) -> None:
        #choose battle mode
        self.choose_battle_mode(battle_mode)
        #prompt
        prompt = "Howdy Trainer! Choose your team as C B S \nwhere \tC is the number of Charmanders \n\tB is the number of Bulbasaurs \n\tS is the number of Squirtles\n>"
        valid_input = False
        
        while not valid_input:
            try:
                user_input = input(prompt)
                charm, bulb, squir  = int(user_input[0]), int(user_input[2]), int(user_input[4])
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
        
        #battle_mode == 0 or 1
        if self.battle_mode in (0,1):
            self.team = CircularQueue(pokemon_num)
            self.populate_team(charm, bulb, squir)

        #battle_mode == 2
        elif self.battle_mode == 2:
            self.team = SortedList(pokemon_num)
            self.populate_team(charm, bulb, squir)
            pass
    
    def populate_team(self, charm: int, bulb: int, squir: int)-> None:
        for num in range(charm):
            self.team.append(Charmander())
        for num in range(bulb):
            self.team.append(Bulbasaur())
        for num in range(squir):
            self.team.append(Squirtle())
            
            
#a = PokeTeam('alo')
#a.team = CircularQueue(1)
#a.team.append(Charmander())
#print(a.team.array[0])
#a.choose_team(0)
#print(a)