"""Нет модуля"""

films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']


def favorite_films(sum1):
    """
    Функция, печатающая список любимых фильмов, которые есть в списке films.
    """
    favorite_films1 = []
    for _ in range(sum1):
        film = str(input('Введите название фильма: '))
        if film in films:
            favorite_films1.append(film)
        else:
            print('Ошибка: фильма ' + film + ' у нас нет :(')
    return favorite_films1


def main():
    """
    Главная функция
    """
    sum_films = int(input('Сколько фильмов хотите добавить? '))
    print('Ваш список любимых фильмов:', favorite_films(sum_films))


main()
# Конец файла
