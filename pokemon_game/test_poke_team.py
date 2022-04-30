import unittest
from tester_base import TesterBase, captured_output
from poke_team import PokeTeam
from array_sorted_list import ArraySortedList
from stack_adt import ArrayStack
from queue_adt import CircularQueue
from pokemon import Charmander


class TestPokeTeam(TesterBase):

    def test_poketeam_constr(self): 
        """test correctness of PokeTeam constructor"""
        try:
            t = PokeTeam("trainer")
        except Exception as e:
            self.verificationErrors.append(f"PokeTeam could not be instantiated: {str(e)}.")
            return
        try:
            if t.battle_mode != 0 or t.trainer_name != "trainer" or t.team != None or t.criterion != None:
                self.verificationErrors.append(f"PokeTeam __init__() logic error: {t.battle_mode, t.trainer_name, t.team , t.criterion}")
        except Exception as e:
            self.verificationErrors.append(f"PokeTeam __init__() failed {e}")

    def test_poketeam_str(self):
        """test correctness of PokeTeam __str__()"""
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
                self.verificationErrors.append(f"__str__() did not return correct string: {s}")
        except Exception as e:
            self.verificationErrors.append(f"__str__() failed: {e}")

    def test_get_trainer_name(self):
        """test correctness of PokeTeam get_trainer_name()"""
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
        """test correctness of PokeTeam get_battle_mode()"""
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
        """test correctness of PokeTeam get_battle_mode()"""
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
        """test correctness of PokeTeam set_criterion()"""
        try:
            t = PokeTeam("trainer")
        except Exception as e:
            self.verificationErrors.append(f"PokeTeam could not be instantiated: {str(e)}.")
            return
        try:
            t.set_criterion("attack")
            if t.criterion != "attack":
                self.verificationErrors.append(f"set_criterion() logic error: {t.criterion}")
        except Exception as e:
            self.verificationErrors.append(f"set_criterion() failed: {e}")
            return

    def test_get_criterion(self):
        """test correctness of PokeTeam get_criterion()"""
        try:
            t = PokeTeam("trainer")
        except Exception as e:
            self.verificationErrors.append(f"PokeTeam could not be instantiated: {str(e)}.")
            return
        try:
            t.set_criterion("lvl")
        except Exception as e:
            self.verificationErrors.append(f"set_level() failed: {e}")
        try:
            result = t.get_criterion()
            if result != "lvl":
                self.verificationErrors.append(f"get_criterion() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"get_criterion() failed: {e}")
            return

    def test_get_crit_val(self):
        """test correctness of get_crit_val()"""
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
            t.set_criterion("hp")
        except Exception as e:
            self.verificationErrors.append(f"set_criterion() failed: {e}")
        try:
            result = t.get_crit_val(c)
            if result != 7:
                self.verificationErrors.append(f"get_crit_val() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"get_crit_val() failed: {e}")
            return
    
    def test_choose_team(self):
        """test correctness of choose_team()"""
        try:
            t = PokeTeam("trainer")
        except Exception as e:
            self.verificationErrors.append(f"PokeTeam could not be instantiated: {str(e)}.")
            return
        #test if choose_team can handle invalid input and populate stack
        try:
            with captured_output("0 1 7\n1 1 1") as (inp, out, err):
                t.choose_team(0)
                result = str(t)
            if result != "Charmander's HP = 7 and level = 1, Bulbasaur's HP = 9 and level = 1, Squirtle's HP = 8 and level = 1":
                self.verificationErrors.append(f"battle mode 1 choose_team() logic error {result}")
        except Exception as e:
            self.verificationErrors.append(f"choose_team() failed: {e}")
            return

        #test if choose_team can handle invalid input and populate CircularQueue
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

        #test if choose_team can handle invalid input and populate sorted list
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
                self.verificationErrors.append(f"battle mode 2 choose_team() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"choose_team() failed: {e}")

    def test_assign_team(self):
        """test correctness of test_assign_team()"""
        try:
            t = PokeTeam("trainer")
        except Exception as e:
            self.verificationErrors.append(f"PokeTeam could not be instantiated: {str(e)}.")
            return
        try:
            t.set_battle_mode(0)
        except Exception as e:
            self.verificationErrors.append(f"set_battle_mode() failed: {e}")
        try:
            t.assign_team(1, 1, 1)
            result = type(t.team)
            if result is not ArrayStack:
                self.verificationErrors.append(f"choose_team() logic error, team is: {result}")
        except Exception as e:
            self.verificationErrors.append(f"choose_team() failed: {e}")

    def test_populate_stack(self):
        """test correctness of populate_stack()"""
        try:
            t = PokeTeam("trainer")
        except Exception as e:
            self.verificationErrors.append(f"PokeTeam could not be instantiated: {str(e)}.")
            return
        try:
            t.populate_stack(1, 1, 1)
            result = str(t)
            if result != "Charmander's HP = 7 and level = 1, Bulbasaur's HP = 9 and level = 1, Squirtle's HP = 8 and level = 1":
                self.verificationErrors.append(f"populate_stack() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"populate_stack() failed: {e}")

    def test_populate_queue(self):
        """test correctness of populate_queue()"""
        try:
            t = PokeTeam("trainer")
        except Exception as e:
            self.verificationErrors.append(f"PokeTeam could not be instantiated: {str(e)}.")
            return
        try:
            t.populate_queue(1, 1, 1)
            result = str(t)
            if result != "Charmander's HP = 7 and level = 1, Bulbasaur's HP = 9 and level = 1, Squirtle's HP = 8 and level = 1":
                self.verificationErrors.append(f"populate_queue() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"populate_queue() failed: {e}")

    def test_populate_sorted_list(self):
        """test correctness of populate_sorted_list()"""
        try:
            t = PokeTeam("trainer")
        except Exception as e:
            self.verificationErrors.append(f"PokeTeam could not be instantiated: {str(e)}.")
            return
        try:
            t.set_criterion("hp")
        except Exception as e:
            self.verificationErrors.append(f"set_criterion() failed: {e}")
        try:
            t.populate_sorted_list(1, 1, 1)
            result = str(t)
            if result != "Bulbasaur's HP = 9 and level = 1, Squirtle's HP = 8 and level = 1, Charmander's HP = 7 and level = 1":
                self.verificationErrors.append(f"populate_sorted_list() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"populate_sorted_list() failed: {e}")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPokeTeam)
    unittest.TextTestRunner(verbosity=0).run(suite)