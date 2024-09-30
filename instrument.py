class Instrument():
    def __init__(self, played, sound, timbre):
        self.played = played
        self.sound = sound
        self.timbre = timbre

    def play_instrument(self):
        return f'Instruments are played {self.played}, produce a {self.sound} sound, and have a {self.timbre} timbre.'

class Violin(Instrument):
    def __init__(self, played, sound, timbre, bowed):
        super().__init__(played, sound, timbre)
        self.bowed = bowed

    def play_violin(self):
        return f'Violins can be played {self.played}, can sound {self.sound}, have a mellow {self.timbre} are usually {self.bowed}.'
    
class Guitar(Instrument):
    def __init__(self, played, sound, timbre, picked):
        super().__init__(played, sound, timbre)
        self.picked = picked

    def play_guitar(self):
        return f'Guitars can be played {self.played}, can sound {self.sound}, have a {self.timbre} timbre are usually {self.picked}.'




if __name__ == '__main__':
    print("Hello world")
    test_intrument = Instrument('loudly', 'melodious', 'different')
    print(test_intrument.play_instrument())
    test_violin = Violin('loudly', 'melodious', 'different', 'bowed')
    print(test_violin.play_violin())
    test_guitar = Guitar('loudly', 'dissonant', 'harsh', 'picked')
    print(test_guitar.play_guitar())




