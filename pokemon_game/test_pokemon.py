import unittest
from pokemon import Bulbasaur, Squirtle, Charmander
from tester_base import TesterBase


class TestPokemon(TesterBase):

    #test Charmander
    def test_char_attacked_by(self):
        try:
            c1 = Charmander()
            c2 = Charmander()
            c1.attacked_by(c2)
            result = str(c1)
            if result != "Charmander's HP = 0 and level = 1":
                self.verificationErrors.append(f"Charmander attacked_by() Charmander logic error: {s}")
        except Exception as e:
            self.verificationErrors.append(f"Charmander attacked_by() Charmander failed {e}")
            return
            
        try:
            c = Charmander()
            s = Squirtle()
            c.attacked_by(s)
            result = str(c)
            if result != "Charmander's HP = -1 and level = 1":
                self.verificationErrors.append(f"Charmander attacked_by() Squirtle logic error: {s}")
        except Exception as e:
            self.verificationErrors.append(f"Charmander attacked_by() Squirtle failed {e}")
            return

    def test_char_get_attack(self):
        try:
            c = Charmander()
            result = c.get_attack()
            if result != 7:
                self.verificationErrors.append(f"Charmander get_attack() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Charmander get_attack() failed {e}")
            return
        try:
            c = Charmander()
            c.set_level(2)
            result = c.get_attack()
            if result != 8:
                self.verificationErrors.append(f"Charmander get_attack() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Charmander get_attack() failed {e}")
            return

    def test_char_get_defence(self):
        try:
            c = Charmander()
            result = c.get_defence()
            if result != 4:
                self.verificationErrors.append(f"Charmander get_defence() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Charmander get_defence() failed {e}")
            return

    def test_char_get_speed(self):
        try:
            c = Charmander()
            result = c.get_speed()
            if result != 8:
                self.verificationErrors.append(f"Charmander get_speed() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Charmander get_speed() failed {e}")
        try:
            c = Charmander()
            c.set_level(2)
            result = c.get_speed()
            if result != 9:
                self.verificationErrors.append(f"Charmander get_speed() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Charmander get_speed() failed {e}")
            return

    #test Bulbasaur
    def test_bulb_attack_by(self):
        try:
            b1 = Bulbasaur()
            b2 = Bulbasaur()
            b1.attacked_by(b2)
            result = str(b1)
            if result != "Bulbasaur's HP = 7 and level = 1":
                self.verificationErrors.append(f"Bulbasaur attacked_by() Bulbasaur logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur attacked_by() Bulbasaur failed {e}")
            return
        try:
            b = Bulbasaur()
            c = Charmander()
            b.attacked_by(c)
            result = str(b)
            if result != "Bulbasaur's HP = -5 and level = 1":
                self.verificationErrors.append(f"Bulbasaur attacked_by() Charmander logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur attacked_by() Charmander failed {e}")
            return

    def test_bulb_get_attack(self):
        try:
            b = Bulbasaur()
            result = b.get_attack()
            if result != 5:
                self.verificationErrors.append(f"Bulbasaur get_attack() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur get_attack() failed {e}")

    def test_bulb_get_defence(self):
        try:
            b = Bulbasaur()
            result = b.get_defence()
            if result != 5:
                self.verificationErrors.append(f"Bulbasaur get_defence() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur get_defence() failed {e}")
            return

    def test_bulb_get_speed(self):
        try:
            c = Bulbasaur()
            result = c.get_speed()
            if result != 7:
                self.verificationErrors.append(f"Bulbasaur get_speed() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur get_speed() failed {e}")
        try:
            c = Bulbasaur()
            c.set_level(2)
            result = c.get_speed()
            if result != 8:
                self.verificationErrors.append(f"Bulbasaur get_speed() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur get_speed() failed {e}")
            return

    #test Squirtle
    def test_char_attacked_by(self):
        try:
            s1 = Squirtle()
            s2 = Squirtle()
            s1.attacked_by(s2)
            result = str(s1)
            if result != "Squirtle's HP = 6 and level = 1":
                self.verificationErrors.append(f"Squirtle attacked_by() Squirtle logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Squirtle attacked_by() Squirtle failed {e}")
            return
        try:
            s = Squirtle()
            b = Bulbasaur()
            s.attacked_by(b)
            result = str(s)
            if result != "Squirtle's HP = 3 and level = 1":
                self.verificationErrors.append(f"Squirtle attacked_by() Bulbasaur logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Squirtle attacked_by() Bulbasaur failed {e}")
            return

    def test_squir_get_attack(self):
        try:
            s = Squirtle()
            result = s.get_attack()
            if result != 4:
                self.verificationErrors.append(f"Squirtle get_attack() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Squirtle get_attack() failed {e}")
            return
        try:
            s = Squirtle()
            s.set_level(2)
            result = s.get_attack()
            if result != 5:
                self.verificationErrors.append(f"Squirtle get_attack() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Squirtle get_attack() failed {e}")
            return

    def test_squir_get_defence(self):
        try:
            s = Squirtle()
            result = s.get_defence()
            if result != 7:
                self.verificationErrors.append(f"Squirtle get_defence() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Squirtle get_defence() failed {e}")
        try:
            s = Squirtle()
            s.set_level(2)
            result = s.get_defence()
            if result != 8:
                self.verificationErrors.append(f"Squirtle get_defence() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Squirtle get_defence() failed {e}")
            return

    def test_squir_get_speed(self):
        try:
            c = Squirtle()
            result = c.get_speed()
            if result != 7:
                self.verificationErrors.append(f"Squirtle get_speed() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Squirtle get_speed() failed {e}")
            return


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPokemon)
    unittest.TextTestRunner(verbosity=0).run(suite)