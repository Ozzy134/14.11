class Employee:

    def __init__(self, name, number, otdel, dol):
        self.name = name
        self.number = number
        self.otdel = otdel
        self.dol = dol

    def __str__(self):
        return f'ФИО: {self.name}, идинтификационный номер: {self.number}, отдел: {self.otdel}, должность: {self.dol}'

pers1 = Employee('Иванов Иван Иванович', '1231245', 'ССР', 'Переворачиватель коров')
pers2 = Employee('Иванов Сергей Алексеевич', '1231969', 'ССР', 'Просиживатель штанов')
pers3 = Employee('Бобиков Мухтар Алексеевич', '228229', 'ССР', 'Продавец плана')
print(pers1)
print(pers2)
print(pers3)