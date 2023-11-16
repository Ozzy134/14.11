from dataclasses import dataclass, field

@dataclass
class RetailItems:
    name: str
    discription: str
    kolvo: int
    price: float

    def __str__(self):
        return f'{self.name}, {self.discription}, {self.kolvo}, {self.price}'

@dataclass
class CashRegister:
    item_list: list = field(default_factory=list)

    def purchase_item(self, purches):
        self.item_list.append(purches)

    def get_total(self):
        total_summ = 0
        for i in self.item_list:
            total_summ += i.price
        return total_summ

    def show_items(self):
        for i in self.item_list:
            print(i)

    def clear_registr(self):
        self.item_list = ['fdfdfdf']

cashregistr = CashRegister()
item1 = RetailItems('fgfgfgf', 'fgfg', 312, 12.12)
item2 = RetailItems('fgfgfg', 'fgfgg', 12, 12.56)
item3 = RetailItems('hgfgd', 'fgfgf', 1, 12.78)
cashregistr.purchase_item(item3)
cashregistr.purchase_item(item2)
cashregistr.show_items()
print(f'total: {cashregistr.get_total()}')
cashregistr.clear_registr()
cashregistr.show_items()


