import unittest

from tester_base import TesterBase


class TestTask1(TesterBase):

    def test_charmander_string(self):
        from pokemon import Charmander
        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(f"Charmander could not be instantiated: {str(e)}.")
            return
        try:
            s = str(c)
            if s != "Charmander's HP = 7 and level = 1":
                self.verificationErrors.append(f"String method did not return correct string: {s}")
        except Exception as e:
            self.verificationErrors.append(f"String method failed. {e}")

    def test_bulbasaur_string(self):
        from pokemon import Bulbasaur
        try:
            c = Bulbasaur()
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur could not be instantiated: {str(e)}.")
            return
        try:
            s = str(c)
            if s != "Bulbasaur's HP = 9 and level = 1":
                self.verificationErrors.append(f"String method did not return correct string: {s}")
        except Exception as e:
            self.verificationErrors.append(f"String method failed. {e}")

    def test_squirtle_string(self):
        from pokemon import Squirtle
        try:
            c = Squirtle()
        except Exception as e:
            self.verificationErrors.append(f"Squirtle could not be instantiated: {str(e)}.")
            return
        try:
            s = str(c)
            if s != "Squirtle's HP = 8 and level = 1":
                self.verificationErrors.append(f"String method did not return correct string: {s}")
        except Exception as e:
            self.verificationErrors.append(f"String method failed. {e}")

    def test_damage_taken(self):
        from pokemon import Charmander, Squirtle
        c = Charmander()
        s = Squirtle()
        try:
            c.attacked_by(s)
            damage = c.hp
            if damage != 6:
                self.verificationErrors.append(f"Damage taken method did not return correct float: {damage}")
        except Exception as e:
            self.verificationErrors.append(f"Damage taken method failed. {e}")



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTask1)
    unittest.TextTestRunner(verbosity=0).run(suite)