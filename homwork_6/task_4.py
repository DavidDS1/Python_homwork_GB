#задание 4
class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go (self):
        print(f'Машина начала движение')
    def stop (self):
        print(f'Машина остановилась')
    def show_speed (self):
        print(f'Скорость автомобиля {self.speed} км/ч')
    def turn (self, direction):
        self.direction =direction
        print(f'Машина повернула {self.direction}')

class TownCar(Car):
    def show_speed (self):
        if self.speed>60:
            print(f'Ваш автомобиль превысил максимально-допустимую скорость км/ч')
        else:
            print(f'Скорость автомобиля {self.speed} км/ч')
class SportCar (Car):
    pass
class WorkCar (Car):
    def show_speed (self):
        if self.speed>40:
            print(f'Ваш автомобиль превысил максимально-допустимую скорость км/ч')
        else:
            print(f'Скорость автомобиля {self.speed} км/ч')

townCar = TownCar(80, 'red', 'mazda', True)
print(townCar.color)
print(townCar.name)
print(townCar.speed)
townCar.go()
townCar.stop()
townCar.turn('направо')
townCar.show_speed()
sportcar = SportCar(300, 'black', 'BMW', True)
print(sportcar.color)
print(sportcar.name)
print(sportcar.speed)
sportcar.go()
sportcar.stop()
sportcar.turn('налево')
sportcar.show_speed()

workcar = WorkCar(40, 'green', 'Matiz', True)
print(workcar.color)
print(workcar.name)
print(workcar.speed)
workcar.go()
workcar.stop()
workcar.turn('прямо')
workcar.show_speed()



