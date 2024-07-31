"""_Модуль_"""


def fun_mus(_list_):
    """Функция считающая время всех песен

    Args:
        _list_ (list): [list]
    """
    sum_time = 0.0
    number_songs = int(input('Сколько песен выбрать? '))
    for total in range(1, number_songs + 1):
        print('Название ' + str(total) + '-й песни:', end=' ')
        answer = input('')
        for step1 in _list_:
            for step2 in step1:
                if answer == step2:
                    sum_time += step1[1]
    print('\nОбщее время звучания песен:', round(sum_time, 2), 'минуты')


def main():
    """
    Главная функция
    """
    violator_songs = [
        ['World in My Eyes', 4.86],
        ['Sweetest Perfection', 4.43],
        ['Personal Jesus', 4.56],
        ['Halo', 4.9],
        ['Waiting for the Night', 6.07],
        ['Enjoy the Silence', 4.20],
        ['Policy of Truth', 4.76],
        ['Blue Dress', 4.29],
        ['Clean', 5.83]
    ]
    fun_mus(violator_songs)


main()
