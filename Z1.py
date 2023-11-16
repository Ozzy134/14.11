class Car:

    def __init__(self, name, speed, price):
        self.name = name
        self.speed = speed
        self.price = price

    def go(self):
        print('Дана машина:')
        print(f'Модель: {self.name}')
        print(f'Максимальная скорость: {self.speed}')
        print(f'Стоимость: {self.price}')

my_car = Car('ВАЗ-2107', 'Бесконечно', 'Безценно')
my_car.go()