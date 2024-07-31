"""Задача 1. Песни 2"""


def sum_time(diction, sum_):
    """sum_time

    Args:
        diction (dictionary): {dictionary}
        sum_ (int): number

    Returns:
        float: number
    """
    score = 0
    for step in range(1, 1 + sum_):
        print(f'Название {step} песни: ', end='')
        answer = str(input())
        score += diction.get(answer)
    return score


def main():
    """main function
    """
    sum_music = int(input('Сколько песен выбрать? '))
    violator_songs = {
        'World in My Eyes': 4.86,
        'Sweetest Perfection': 4.43,
        'Personal Jesus': 4.56,
        'Halo': 4.9,
        'Waiting for the Night': 6.07,
        'Enjoy the Silence': 4.20,
        'Policy of Truth': 4.76,
        'Blue Dress': 4.29,
        'Clean': 5.83
    }
    print('Общее время звучания песен:', round(
        sum_time(violator_songs, sum_music), 2))


main()
