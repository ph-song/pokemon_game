import unittest
from pokemon import Bulbasaur, Squirtle, Charmander, GlitchMon, MissingNo
from tester_base import TesterBase
from random import seed


class TestPokemon(TesterBase):
    """test Charmander"""

    def test_char_constr(self):
        """test Charmander constructor"""
        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(f"Charmander could not be instantiated: {str(e)}.")
            return
        try:
            s = str(c)
            if s != "Charmander's HP = 7 and level = 1":
                self.verificationErrors.append(f"Charmander __init__() logic error: {s}")
        except Exception as e:
            self.verificationErrors.append(f"Charmander __str__() method failed. {e}")
            return 

    def test_char_attacked_by(self):
        """test correctness of Charmander attacked_by()"""
        #test a Charmander's HP and level after being attacked by another Charmander
        try:
            c1 = Charmander()
        except Exception as e:
            self.verificationErrors.append(f"Charmander1 could not be instantiated: {str(e)}.")
            return
        try:
            c2 = Charmander()
        except Exception as e:
            self.verificationErrors.append(f"Charmander2 could not be instantiated: {str(e)}.")
            return
        try:
            c1.attacked_by(c2)
            result = str(c1)
            if result != "Charmander's HP = 0 and level = 1":
                self.verificationErrors.append(f"Charmander attacked_by() Charmander logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Charmander attacked_by() Charmander failed {e}")
            return
        #test Charmander's HP and level after being attacked by Squirtle
        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(f"Charmander could not be instantiated: {str(e)}.")
            return
        try:
            s = Squirtle()
        except Exception as e:
            self.verificationErrors.append(f"Squirtle could not be instantiated: {str(e)}.")
            return
        try:
            c.attacked_by(s)
            result = str(c)
            if result != "Charmander's HP = -1 and level = 1":
                self.verificationErrors.append(f"Charmander attacked_by() Squirtle logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Charmander attacked_by() Squirtle failed {e}")
            return

    def test_char_get_attack(self):
        """test correctness of Charmander get_attack()"""
        #test attack of Charmander before level up
        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(f"Charmander could not be instantiated: {str(e)}.")
            return
        try:
            result = c.get_attack()
            if result != 7:
                self.verificationErrors.append(f"Charmander get_attack() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Charmander get_attack() failed {e}")
            return
        #test attack of Charmander after level up
        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(f"Charmander could not be instantiated: {str(e)}.")
            return
        try:
            c.set_level(2)
            result = c.get_attack()
            if result != 8:
                self.verificationErrors.append(f"Charmander get_attack() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Charmander get_attack() failed {e}")
            return

    def test_char_get_defence(self):
        """test correctness of Charmander get_defence()"""
        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(f"Charmander could not be instantiated: {str(e)}.")
            return
        try:
            result = c.get_defence()
            if result != 4:
                self.verificationErrors.append(f"Charmander get_defence() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Charmander get_defence() failed {e}")
            return

    def test_char_get_speed(self):
        """test correctness of Charmander get_speed()"""
        #test speed of Charmander before level up
        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(f"Charmander could not be instantiated: {str(e)}.")
            return
        try:
            result = c.get_speed()
            if result != 8:
                self.verificationErrors.append(f"Charmander get_speed() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Charmander get_speed() failed {e}")
            return 
        #test speed of Charmander after level up
        try:
            c.set_level(2)
            result = c.get_speed()
            if result != 9:
                self.verificationErrors.append(f"Charmander get_speed() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Charmander get_speed() failed {e}")
            return

    def test_char_has_fought(self):
        """test correctness of Charmander has_fought()"""
        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(f"Charmander could not be instantiated: {str(e)}.")
            return
        try:
            b = Bulbasaur()
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur could not be instantiated: {str(e)}.")
            return
        try:
            c.attacked_by(b)
        except Exception as e:
            self.verificationErrors.append(f"Charmander attacked_by() method failed: {str(e)}.")
            return
        try:
            result = c.has_fought()
            if not result:
                self.verificationErrors.append(f"Charmander has_fought() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Charmander has_fought() failed {e}")
            return

    #test Bulbasaur
    def test_bulb_constr(self):
        """test correctness Bulbasaur constructor"""
        try:
            b = Bulbasaur()
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur could not be instantiated: {str(e)}.")
            return

        try:
            s = str(b)
            if s != "Bulbasaur's HP = 9 and level = 1":
                self.verificationErrors.append(f"Bulbasaur __init__() logic error: {s}")
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur __str__() method failed. {e}")
            return 

    def test_bulb_attacked_by(self):
        """test correctness of Bulbasaur attacked_by()"""
        #test the Bulbasaur's HP and level after being attacked by another Bulbasaur
        try:
            b1 = Bulbasaur()
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur1 could not be instantiated: {str(e)}.")
            return
        try:
            b2 = Bulbasaur()
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur2 could not be instantiated: {str(e)}.")
            return
        try:
            b1.attacked_by(b2)
            result = str(b1)
            if result != "Bulbasaur's HP = 7 and level = 1":
                self.verificationErrors.append(f"Bulbasaur attacked_by() Bulbasaur logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur attacked_by() Bulbasaur failed {e}")
            return
        #test the Bulbasaur's HP and level after being attacked by a Charmander
        try:
            b = Bulbasaur()
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur could not be instantiated: {str(e)}.")
            return
        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(f"Charmander could not be instantiated: {str(e)}.")
            return
        try:
            b.attacked_by(c)
            result = str(b)
            if result != "Bulbasaur's HP = -5 and level = 1":
                self.verificationErrors.append(f"Bulbasaur attacked_by() Charmander logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur attacked_by() Charmander failed {e}")
            return

    def test_bulb_get_attack(self):
        """test correctness of Bulbasaur get_attack()"""
        try:
            b = Bulbasaur()
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur could not be instantiated: {str(e)}.")
            return
        try:
            result = b.get_attack()
            if result != 5:
                self.verificationErrors.append(f"Bulbasaur get_attack() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur get_attack() failed {e}")
            return 

    def test_bulb_get_defence(self):
        """test correctness of Bulbasaur get_defence()"""
        try:
            b = Bulbasaur()
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur could not be instantiated: {str(e)}.")
            return
        try:
            result = b.get_defence()
            if result != 5:
                self.verificationErrors.append(f"Bulbasaur get_defence() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur get_defence() failed {e}")
            return

    def test_bulb_get_speed(self):
        """test correctness of Bulbasaur get_speed()"""
        #test whether the get_speed method returns the correct speed of Bulbasaur
        try:
            b = Bulbasaur()
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur could not be instantiated: {str(e)}.")
            return
        try:
            result = b.get_speed()
            if result != 7:
                self.verificationErrors.append(f"Bulbasaur get_speed() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur get_speed() failed {e}")
            return 
        
        #test whether the get_speed method returns the correct speed of Bulbasaur after leveling up
        try:
            b.set_level(2)
            result = b.get_speed()
            if result != 8:
                self.verificationErrors.append(f"Bulbasaur get_speed() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur get_speed() failed {e}")
            return

    def test_bulb_has_fought(self):
        """test correctness of Bulbasaur has_fought()"""
        try:
            b = Bulbasaur()
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur could not be instantiated: {str(e)}.")
            return
        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(f"Charmander could not be instantiated: {str(e)}.")
            return
        try:
            b.attacked_by(c)
        except Exception as e:
            self.verificationErrors.append(f"attacked_by method failed: {str(e)}.")
            return
        try:
            result = b.has_fought()
            if not result:
                self.verificationErrors.append(f"Bulbasaur has_fought() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur has_fought() failed {e}")
            return

    #test Squirtle
    def test_squirtle_constr(self):
        """test correctness of Squirtle constructor"""
        #test Squirtle constructor
        try:
            c = Squirtle()
        except Exception as e:
            self.verificationErrors.append(f"Squirtle could not be instantiated: {str(e)}.")
            return
        #test Squirtle __str__()
        try:
            s = str(c)
            if s != "Squirtle's HP = 8 and level = 1":
                self.verificationErrors.append(f"Squirtle __init__() logic error: {s}")
        except Exception as e:
            self.verificationErrors.append(f"Squirtle __str__() failed. {e}")
            return 

    def test_squir_attacked_by(self):
        """test correctness of Squirtle attacked_by()"""
        #test the Squirtle's HP and level after being attacked by another Squirtle
        try:
            s1 = Squirtle()
        except Exception as e:
            self.verificationErrors.append(f"Squirtle1 could not be instantiated: {str(e)}.")
            return
        try:
            s2 = Squirtle()
        except Exception as e:
            self.verificationErrors.append(f"Squirtle2 could not be instantiated: {str(e)}.")
            return
        try:
            s1.attacked_by(s2)
            result = str(s1)
            if result != "Squirtle's HP = 6 and level = 1":
                self.verificationErrors.append(f"Squirtle attacked_by() Squirtle logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Squirtle attacked_by() Squirtle failed {e}")
            return
        #test the Squirtle's HP and level after being attacked by Bulbasaur
        try:
            s = Squirtle()
        except Exception as e:
            self.verificationErrors.append(f"Squirtle could not be instantiated: {str(e)}.")
            return
        try:
            b = Bulbasaur()
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur could not be instantiated: {str(e)}.")
            return
        try:
            s.attacked_by(b)
            result = str(s)
            if result != "Squirtle's HP = 3 and level = 1":
                self.verificationErrors.append(f"Squirtle attacked_by() Bulbasaur logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Squirtle attacked_by() Bulbasaur failed {e}")
            return

    def test_squir_get_attack(self):
        """test correctness of Squirtle get_attack()"""
        #test whether the get_attack method returns the correct attack stat of Squirtle
        try:
            s = Squirtle()
        except Exception as e:
            self.verificationErrors.append(f"Squirtle could not be instantiated: {str(e)}.")
            return
        try:
            result = s.get_attack()
            if result != 4:
                self.verificationErrors.append(f"Squirtle get_attack() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Squirtle get_attack() failed {e}")
            return
        #test whether the get_attack method returns the correct attack stat of Squirtle after leveling up
        try:
            s = Squirtle()
        except Exception as e:
            self.verificationErrors.append(f"Squirtle could not be instantiated: {str(e)}.")
            return
        try:
            s.set_level(2)
            result = s.get_attack()
            if result != 5:
                self.verificationErrors.append(f"Squirtle get_attack() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Squirtle get_attack() failed {e}")
            return

    def test_squir_get_defence(self):
        """test correctness of Squirtle get_defence()"""
        #test whether the get_defence method returns the correct defence value of Squirtle
        try:
            s = Squirtle()
        except Exception as e:
            self.verificationErrors.append(f"Squirtle could not be instantiated: {str(e)}.")
            return
        try:
            result = s.get_defence()
            if result != 7:
                self.verificationErrors.append(f"Squirtle get_defence() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Squirtle get_defence() failed {e}")
            return 
        #test whether the get_defence method returns the correct defence value of Squirtle after leveling up
        try:
            s = Squirtle()
        except Exception as e:
            self.verificationErrors.append(f"Squirtle could not be instantiated: {str(e)}.")
            return
        try:
            s.set_level(2)
            result = s.get_defence()
            if result != 8:
                self.verificationErrors.append(f"Squirtle get_defence() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Squirtle get_defence() failed {e}")
            return

    def test_squir_get_speed(self):
        """test correctness of Squirtle get_speed()"""
        try:
            s = Squirtle()
        except Exception as e:
            self.verificationErrors.append(f"Squirtle could not be instantiated: {str(e)}.")
            return
        try:
            result = s.get_speed()
            if result != 7:
                self.verificationErrors.append(f"Squirtle get_speed() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Squirtle get_speed() failed {e}")
            return

    def test_squir_has_fought(self):
        """test correctness of Squirtle has_fought()"""
        try:
            s = Squirtle()
        except Exception as e:
            self.verificationErrors.append(f"Squirtle could not be instantiated: {str(e)}.")
            return
        try:
            b = Bulbasaur()
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur could not be instantiated: {str(e)}.")
            return
        try:
            s.attacked_by(b)
        except Exception as e:
            self.verificationErrors.append(f"attacked_by method failed: {str(e)}.")
            return
        try:
            result = s.has_fought()
            if not result:
                self.verificationErrors.append(f"Squirtle has_fought() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Squirtle has_fought() failed {e}")
            return

    #test GlitchMon

    def test_glitchmon_constr(self): 
        """test correctness of GlitchMon constructor"""
        try:
            m = MissingNo()
        except Exception as e:
            self.verificationErrors.append(f"MissingNo could not be instantiated: {str(e)}.")
            return
        try:
            GlitchMon.__init__(m, 18, "MissingNo")
            res = str(m)
            res_poke_type = m.get_type()
            if res != "MissingNo's HP = 18 and level = 1" or res_poke_type != None:
                self.verificationErrors.append(f"GlitchMon __init__() logic error: {res, res_poke_type}")
        except Exception as e:
            self.verificationErrors.append(f"GlitchMon __init__() failed {e}")
            return
    
    #test MissingNo
    def test_missingno_constr(self):
        """test correctness of MissingNo constructor"""
        #test whether MissingNo is instantiated successfully
        try:
            m = MissingNo()
        except Exception as e:
            self.verificationErrors.append(f"MissingNo could not be instantiated: {str(e)}.")
            return
        #test whether MissingNo object is printed correctly
        try:
            if str(m) != "MissingNo's HP = 8 and level = 1":
                self.verificationErrors.append(f"MissingNo __init__() logic error: {str(m)}")
        except Exception as e:
            self.verificationErrors.append(f"MissingNo __str__() failed. {e}")

    def test_missingno_get_attack(self):
        """test correctness of MissingNo get_attack()"""
        try:
            m = MissingNo()
        except Exception as e:
            self.verificationErrors.append(f"MissingNo could not be instantiated: {str(e)}.")
            return
        try:
            result = m.get_attack()
            if result != 16/3:
                self.verificationErrors.append(f"MissingNo get_attack() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"MissingNo get_attack() failed {e}")
            return

    def test_missingno_get_defence(self):
        """test correctness of MissingNo get_defence()"""
        try:
            m = MissingNo()
        except Exception as e:
            self.verificationErrors.append(f"MissingNo could not be instantiated: {str(e)}.")
            return
        try:
            result = m.get_defence()
            if result != 16/3:
                self.verificationErrors.append(f"MissingNo get_defence() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"MissingNo get_defence() failed {e}")
            return

    def test_missingno_get_speed(self):
        """test correctness of MissingNo get_speed()"""
        #test if the get_speed method returns the correct speed of MissingNo
        try:
            m = MissingNo()
        except Exception as e:
            self.verificationErrors.append(f"MissingNo could not be instantiated: {str(e)}.")
            return
        try:
            result = m.get_speed()
            if result != (22/3 +1 -1):
                self.verificationErrors.append(f"MissingNo get_speed() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"MissingNo get_speed() failed {e}")
            return 
        #test if the get_speed method returns the correct speed of MissingNo after leveling up
        try:
            m.set_level(2)
            result = m.get_speed()
            if result != 27/3:
                self.verificationErrors.append(f"MissingNo get_speed() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"MissingNo get_speed() failed {e}")
            return

    def test_missingno_attacked_by(self):
        """test correctness of MissingNo attack_by()"""
        seed(1)
        try:
            m = MissingNo()
        except Exception as e:
            self.verificationErrors.append(f"failed to instantiate MissingNo: {str(e)}.")
        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(f"failed to instantiate Charmander: {str(e)}.")
        try:
            m.attacked_by(c)
            if m.get_hp() != 1:
                self.verificationErrors.append(f"wrong MissingNo HP after calling attacked_by(): {str(m.get_hp())}")
            if m.get_level() != 1:
                self.verificationErrors.append(f"wrong MissingNo level after calling attacked_by(): {str(m.get_level())}")
        except Exception as e:
            self.verificationErrors.append(f": {str(e)}.")

    def test_missingno_has_fought(self):
        """test correctness of MissingNo has_fought()"""
        try:
            m = MissingNo()
        except Exception as e:
            self.verificationErrors.append(f"MissingNo could not be instantiated: {str(e)}.")
            return
        try:
            s = Squirtle()
        except Exception as e:
            self.verificationErrors.append(f"Squirtle could not be instantiated: {str(e)}.")
            return
        try:
            m.attacked_by(s)
        except Exception as e:
            self.verificationErrors.append(f"MissingNo attacked_by() method failed: {str(e)}.")
            return
        try:
            result = m.has_fought()
            if not result:
                self.verificationErrors.append(f"MissingNo has_fought() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"MissingNo has_fought() failed {e}")


    def test_missingno_superpower(self):
        seed(0)
        try:
            m = MissingNo()
        except Exception as e:
            self.verificationErrors.append(f"MissingNo could not be instantiated: {str(e)}.")
            return
        try:
            m.super_power()
            if m.get_hp() != 8:
                self.verificationErrors.append(f"wrong MissingNo HP after calling superpower(): {str(m.get_hp())}")
            if m.get_level() != 2:
                self.verificationErrors.append(f"wrong MissingNo level after calling super(): {str(m.get_level())}")
        except Exception as e:
            self.verificationErrors.append(f"MissingNo superpower() failed: {str(e)}.")
            return

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPokemon)
    unittest.TextTestRunner(verbosity=0).run(suite)