import unittest
from instrument import *

class Test(unittest.TestCase):
    #def test_isinstrument(self):
    #    test_instrument = Instrument('played', 'sound', 'timbre')
    #    self.assertTrue(test_instrument.played == 'played', 'These are not equal.')

    def instrument2(self):
        test_instrument = Instrument('played', 'sound', 'timbre')
        self.assertEqual(test_instrument.play_instrument(), 'Instruments are played played, produce a sound sound, and have a timbre timbre.')
        print(test_instrument.play_instrument())

if __name__ == '__main__':
    unittest.main()
   
   