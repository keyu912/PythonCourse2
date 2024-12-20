

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

# TODO: написать класс Library
class Library:
    def __init__(self, books=None):
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self):
        if not self.books:
            return 1
        return self.books[-1].id_ + 1

    def get_index_by_book_id(self, book_id: int):
        for index, book in enumerate(self.books):
            if book.id_ == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")

if __name__ == '__main__':
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

    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    # Инициализируем библиотеку с книгами
    library_with_books = Library(books=list_books)
    print(library_with_books.get_next_book_id())  # Проверяем следующий id для непустой библиотеки

    # Проверяем индекс книги с id = 1
    print(library_with_books.get_index_by_book_id(1))

    # Проверяем индекс книги с id = 2
    print(library_with_books.get_index_by_book_id(2))

    # Проверяем индекс книги с несуществующим id
    try:
        print(library_with_books.get_index_by_book_id(3))
    except ValueError as e:
        print(e)  # Книги с запрашиваемым id не существует
