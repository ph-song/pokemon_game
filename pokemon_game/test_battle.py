import unittest
from tester_base import TesterBase, captured_output
from battle import Battle


class TestBattle(TesterBase):

    def test_fight(self):
        """test if the battle of the pokemon is implemented correctly"""
        try:
            b = Battle("player1", "player2")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("0 1 1\n1 1 1") as (inp, out, err):
                b.team1.choose_team(0)
                b.team2.choose_team(0)
        except Exception as e:
            self.verificationErrors.append(f"{e}")
            return
        try:
            p1 = b.team1.team.pop()
        except Exception as e:
            self.verificationErrors.append(f"failed to pop pokemon from team1{e}")
            return
        try:
            p2 = b.team2.team.pop()
        except Exception as e:
            self.verificationErrors.append(f"failed to pop pokemon form team2{e}")
            return
        try:
            b.fight(p1, p2)
            if str(p1) != "Bulbasaur's HP = -5 and level = 1":
                self.verificationErrors.append(f"incorrect p1 value: {p1}")
            if str(p2) != "Charmander's HP = 7 and level = 2":
                self.verificationErrors.append(f"incorrect p2 value: {p2}")
        except Exception as e:
            self.verificationErrors.append(f"fight() failed: {e}")

    def test_set_mode_battle(self):
        """test if set_mode_battle() returns correct result"""
        try:
            b = Battle("player1", "player2")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("0 1 1\n1 1 1") as (inp, out, err):
                result = b.set_mode_battle()
            if result != "player2":
                self.verificationErrors.append(f"set_mode_battle incorrect result: {result}")
        except Exception as e:
            self.verificationErrors.append(f"set_mode_battle() failed: {e}")


    def test_rotating_mode_battle(self):
        """test if rotating_mode_battle() returns correct result"""
        try:
            b = Battle("player1", "player2")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("1 1 0\n1 1 1") as (inp, out, err):
                result = b.rotating_mode_battle()
            if result != "player2":
                self.verificationErrors.append(f"rotating_mode() incorrect result: {result}")
        except Exception as e:
            self.verificationErrors.append(f"rotating_mode() failed: {e}")


    def test_optimised_mode_battle(self):
        """test if optimised_mode_battle() returns correct result"""
        try:
            b = Battle("player1", "player2")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("0 1 1\n1 1 1") as (inp, out, err):
                result = b.optimised_mode_battle('hp','lvl')
            if result != "player2":
                self.verificationErrors.append(f"optimised_mode_battle() logic error {result}")
        except Exception as e:
            self.verificationErrors.append(f"optimised_mode_battle() failed: {e}")


    def test_result(self):
        """test if result() returns correct winner"""
        try:
            b = Battle("player1", "player2")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("1 1 1\n1 1 1") as (inp, out, err):
                b.set_mode_battle()
                result = b.result()
            if result != "Draw":
                self.verificationErrors.append(f"result() logic error {result}")
        except Exception as e:
            self.verificationErrors.append(f"result() failed: {e}")
        try:
            b = Battle("player1", "player2")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("0 0 1\n0 0 0") as (inp, out, err):
                b.rotating_mode_battle()
                result = b.result()
            if result != "player1":
                self.verificationErrors.append(f"result() logic error {result}")
        except Exception as e:
            self.verificationErrors.append(f"result() failed: {e}")
            return
        try:
            b = Battle("player1", "player2")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("0 0 0\n0 0 1") as (inp, out, err):
                b.optimised_mode_battle('hp', 'attack')
                result = b.result()
            result = b.result()
            if result != "player2":
                self.verificationErrors.append(f"result() logic error {result}")
        except Exception as e:
            self.verificationErrors.append(f"result() failed: {e}")
            return 


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBattle)
    unittest.TextTestRunner(verbosity=0).run(suite)

