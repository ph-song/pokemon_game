import unittest
from pokemon_base import PokemonBase
from tester_base import TesterBase
from pokemon import Bulbasaur, Squirtle, Charmander, MissingNo 


class TestPokemonBase(TesterBase):

    def test_pokemonbase_constr_str(self): 
        """test PokeBase constructor and __str__()"""
        try:
            b = Bulbasaur()
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur could not be instantiated: {str(e)}.")
            return
        try:
            PokemonBase.__init__(b, 10, "Grass")
            if b.hp != 10 or b.poke_type != "Grass":
                self.verificationErrors.append(f"PokemonBase __init__() logic error: hp={b.hp}, poke_type={b.poke_type}")
        except Exception as e:
            self.verificationErrors.append(f"PokemonBase __init__() failed: {str(e)}.")
        try:
            res = str(b)
            if res != "Bulbasaur's HP = 10 and level = 1":
                self.verificationErrors.append(f"PokemonBase __str__() logic error: {res, b.poke_type}")
        except Exception as e:
            self.verificationErrors.append(f"PokemonBase __str__() failed: {str(e)}.")
    
    def test_get_type(self):
        """test correctness of PokeBase get_type() method"""
        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(f"Charmander could not be instantiated: {str(e)}.")
        try:
            result = PokemonBase.get_type(c)
            if result != "Fire":
                self.verificationErrors.append(f"Charmander get_type() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Charmander get_type() failed {e}")
            return

    def test_get_name(self):
        """test correctness of PokeBase get_name()"""
        try:
            b = Bulbasaur()
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur could not be instantiated: {str(e)}.")
            return
        try:
            result = PokemonBase.get_name(b)
            if result != "Bulbasaur":
                self.verificationErrors.append(f"PokeBase get_name() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"PokeBase get_name() failed {e}")

    def test_set_hp(self):
        """test correctness of PokemonBase set_hp())"""
        try:
            s = Squirtle()
        except Exception as e:
            self.verificationErrors.append(f"Squirtle could not be instantiated: {str(e)}.")
            return
        try:
            PokemonBase.set_hp(s, 12)
            result = str(s)
            if result != "Squirtle's HP = 12 and level = 1":
                self.verificationErrors.append(f"PokemonBase set_hp() logic error: {result}")
                return
        except Exception as e:
            self.verificationErrors.append(f"PokemonBase set_hp() failed {e}")

    def test_get_hp(self):
        """test correctness of PokemonBase gett_hp()"""
        try:
            result = PokemonBase.get_hp(MissingNo())
            if result != 24/3:
                self.verificationErrors.append(f"PokemonBase get_hp() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"PokemonBase get_hp() failed {e}")
            return

    def test_set_level(self):
        """test correctness of PokemonBase set_level()"""
        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(f"Charmander could not be instantiated: {str(e)}.")
            return
        try:
            PokemonBase.set_level(c, 3)
            result = str(c)
            if result != "Charmander's HP = 7 and level = 3":
                self.verificationErrors.append(f"PokemonBase set_level() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"PokemonBase set_level() failed {e}")

    def test_get_level(self):
        """test correctness of PokemonBase get_level()"""
        try:
            result = PokemonBase.get_level(MissingNo())
            if result != 1:
                self.verificationErrors.append(f"PokemonBase get_level() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"PokemonBase get_level() failed {e}")
            return

    def test_is_fainted(self):
        """test correctness of PokemonBase is_fainted()"""
        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(f"Charmander could not be instantiated: {str(e)}.")
            return
        try:
            c.set_hp(0)
        except Exception as e:
            self.verificationErrors.append(f"Charmander set_hp() failed {e}")
        try:
            flag = PokemonBase.is_fainted(c)
            if flag != True:
                self.verificationErrors.append(f"PokemonBase is_fainted() logic error: {flag}")
        except Exception as e:
            self.verificationErrors.append(f"PokemonBase is_fainted() failed {e}")
            return

        try:
            b = Bulbasaur()
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur could not be instantiated: {str(e)}.")
            return
        try:
            flag = b.is_fainted()
            if flag != False:
                self.verificationErrors.append(f"PokemonBase is_faint() logic error: {flag}")
        except Exception as e:
            self.verificationErrors.append(f"PokemonBase is_faint() failed. {e}")
            return 

    def test_damage_multiplier(self):
        """ttest correctness of PokeBase damage_multiplier()"""
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
            result = c.damage_multiplier(b)
            if result != 2:
                self.verificationErrors.append(f"PokemonBase damage_multiplier() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"PokemonBase damage_multiplier() failed {e}")
            return



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPokemonBase)
    unittest.TextTestRunner(verbosity=0).run(suite)



