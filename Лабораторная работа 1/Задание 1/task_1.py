# TODO: Подробно описать три произвольных класса


# TODO: описать класс
class Photo:
    def __init__(self, title: str, resolution: tuple[int, int], format: str):
        if not isinstance(title, str):
            raise TypeError("Название должно быть строкой")
        if not isinstance(resolution, tuple) or len(resolution) != 2 or not all(isinstance(i, int) and i > 0 for i in resolution):
            raise ValueError("Разрешение должно быть кортежем из двух положительных целых чисел")
        if not isinstance(format, str):
            raise TypeError("Формат должен быть строкой")

        self.title = title
        self.resolution = resolution
        self.format = format

    def resize(self, new_width: int, new_height: int) -> str:
        """
        Изменяет разрешение фотографии.

        Аргументы:
            new_width (int): Новая ширина фотографии в пикселях.
            new_height (int): Новая высота фотографии в пикселях.

        Возвращаемое значение:
            str: Сообщение о новом разрешении фотографии.

        Исключения:
            ValueError: Если new_width или new_height не являются положительными целыми числами.

        Примеры:
            >>> photo = Photo("Sunset", (1920, 1080), "JPEG")
            >>> photo.resize(1280, 720)
            'Фотография изменена до разрешения (1280, 720)'
        """
        if not isinstance(new_width, int) or new_width <= 0:
            raise ValueError("Новая ширина должна быть положительным целым числом")
        if not isinstance(new_height, int) or new_height <= 0:
            raise ValueError("Новая высота должна быть положительным целым числом")
        self.resolution = (new_width, new_height)
        return f"Фотография изменена до разрешения {self.resolution}"

    def convert_format(self, new_format: str) -> str:
        """
        Изменяет формат фотографии.

        Аргументы:
            new_format (str): Новый формат файла фотографии.

        Возвращаемое значение:
            str: Сообщение о новом формате фотографии.

        Исключения:
            TypeError: Если new_format не является строкой.

        Примеры:
            >>> photo = Photo("Sunset", (1920, 1080), "JPEG")
            >>> photo.convert_format("PNG")
            'Формат фотографии изменен на PNG'
        """
        if not isinstance(new_format, str):
            raise TypeError("Новый формат должен быть строкой")
        self.format = new_format
        return f"Формат фотографии изменен на {self.format}"

    def get_info(self) -> str:
        """
        Возвращает информацию о фотографии.

        Возвращаемое значение:
            str: Информация о фотографии, включающая название, разрешение и формат.

        Примеры:
            >>> photo = Photo("Sunset", (1920, 1080), "JPEG")
            >>> photo.get_info()
            'Название: Sunset, Разрешение: (1920, 1080), Формат: JPEG'
        """
        return f"Название: {self.title}, Разрешение: {self.resolution}, Формат: {self.format}"

# TODO: описать ещё класс
class Video:
    def __init__(self, title: str, duration: int, format: str):
        if not isinstance(title, str):
            raise TypeError("Название должно быть строкой")
        if not isinstance(duration, int) or duration <= 0:
            raise ValueError("Длительность должна быть положительным целым числом")
        if not isinstance(format, str):
            raise TypeError("Формат должен быть строкой")

        self.title = title
        self.duration = duration
        self.format = format

    def trim(self, start: int, end: int) -> str:
        """
        Обрезка видео от начала до конца.

        Аргументы:
            start (int): Начальная точка обрезки в секундах.
            end (int): Конечная точка обрезки в секундах.

        Возвращаемое значение:
            str: Сообщение о новой длительности видео.

        Исключения:
            ValueError: Если start или end не являются положительными целыми числами, или если start не меньше end.

        Примеры:
            >>> video = Video("Movie", 3600, "MP4")
            >>> video.trim(600, 1200)
            'Видео обрезано до 600 секунд'
        """
        if not isinstance(start, int) or start < 0:
            raise ValueError("Начало должно быть положительным целым числом")
        if not isinstance(end, int) or end < 0:
            raise ValueError("Конец должен быть положительным целым числом")
        if start >= end:
            raise ValueError("Начало должно быть меньше конца")
        self.duration = end - start
        return f"Видео обрезано до {self.duration} секунд"

    def convert_format(self, new_format: str) -> str:
        """
        Изменяет формат видео.

        Аргументы:
            new_format (str): Новый формат файла видео.

        Возвращаемое значение:
            str: Сообщение о новом формате видео.

        Исключения:
            TypeError: Если new_format не является строкой.

        Примеры:
            >>> video = Video("Movie", 3600, "MP4")
            >>> video.convert_format("AVI")
            'Формат видео изменен на AVI'
        """
        if not isinstance(new_format, str):
            raise TypeError("Новый формат должен быть строкой")
        self.format = new_format
        return f"Формат видео изменен на {self.format}"

    def get_info(self) -> str:
        """
        Возвращает информацию о видео.

        Возвращаемое значение:
            str: Информация о видео, включающая название, длительность и формат.

        Примеры:
            >>> video = Video("Movie", 3600, "MP4")
            >>> video.get_info()
            'Название: Movie, Длительность: 3600 секунд, Формат: MP4'
        """
        return f"Название: {self.title}, Длительность: {self.duration} секунд, Формат: {self.format}"
# TODO: и ещё один
class Audio:
    def __init__(self, title: str, duration: int, format: str):
        if not isinstance(title, str):
            raise TypeError("Название должно быть строкой")
        if not isinstance(duration, int) or duration <= 0:
            raise ValueError("Длительность должна быть положительным целым числом")
        if not isinstance(format, str):
            raise TypeError("Формат должен быть строкой")

        self.title = title
        self.duration = duration
        self.format = format

    def cut(self, start: int, end: int) -> str:
        """
        Обрезка аудиофайла от начала до конца.

        Аргументы:
            start (int): Начальная точка обрезки в секундах.
            end (int): Конечная точка обрезки в секундах.

        Возвращаемое значение:
            str: Сообщение о новой длительности аудиофайла.

        Исключения:
            ValueError: Если start или end не являются положительными целыми числами, или если start не меньше end.

        Примеры:
            >>> audio = Audio("Song", 300, "MP3")
            >>> audio.cut(30, 90)
            'Аудио обрезано до 60 секунд'
        """
        if not isinstance(start, int) or start < 0:
            raise ValueError("Начало должно быть положительным целым числом")
        if not isinstance(end, int) or end < 0:
            raise ValueError("Конец должен быть положительным целым числом")
        if start >= end:
            raise ValueError("Начало должно быть меньше конца")
        self.duration = end - start
        return f"Аудио обрезано до {self.duration} секунд"

    def convert_format(self, new_format: str) -> str:
        """
        Изменяет формат аудиофайла.

        Аргументы:
            new_format (str): Новый формат файла аудио.

        Возвращаемое значение:
            str: Сообщение о новом формате аудиофайла.

        Исключения:
            TypeError: Если new_format не является строкой.

        Примеры:
            >>> audio = Audio("Song", 300, "MP3")
            >>> audio.convert_format("WAV")
            'Формат аудио изменен на WAV'
        """
        if not isinstance(new_format, str):
            raise TypeError("Новый формат должен быть строкой")
        self.format = new_format
        return f"Формат аудио изменен на {self.format}"

    def get_info(self) -> str:
        """
        Возвращает информацию о аудиофайле.

        Возвращаемое значение:
            str: Информация о аудиофайле, включающая название, длительность и формат.

        Примеры:
            >>> audio = Audio("Song", 300, "MP3")
            >>> audio.get_info()
            'Название: Song, Длительность: 300 секунд, Формат: MP3'
        """
        return f"Название: {self.title}, Длительность: {self.duration} секунд, Формат: {self.format}"
