import unittest
from tester_base import TesterBase, captured_output
from poke_team import PokeTeam
from array_sorted_list import ArraySortedList
from stack_adt import ArrayStack
from queue_adt import CircularQueue


class TestPokeTeam(TesterBase):

    def test_get_trainer_name(self):
        try:
            t = PokeTeam("trainer")
            result = t.get_trainer_name()
            if result != "trainer":
                self.verificationErrors.append(f"get_trainer_name() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"get_trainer_name() failed: {e}")
            return
    
    def test_choose_team(self):
        try:
            t = PokeTeam("trainer")
            with captured_output("0 1 7\n1 1 1") as (inp, out, err):
                t.choose_team(0)
                result = str(t)
            if result != "Charmander's HP = 7 and level = 1, Bulbasaur's HP = 9 and level = 1, Squirtle's HP = 8 and level = 1":
                self.verificationErrors.append(f"choose_team() logic error {result}")
        except Exception as e:
            self.verificationErrors.append(f"choose_team() failed: {e}")
            return
        try:
            t = PokeTeam("trainer")
            with captured_output("abcde\n1 1 1") as (inp, out, err):
                t.choose_team(1)
                result = str(t)
            if result != "Charmander's HP = 7 and level = 1, Bulbasaur's HP = 9 and level = 1, Squirtle's HP = 8 and level = 1":
                self.verificationErrors.append(f"choose_team() logic error {result}")
        except Exception as e:
            self.verificationErrors.append(f"choose_team() failed: {e}")
            return
        
        try:
            t = PokeTeam("trainer")
            with captured_output("0 1 7\n1 1 1") as (inp, out, err):
                t.choose_team(2, "speed")
                result = str(t)
            if result != "Charmander's HP = 7 and level = 1, Bulbasaur's HP = 9 and level = 1, Squirtle's HP = 8 and level = 1":
                self.verificationErrors.append(f"choose_team() logic error {result}")
        except Exception as e:
            self.verificationErrors.append(f"choose_team() failed: {e}")

    def test_assign_team(self):
        try:
            t = PokeTeam("trainer")
            t.set_battle_mode(0)
            t.assign_team(1, 1, 1)
            result = type(t.team)
            if result is not ArrayStack:
                self.verificationErrors.append(f"choose_team() logic error {result}")
        except Exception as e:
            self.verificationErrors.append(f"choose_team() failed: {e}")

    def test_populate_stack(self):
        try:
            t = PokeTeam("trainer")
            t.populate_stack(1, 1, 1)
            result = type(t.team)
            if result is not ArrayStack:
                self.verificationErrors.append(f"choose_team() logic error {result}")
        except Exception as e:
            self.verificationErrors.append(f"choose_team() failed: {e}")

    def test_populate_queue(self):
        try:
            t = PokeTeam("trainer")
            t.populate_queue(1, 1, 1)
            result = type(t.team)
            if result is not CircularQueue:
                self.verificationErrors.append(f"choose_team() logic error {result}")
        except Exception as e:
            self.verificationErrors.append(f"choose_team() failed: {e}")

    def test_populate_sorted_list(self):
        try:
            t = PokeTeam("trainer")
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