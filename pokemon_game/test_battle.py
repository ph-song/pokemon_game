import unittest
from tester_base import TesterBase, captured_output
from battle import Battle


class TestBattle(TesterBase):

    def test_fight(self):
        try:
            b = Battle("player1", "player2")
            with captured_output("0 1 1\n1 1 1") as (inp, out, err):
                b.player1.choose_team(0)
                b.player2.choose_team(0)
                p1 = b.player1.team.pop()
                p2 = b.player2.team.pop()
                b.fight(p1,p2)
            if str(p1) != "Bulbasaur's HP = -5 and level = 1":
                self.verificationErrors.append(f"fight() logic error, incorrect p1 value: {p1}")
            if str(p2) != "Charmander's HP = 7 and level = 2":
                self.verificationErrors.append(f"fight() logic error, incorrect p2 value: {p2}")
        except Exception as e:
            self.verificationErrors.append(f"fight() failed: {e}")

    def test_set_mode_battle(self):
        try:
            b = Battle("player1", "player2")
            with captured_output("0 1 1\n1 1 1") as (inp, out, err):
                result = b.set_mode_battle()
            if result != "player2":
                self.verificationErrors.append(f"set_mode_battle() logic error {result}")
        except Exception as e:
            self.verificationErrors.append(f"set_mode_battle() failed: {e}")
            return


    def test_rotating_mode_battle(self):
        try:
            b = Battle("player1", "player2")
            with captured_output("1 1 0\n1 1 1") as (inp, out, err):
                result = b.rotating_mode_battle()
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
                result = b.optimised_mode_battle('hp','level')
            if result != "player2":
                self.verificationErrors.append(f"optimised_mode_battle() logic error {result}")
        except Exception as e:
            self.verificationErrors.append(f"optimised_mode_battle() failed: {e}")
            return


    def test_result(self):
        try:
            b = Battle("player1", "player2")
            with captured_output("1 1 1\n1 1 1") as (inp, out, err):
                b.set_mode_battle()
                result = b.result()
            if result != "Draw":
                self.verificationErrors.append(f"result() logic error {result}")
        except Exception as e:
            self.verificationErrors.append(f"result() failed: {e}")
            return
        try:
            b = Battle("player1", "player2")
            with captured_output("0 0 1\n0 0 0") as (inp, out, err):
                b.rotating_mode_battle()
                result = b.result()
            result = b.result()
            if result != "player1":
                self.verificationErrors.append(f"result() logic error {result}")
        except Exception as e:
            self.verificationErrors.append(f"result() failed: {e}")
            return
        try:
            b = Battle("player1", "player2")
            with captured_output("0 0 0\n0 0 1") as (inp, out, err):
                b.optimised_mode_battle('hp', 'attack')
                result = b.result()
            result = b.result()
            if result != "player2":
                self.verificationErrors.append(f"result() logic error {result}")
        except Exception as e:
            self.verificationErrors.append(f"result() failed: {e}")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBattle)
    unittest.TextTestRunner(verbosity=0).run(suite)

