class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}"

print(Book("Самый богатый человек в Вавилоне", "Джордж Самюэль", 1926).get_info())

