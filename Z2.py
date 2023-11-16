class Book:

    def __init__(self, title, namea, namei):
        self.title = title
        self.namea = namea
        self.namei = namei

    def get_title(self):
        return self.title

    def get_namea(self):
        return self.namea

    def get_namei(self):
        return self.namei

    def set_title(self, title):
        self.title = title

    def set_namea(self, namea):
        self.namea = namea

    def set_namei(self, namei):
        self.namei = namei

    def __str__(self):
        return f'Заголовок: {self.title}, Имя автора: {self.namea}, Имя издателя: {self.namei}'

book1 = Book('Азбука', 'Я', '1')
print(book1.get_title())
print(book1.set_namei(2))
print(book1.__str__())