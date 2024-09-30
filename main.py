class Car:
    def __init__(self, wheels, color):
        self.wheels = wheels
        self.color = color



if __name__ == '__main__':
    test_car = Car(4, 'red')
    print(f'This car has {test_car.wheels} wheels')
    

