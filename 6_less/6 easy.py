class Car:
    def __init__(self, speed, color, name, police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.police = police

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}')


class TownCar(Car):
    def go(self):
        print(f'Машина {self.name} поехала со скоростью {self.speed} км/час')


class SportCar(Car):
    pass


class WorkCar(Car):
    pass


class PoliceCar(Car):
    pass


car1 = SportCar('160', 'Red', 'Lamborghini')
car2 = TownCar('60', 'Blue', 'Toyota')
car3 = WorkCar('60', 'Yellow', 'Ford')
car4 = PoliceCar('120', 'White', 'Chevrolet', True)

car1.go()
car3.stop()
car4.turn('налево')
car2.go()
