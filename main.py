class Car:
    def __init__(self, wheels, color):
        self.wheels = wheels
        self.color = color

    def summary(self):
        return f'This car has {test_car.wheels} wheels'


class Mfg(Car):
    def __init__(self, wheels, color, name):
        super().__init__(wheels, color)
        self.name = name





if __name__ == '__main__':
    test_car = Car(4, 'red')
    print(test_car.summary())
    test_mfg = Mfg(4, 'green', 'Ford')
    print(f'This car was made by {test_mfg.name} and is the color {test_mfg.color}.')
    print(test_mfg.summary())






