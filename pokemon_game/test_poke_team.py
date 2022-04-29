import unittest
from tester_base import TesterBase, captured_output
from poke_team import PokeTeam
from array_sorted_list import ArraySortedList
from stack_adt import ArrayStack
from queue_adt import CircularQueue
from pokemon import Charmander


class TestPokeTeam(TesterBase):

    def test_poketeam_init(self): 
        """test whether the init method initialises a PokeTeam attributes correctly"""
        try:
            t = PokeTeam("trainer")
        except Exception as e:
            self.verificationErrors.append(f"PokeTeam could not be instantiated: {str(e)}.")
            return
        try:
            res_battle_mode = t.battle_mode
            res_trainer_name = t.trainer_name
            res_team = t.team 
            res_criterion = t.criterion
            if res_battle_mode != 0 or res_trainer_name != "trainer" or res_team != None or res_criterion != None:
                self.verificationErrors.append(f"PokeTeam __init__() logic error: {res_battle_mode, res_trainer_name, res_team, res_criterion}")
        except Exception as e:
            self.verificationErrors.append(f"PokeTeam __init__() failed {e}")
            return

    def test_poketeam_string(self):
        """
        test whether PokeTeam is instantiated successfully
        test whether PokeTeam object is printed correctly
        """
        try:
            t = PokeTeam("Ash")
        except Exception as e:
            self.verificationErrors.append(f"PokeTeam could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("0 1 1") as (inp, out, err):
                t.choose_team(1)
        except Exception as e:
            self.verificationErrors.append(f"choose_team() failed: {str(e)}.")
            return
        try:
            s = str(t)
            if s != "Bulbasaur's HP = 9 and level = 1, Squirtle's HP = 8 and level = 1":
                self.verificationErrors.append(f"String method did not return correct string: {s}")
        except Exception as e:
            self.verificationErrors.append(f"String method failed. {e}")
            return 

    def test_get_trainer_name(self):
        """
        test whether the get_trainer_name method returns the correct trainer name of a Pokemon team
        """
        try:
            t = PokeTeam("trainer")
        except Exception as e:
            self.verificationErrors.append(f"PokeTeam could not be instantiated: {str(e)}.")
            return
        try:
            result = t.get_trainer_name()
            if result != "trainer":
                self.verificationErrors.append(f"get_trainer_name() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"get_trainer_name() failed: {e}")
            return

    def test_get_battle_mode(self):
        """
        test whether the get_battle_mode method returns the correct battle mode of a Pokemon team
        """
        try:
            t = PokeTeam("trainer")
        except Exception as e:
            self.verificationErrors.append(f"PokeTeam could not be instantiated: {str(e)}.")
            return
        try:
            t.battle_mode = 1
            result = t.get_battle_mode()
            if result != 1:
                self.verificationErrors.append(f"get_battle_mode() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"get_battle_mode() failed: {e}")
            return

    def test_set_battle_mode(self):
        """
        test whether the set_battle_mode method sets the correct battle mode of a Pokemon team
        """
        try:
            t = PokeTeam("trainer")
        except Exception as e:
            self.verificationErrors.append(f"PokeTeam could not be instantiated: {str(e)}.")
            return
        try:
            t.set_battle_mode(2)
            result = t.battle_mode
            if result != 2:
                self.verificationErrors.append(f"set_battle_mode() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"set_battle_mode() failed: {e}")
            return

    def test_set_criterion(self):
        """
        test whether the set_criterion method sets the correct criterion of a Pokemon team
        """
        try:
            t = PokeTeam("trainer")
        except Exception as e:
            self.verificationErrors.append(f"PokeTeam could not be instantiated: {str(e)}.")
            return
        try:
            t.set_criterion("attack")
            result = t.criterion
            if result != "attack":
                self.verificationErrors.append(f"set_criterion() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"set_criterion() failed: {e}")
            return

    def test_get_criterion(self):
        """
        test whether the get_criterion method returns the correct criterion of a Pokemon team
        """
        try:
            t = PokeTeam("trainer")
        except Exception as e:
            self.verificationErrors.append(f"PokeTeam could not be instantiated: {str(e)}.")
            return
        try:
            t.criterion = "lvl"
            result = t.get_criterion()
            if result != "lvl":
                self.verificationErrors.append(f"get_criterion() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"get_criterion() failed: {e}")
            return

    def test_get_crit_val(self):
        """
        test whether the get_criterion_val method returns the correct criterion value of a Pokemon team
        """
        try:
            t = PokeTeam("trainer")
        except Exception as e:
            self.verificationErrors.append(f"PokeTeam could not be instantiated: {str(e)}.")
            return
        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(f"Charmander could not be instantiated: {str(e)}.")
            return
        try:
            t.criterion = "hp"
            result = t.get_crit_val(c)
            if result != 7:
                self.verificationErrors.append(f"get_crit_val() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"get_crit_val() failed: {e}")
            return
    
    def test_choose_team(self):
        """
        test whether choose_team method allows for additional input attempts after invalid input
        test whether the Pokemon is added in the correct order using ArrayStack
        test whether the Pokemon is added in the correct order using CircularQueue
        test whether the Pokemon is added in the correct order according to the criterion
        """
        try:
            t = PokeTeam("trainer")
        except Exception as e:
            self.verificationErrors.append(f"PokeTeam could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("0 1 7\n1 1 1") as (inp, out, err):
                t.choose_team(0)
                result = str(t)
            if result != "Charmander's HP = 7 and level = 1, Bulbasaur's HP = 9 and level = 1, Squirtle's HP = 8 and level = 1":
                self.verificationErrors.append(f"battle mode 1 choose_team() logic error {result}")
        except Exception as e:
            self.verificationErrors.append(f"choose_team() failed: {e}")
            return

        try:
            t = PokeTeam("trainer")
        except Exception as e:
            self.verificationErrors.append(f"PokeTeam could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("abcde\n1 1 1") as (inp, out, err):
                t.choose_team(1)
                result = str(t)
            if result != "Charmander's HP = 7 and level = 1, Bulbasaur's HP = 9 and level = 1, Squirtle's HP = 8 and level = 1":
                self.verificationErrors.append(f"battle mode 1 choose_team() logic error {result}")
        except Exception as e:
            self.verificationErrors.append(f"choose_team() failed: {e}")
            return

        try:
            t = PokeTeam("trainer")
        except Exception as e:
            self.verificationErrors.append(f"PokeTeam could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("0 1 7\n1 1 1") as (inp, out, err):
                t.choose_team(2, "speed")
                result = str(t)
            if result != "Charmander's HP = 7 and level = 1, Bulbasaur's HP = 9 and level = 1, Squirtle's HP = 8 and level = 1":
                self.verificationErrors.append(f"battle mode 2 choose_team() logic error {result}")
        except Exception as e:
            self.verificationErrors.append(f"choose_team() failed: {e}")

    def test_assign_team(self):
        """
        test whether the team is populated correctly based on the battle mode
        """
        try:
            t = PokeTeam("trainer")
        except Exception as e:
            self.verificationErrors.append(f"PokeTeam could not be instantiated: {str(e)}.")
            return
        try:
            t.set_battle_mode(0)
            t.assign_team(1, 1, 1)
            result = type(t.team)
            if result is not ArrayStack:
                self.verificationErrors.append(f"choose_team() logic error {result}")
        except Exception as e:
            self.verificationErrors.append(f"choose_team() failed: {e}")

    def test_populate_stack(self):
        """
        test whether the team populated is an ArrayStack
        """
        try:
            t = PokeTeam("trainer")
        except Exception as e:
            self.verificationErrors.append(f"PokeTeam could not be instantiated: {str(e)}.")
            return
        try:
            t.populate_stack(1, 1, 1)
            result = type(t.team)
            if result is not ArrayStack:
                self.verificationErrors.append(f"choose_team() logic error {result}")
        except Exception as e:
            self.verificationErrors.append(f"choose_team() failed: {e}")

    def test_populate_queue(self):
        """
        test whether the team populated is a CircularQueue
        """
        try:
            t = PokeTeam("trainer")
        except Exception as e:
            self.verificationErrors.append(f"PokeTeam could not be instantiated: {str(e)}.")
            return
        try:
            t.populate_queue(1, 1, 1)
            result = type(t.team)
            if result is not CircularQueue:
                self.verificationErrors.append(f"choose_team() logic error {result}")
        except Exception as e:
            self.verificationErrors.append(f"choose_team() failed: {e}")

    def test_populate_sorted_list(self):
        """
        test whether the team populated is an ArraySortedList
        """
        try:
            t = PokeTeam("trainer")
        except Exception as e:
            self.verificationErrors.append(f"PokeTeam could not be instantiated: {str(e)}.")
            return
        try:
            t.set_criterion("hp")
            t.populate_sorted_list(1, 1, 1)
            result = type(t.team)
            if result is not ArraySortedList:
                self.verificationErrors.append(f"choose_team() logic error {result}")
        except Exception as e:
            self.verificationErrors.append(f"choose_team() failed: {e}")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPokeTeam)
    unittest.TextTestRunner(verbosity=0).run(suite)