class Instrument():
    def __init__(self, played, sound, timbre):
        self.played = played
        self.sound = sound
        self.timbre = timbre

    def play_instrument(self):
        return f'Instruments are played {self.played}, produce a {self.sound} sound, and have a {self.timbre} timbre.'








if __name__ == '__main__':
    print("Hello world")
    test_intrument = Instrument('loudly', 'melodious', 'different')
    print(test_intrument.play_instrument())
    




