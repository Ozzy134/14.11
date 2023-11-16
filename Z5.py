class information:

    def __init__(self, name, adress, age, phone):
        self.name = name
        self.adress = adress
        self.age = age
        self.phone = phone

    def get_name(self):
        return self.name

    def get_adress(self):
        return self.adress

    def get_age(self):
        return self.age

    def get_phone(self):
        return self.phone

    def set_name(self, name):
        self.name = name

    def set_adress(self, adress):
        self.adress = adress

    def set_age(self, age):
        self.age = age

    def set_phone(self, phone):
        self.phone = phone

PI = information('1', '2', '3', '2323')
PI1 = information('1', '2', '3', '2323')
PI2 = information('1', '2', '3', '2323')

