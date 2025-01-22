# TODO: описать базовый класс
class SocialNetwork:
    """
    Базовый класс для всех социальных сетей.

    Атрибуты:
    name : str
        Название социальной сети.
    users_count : int
        Количество пользователей.
    _messages_sent : int
        Количество отправленных сообщений (инкапсулированный атрибут).

    Методы:
    send_message(user: str, message: str) -> None:
        Отправляет сообщение пользователю.
    get_messages_sent() -> int:
        Возвращает количество отправленных сообщений.
    """

    def __init__(self, name: str, users_count: int, messages_sent: int = 0):
        """
        Инициализирует новый экземпляр класса SocialNetwork.

        Параметры:
        name : str
            Название социальной сети.
        users_count : int
            Количество пользователей.
        messages_sent : int
            Количество отправленных сообщений (по умолчанию 0).
        """
        self.name = name
        self.users_count = users_count
        self._messages_sent = messages_sent # Инкапсулированный атрибут, так как количество сообщений не должно изменяться напрямую

    def send_message(self, user: str, message: str) -> None:
        """
        Отправляет сообщение пользователю.

        Параметры:
        user : str
            Имя пользователя.
        message : str
            Сообщение.
        """
        if user and message:
            self._messages_sent += 1
            print(f"Сообщение отправлено {user}: {message}")

    def get_messages_sent(self) -> int:
        """
        Возвращает количество отправленных сообщений.

        Возвращает:
        int
            Количество отправленных сообщений.
        """
        return self._messages_sent

    def __str__(self) -> str:
        """
        Возвращает строковое представление социальной сети.

        Возвращает:
        str
            Строковое представление социальной сети.
        """
        return f"{self.name}, Пользователи: {self.users_count}, Сообщений отправлено: {self._messages_sent}"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление социальной сети.

        Возвращает:
        str
            Официальное строковое представление социальной сети.
        """
        return f"SocialNetwork(name={self.name!r}, users_count={self.users_count!r}, messages_sent={self._messages_sent!r})"
# TODO: описать дочерний класс
class Telegram(SocialNetwork):
    """
    Дочерний класс для социальной сети Telegram.

    Атрибуты:
    channels_count : int
        Количество каналов.

    Методы:
    create_channel(channel_name: str) -> None:
        Создает новый канал.
    """

    def __init__(self, users_count: int, channels_count: int, messages_sent: int = 0):
        """
        Инициализирует новый экземпляр класса Telegram.

        Параметры:
        users_count : int
            Количество пользователей.
        channels_count : int
            Количество каналов.
        messages_sent : int, optional
            Количество отправленных сообщений (по умолчанию 0).
        """
        super().__init__("Telegram", users_count, messages_sent)
        self.channels_count = channels_count

    def create_channel(self, channel_name: str) -> None:
        """
        Создает новый канал.

        Параметры:
        channel_name : str
            Название канала.
        """
        if channel_name:
            self.channels_count += 1
            print(f"Канал '{channel_name}' создан.")

    def send_message(self, user: str, message: str) -> None:
        """
        Отправляет сообщение пользователю.
        Перегруженный метод, чтобы добавить специфическую логику для Telegram.

        Параметры:
        user : str
            Имя пользователя.
        message : str
            Сообщение.
        """
        if user and message:
            self._messages_sent += 1
            print(f"Сообщение Telegram отправлено {user}: {message}")

    def __str__(self) -> str:
        """
        Возвращает строковое представление Telegram.

        Возвращает:
        str
            Строковое представление Telegram.
        """
        return (f"{self.name}, Пользователи: {self.users_count}, Сообщений отправлено: {self._messages_sent}, "
                f"Каналы: {self.channels_count}")

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление Telegram.

        Возвращает:
        str
            Официальное строковое представление Telegram.
        """
        return (f"Telegram(users_count={self.users_count!r}, channels_count={self.channels_count!r}, "
                f"messages_sent={self._messages_sent!r})")