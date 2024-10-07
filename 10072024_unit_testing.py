import unittest
from instrument import *

class Test(unittest.TestCase):
    def test_isinstrument(self):
        test_instrument = Instrument('played', 'sound', 'timbre')
        self.assertTrue(test_instrument.played == 'played', 'These are not equal.')

    def test_instrument2(self):
        test_instrument = Instrument('played', 'sound', 'timbre')
        self.assertEqual(type(test_instrument.play_instrument()), type('Instruments are played played, produce a sound sound, and have a timbre timbre.'))
        print(test_instrument.play_instrument())

if __name__ == '__main__':
    unittest.main()
   
   