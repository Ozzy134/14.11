class Employee:

    def __init__(self, name, number_id, office, work):
        self.name = name
        self.number_id = number_id
        self.office = office
        self.work = work

    def set_name(self, name):
        self.name = name

    def set_office(self, office):
        self.office = office

    def set_work(self, work):
        self.work = work

    def __str__(self):
        return f'{self.name}, {self.number_id}, {self.office}, {self.work}'

def e_list(key, value, dict):
    dict[key] = value
    return dict

def e_search(dict, name, counter):
    res = {}
    for key in dict:
        if name == dict[key].name:
            print(dict[key])
    if res:
        print(dict[key])
    else:
        print('no')

def e_change(name, office, work, Emp):
    Emp.set_name(name)
    Emp.set_office(office)
    Emp.set_work(work)

def e_delete(key, dict):
    del dict[key]

counter = 0
reestr = {}
a1 = Employee('1', '2', '3', '4')
e_list(counter, a1, reestr)
counter += 1
a2 = Employee('3', '4', '65', '9')
e_list(counter, a2, reestr)
counter += 2
a3 = Employee('2', '9', '0', '3')
e_list(counter, a3, reestr)

e_search(reestr, '2', counter)
e_change('dfdf', '2332', 'sfsfdf', reestr[0])
print(reestr[0])
e_delete(0, reestr)
print(reestr[1])
