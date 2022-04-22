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

    def test_get_attack_charmander(self):
        from pokemon import Charmander
        c = Charmander()
        try:
            att = float(c.get_attack())
            if att != 7:
                self.verificationErrors.append(f"Get attack method did not return correct integer: {att}")
        except Exception as e:
            self.verificationErrors.append(f"Get attack method failed. {e}")

    def test_get_attack_squirtle(self):
        from pokemon import Squirtle
        c = Squirtle()
        try:
            att = float(c.get_attack())
            if att != 4:
                self.verificationErrors.append(f"Get attack method did not return correct integer: {att}")
        except Exception as e:
            self.verificationErrors.append(f"Get attack method failed. {e}")

    def test_is_faint(self):
        from pokemon import Charmander, Bulbasaur
        b = Bulbasaur()
        try:
            # b.set_hp(b.get_hp() - (b.get_attack() * 2))
            flag = b.is_fainted()
            if flag != False:
                self.verificationErrors.append(f"Is_faint method did not return correct float: {flag}")
        except Exception as e:
            self.verificationErrors.append(f"Is_faint method failed. {e}")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTask1)
    unittest.TextTestRunner(verbosity=0).run(suite)
