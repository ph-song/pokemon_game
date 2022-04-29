import unittest
from pokemon_base import PokemonBase
from tester_base import TesterBase
from pokemon import Bulbasaur, Squirtle, Charmander, MissingNo 


class TestPokemonBase(TesterBase):

    def test_pokemonbase_init(self): 
        """test PokeBase constructor"""
        try:
            b = Bulbasaur()
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur could not be instantiated: {str(e)}.")
            return
        try:
            PokemonBase.__init__(b, 10, "Grass")
            res = str(b)
            res_poke_type = b.get_type()
            if res != "Bulbasaur's HP = 10 and level = 1" or res_poke_type != "Grass":
                self.verificationErrors.append(f"PokemonBase __init__() logic error: {res, res_poke_type}")
        except Exception as e:
            self.verificationErrors.append(f"PokemonBase __init__() failed {e}")
            return
    
    def test_get_type(self):
        """test correctness of PokeBase get_type() method"""
        try:
            result = PokemonBase.get_type(Charmander())
            if result != "Fire":
                self.verificationErrors.append(f"Charmander get_type() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Charmander get_type() failed {e}")
            return

    def test_get_name(self):
        """test correctness of PokeBase get_name()"""
        try:
            result = PokemonBase.get_name(Bulbasaur())
            if result != "Bulbasaur":
                self.verificationErrors.append(f"Bulbasaur get_name() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur get_name() failed {e}")
            return

    def test_set_hp(self):
        """test correctness of PokeBase set_hp())"""
        try:
            s = Squirtle()
        except Exception as e:
            self.verificationErrors.append(f"Squirtle could not be instantiated: {str(e)}.")
            return
        try:
            PokemonBase.set_hp(s, 12)
            result = str(s)
            if result != "Squirtle's HP = 12 and level = 1":
                self.verificationErrors.append(f"Squirtle set_hp() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Squirtle set_hp() failed {e}")
            return

    def test_get_hp(self):
        """test correctness of PokeBase gett_hp()"""
        try:
            result = PokemonBase.get_hp(MissingNo())
            if result != 24/3:
                self.verificationErrors.append(f"MissingNo get_hp() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"MissingNo get_hp() failed {e}")
            return

    def test_set_level(self):
        """test correctness of PokeBase set_level()"""
        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(f"Charmander could not be instantiated: {str(e)}.")
            return
        try:
            PokemonBase.set_level(c, 3)
            result = str(c)
            if result != "Charmander's HP = 7 and level = 3":
                self.verificationErrors.append(f"Charmander set_level() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Charmander set_level() failed {e}")
            return

    def test_get_level(self):
        """test correctness of PokeBase get_level()"""
        try:
            result = PokemonBase.get_level(MissingNo())
            if result != 1:
                self.verificationErrors.append(f"MissingNo get_level() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"MissingNo get_level() failed {e}")
            return

    def test_is_fainted(self):
        """test correctness of PokeBase is_fainted()"""
        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(f"Charmander could not be instantiated: {str(e)}.")
            return
        try:
            c.set_hp(0)
            flag = PokemonBase.is_fainted(c)
            if flag != True:
                self.verificationErrors.append(f"Charmander is_fainted() logic error: {flag}")
        except Exception as e:
            self.verificationErrors.append(f"Charmander is_fainted() failed {e}")
            return

        try:
            b = Bulbasaur()
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur could not be instantiated: {str(e)}.")
            return
        try:
            flag = b.is_fainted()
            if flag != False:
                self.verificationErrors.append(f"Is_faint method did not return correct float: {flag}")
        except Exception as e:
            self.verificationErrors.append(f"Is_faint method failed. {e}")
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
            result = PokemonBase.damage_multiplier(c, b)
            if result != 2:
                self.verificationErrors.append(f"Charmander damage_multiplier() logic error: {result}")
        except Exception as e:
            self.verificationErrors.append(f"Charmander damage_multiplier() failed {e}")
            return



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPokemonBase)
    unittest.TextTestRunner(verbosity=0).run(suite)



