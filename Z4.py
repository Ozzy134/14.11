class Car:

    def __init__(self, _year_model, rttake):
        self._year_model = _year_model
        self.rttake = rttake
        self._speed = 0

    def acelerate(self):
        self._speed += 5
        print(f'Скорость автомобиля: {self._speed}')

    def brake(self):
        self._speed -= 5
        print(f'Скорость автомобиля: {self._speed}')

    def get_speed(self):
        return self._speed

car1 = Car(2008, '1')
for i in range(5):
    car1.acelerate()
    car1.brake()

print(car1.get_speed())
