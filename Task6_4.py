"""
4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} сворачивает вправо'

    def turn_left(self):
        return f'{self.name} сворачивает влево'

    def show_speed(self):
        return f'Ограничение скорости {self.name} {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Ограничение скорости машины в городе {self.name} {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} слишком большая для городской машины'
        else:
            return f'Скорость {self.name} нормальная для городской машины'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Cкорость {self.name} - {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} большая для рабочей машины'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} полицейская машина'
        else:
            return f'{self.name} не полицейская машина'


aston_martin = SportCar(100, 'Black', 'Астон', False)
mazda = TownCar(30, 'White', 'Машка', False)
renault = WorkCar(70, 'Red', 'Рено', False)
ford = PoliceCar(110, 'Blue', 'Форд', True)
print(ford.police())
print(f'Когда {mazda.turn_right()}, - {ford.turn_left()}')
print(f'{ford.name} {renault.color}')
print(f'{renault.show_speed()}')
print(f'{aston_martin.name} полицейская машина? {aston_martin.is_police}')
print(f'{renault.name} полицейская машина? {renault.is_police}')
print(aston_martin.show_speed())
print(mazda.show_speed())
print(ford.show_speed())
