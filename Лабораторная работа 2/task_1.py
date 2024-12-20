


# TODO: написать класс Book
class Book:
    def __init__(self, id_: int, name: str, pages: int):
        if not isinstance(id_, int) or id_ <= 0:
            raise ValueError("Идентификатор книги должен быть положительным целым числом")
        if not isinstance(name, str):
            raise TypeError("Название книги должно быть строкой")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом")

        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f"Book(id_={self.id_}, name='{self.name}', pages={self.pages})"

if __name__ == '__main__':
    # инициализируем список книг
    BOOKS_DATABASE = [
        {
            "id": 1,
            "name": "test_name_1",
            "pages": 200,
        },
        {
            "id": 2,
            "name": "test_name_2",
            "pages": 400,
        }
    ]
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]

    # Проверяем метод __str__
    for book in list_books:
        print(book)

    # Проверяем метод __repr__
    print(list_books)