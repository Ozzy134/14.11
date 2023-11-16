class Retailitem:

    def __init__(self, name, kolvo, price):
        self.name = name
        self.kolvo = kolvo
        self.price = price

    def __str__(self):
        return f'''
Описание: {self.name}
Количевсвто на складе: {self.kolvo}
Цена: {self.price}
'''

smot1 = Retailitem('Пиджак', '228', '339')
smot2 = Retailitem('Рубашка', '22', '39')
smot3 = Retailitem('Брюки', '128', '319')
print(smot1)
print(smot2)
print(smot3)