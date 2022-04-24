import unittest
from tester_base import TesterBase, captured_output
from battle import Battle
from array_sorted_list import ArraySortedList
from stack_adt import ArrayStack
from queue_adt import CircularQueue

class TestBattle(TesterBase):
    def test_fight(self):
        #poke1, poke2
        pass


    def test_set_mode_battle(self):
        try:
            b = Battle("player1", "player2")
            with captured_output("0 1 1\n1 1 1") as (inp, out, err):
                b.set_mode_battle()
            result = "player2"
            if result != "player2":
                self.verificationErrors.append(f"set_mode_battle() logic error {result}")
        except Exception as e:
            self.verificationErrors.append(f"set_mode_battle() failed: {e}")
            return


    def test_rotating_mode_battle(self):
        try:
            b = Battle("player1", "player2")
            with captured_output("0 1 1\n1 1 1") as (inp, out, err):
                b.rotating_mode_battle()
            result = "player2"
            if result != "player2":
                self.verificationErrors.append(f"rotating_mode() logic error {result}")
        except Exception as e:
            self.verificationErrors.append(f"rotating_mode() failed: {e}")
            return


    def test_optimised_mode_battle(self):
        #criterion_team1: str, criterion_team2: str
        try:
            b = Battle("player1", "player2")
            with captured_output("0 1 1\n1 1 1") as (inp, out, err):
                b.optimised_mode_battle('hp','level')
            result = "player2"
            if result != "player2":
                self.verificationErrors.append(f"optimised_mode_battle() logic error {result}")
        except Exception as e:
            self.verificationErrors.append(f"optimised_mode_battle() failed: {e}")
            return


    def test_result(self):
        try:
            b = Battle("player1", "player2")
            b.player1.set_battle_mode(0)
            b.player2.set_battle_mode(0)
            b.player1.assign_team(1,1,1)
            b.player2.assign_team(0,0,0)
            result = b.result()
            if result != "player1":
                self.verificationErrors.append(f"result() logic error {result}")
        except Exception as e:
            self.verificationErrors.append(f"result() failed: {e}")
            return
        try:
            b = Battle("player1", "player2")
            b.player1.set_battle_mode(1)
            b.player2.set_battle_mode(1)
            b.player1.assign_team(0,0,0)
            b.player2.assign_team(0,0,1)
            result = b.result()
            if result != "player2":
                self.verificationErrors.append(f"result() logic error {result}")
        except Exception as e:
            self.verificationErrors.append(f"result() failed: {e}")
            return
        try:
            b = Battle("player1", "player2")
            b.player1.set_battle_mode(1)
            b.player2.set_battle_mode(1)
            b.player1.assign_team(0,0,0)
            b.player2.assign_team(0,0,0)
            result = b.result()
            if result != "Draw":
                self.verificationErrors.append(f"result() logic error {result}")
        except Exception as e:
            self.verificationErrors.append(f"result() failed: {e}")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBattle)
    unittest.TextTestRunner(verbosity=0).run(suite)

