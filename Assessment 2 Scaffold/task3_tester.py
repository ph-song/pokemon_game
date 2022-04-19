import unittest

from tester_base import TesterBase, captured_output

class TestTask3(TesterBase):

    def test_battle_example(self):
        from battle import Battle

        try:
            b = Battle("Ash", "Misty")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("0 1 0\n1 0 0") as (inp, out, err):
                # Here, Ash gets a Bulbasaur, and Misty gets a Charmander.
                result = b.set_mode_battle()
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            assert result == "Misty"
        except AssertionError:
            self.verificationErrors.append(f"Misty should win: {result}.")

    def test_battle_draw(self):
        from battle import Battle

        try:
            b = Battle("Ash", "Misty")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("0 1 0\n0 1 0") as (inp, out, err):
                # Here, Ash gets a Bulbasaur, and Misty gets a Charmander.
                result = b.set_mode_battle()
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            assert result == "Draw"
        except AssertionError:
            self.verificationErrors.append(f"The result should be draw: {result}.")

    def test_battle_ash(self):
        from battle import Battle

        try:
            b = Battle("Ash", "Misty")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("0 3 0\n0 1 0") as (inp, out, err):
                # Here, Ash gets a Bulbasaur, and Misty gets a Charmander.
                result = b.set_mode_battle()
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            assert result == "Ash"
        except AssertionError:
            self.verificationErrors.append(f"Ash should win: {result}.")  



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTask3)
    unittest.TextTestRunner(verbosity=0).run(suite)