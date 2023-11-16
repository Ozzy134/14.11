from dataclasses import dataclass, field

@dataclass

class Patiend:

    adress: str
    town: str
    obl: str
    mail_index: str
    num: list = field(default_factory=list)
    fio: list = field(default_factory=list)
    procedures: list = field(default_factory=list)

    def get_fio(self):
        return self.fio

    def get_adress(self):
        return self.adress

    def get_town(self):
        return self.town

    def get_obl(self):
        return self.obl

    def get_mailindex(self):
        return self.mail_index

    def get_num(self):
        return self.num

    def get_ext_num(self):
        return self.ext_num

    def get_procidures(self):
        return self.procedures

    def set_fio(self, fio):
        self.fio = fio

    def set_adress(self, adress):
        self.adress = adress

    def set_town(self, town):
        self.town = town

    def set_obl(self, obl):
        self.obl = obl

    def set_mailindex(self, mail_index):
        self.mail_index = mail_index

    def set_num(self, num):
        self.num = num

    def set_procidures(self, procidures):
        self.procedures = procidures

    def __repr__(self):
        return f'{self.fio}, {self.adress}, {self.town}, {self.obl}, {self.mail_index}, {self.num}'

class Procedure:
    name: str
    data: str
    doctor: str
    price: float

    def get_name(self):
        return self.name

    def get_data(self):
        return self.data

    def get_doctor(self):
        return self.doctor

    def get_price(self):
        return self.price

    def set_name(self, name):
        self.name = name

    def set_data(self, data):
        self.data = data

    def set_doctor(self, doctor):
        self.doctor = doctor

    def set_price(self, price):
        self.price = price

    def __str__(self):
        return f'Название процедуры: {self.name}, дата проведения: {self.data}, лечущий врач: {self.doctor}, стоимость: {self.price}'

    def __repr__(self):
        return f'{self.fio}, {self.adress}, {self.town}, {self.obl}, {self.mail_index}, {self.num}'

a1 = Patiend('Shiskino', 'Elabuga', 'Tatarstan', 'G331H14', ['88005553535'], ['Nazarov', 'Nazar', 'Michailovich'])
print(a1)
p1 = Procedure('Осмотр', 'Сегодня', 'Ашот', 250)
p2 = Procedure('Принятие', 'Завтра', 'Наташа', 550)
p3 = Procedure('Вырезание', 'Сегодня', 'Леха', 850)
a1.procedures = [p1, p2, p3]
a1.get_procidures()