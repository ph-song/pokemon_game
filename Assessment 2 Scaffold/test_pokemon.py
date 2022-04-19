import unittest

from tester_base import TesterBase


class TestPokemon(TesterBase):
    def test_char_attacked(self):
        from pokemon import Charmander
        try:
            c1 = Charmander()
            c2 = Charmander()
            c2.attacked(c1)
            s1 = str(c1)
            if s1!= "Charmander's HP = 0 and level = 1":
                self.verificationErrors.append(f"attacked_by method did not calculate attack correctly: {s1}")
        except Exception as e:
            self.verificationErrors.append(f"attacked_by method failed. {e}")

    """
    def test_bulb_attacked_by():
        from pokemon import Bulbasaur
        pass

    def test_squi_attacked_by():
        from pokemon import Squirtle
        pass
    """

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPokemon)
    unittest.TextTestRunner(verbosity=0).run(suite)