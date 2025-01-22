# TODO: импортируйте классы, созданные в ходе выполнения прошлого задания
from task_1 import Photo, Video, Audio


if __name__ == "__main__":
 # TODO: инстанцировать все описанные классы, создав три объекта.C()
    photo = Photo("Sunset", (1920, 1080), "JPEG")
    video = Video("Movie", 3600, "MP4")
    audio = Audio("Song", 300, "MP3")

    photo.resize(1280, 720)
    photo.convert_format("PNG")
    photo.get_info()

    video.trim(600, 1200)
    video.convert_format("AVI")
    video.get_info()

    audio.cut(30, 90)
    audio.convert_format("WAV")
    audio.get_info()

    try:
     # TODO: вызвать метод с некорректными аргументами(b)
        photo.resize(-1280, 720)  # Некорректная ширина
    except Exception:
        print('Ошибка: неправильные данные')

    try:
     # TODO: вызвать метод с некорректными аргументами(a)
        photo.convert_format(123)  # Некорректный формат
    except Exception:
        print('Ошибка: неправильные данные')

    try:
     # TODO: вызвать метод с некорректными аргументами(a)
        video.trim(1200, 600)
    except Exception:
        print('Ошибка: неправильные данные')

