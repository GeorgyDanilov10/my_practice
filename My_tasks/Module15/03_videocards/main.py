"""Нет модуля"""

def new_list_video_card(_list_,sum1):
    """
    Функция, печатающая новый список видеокард.
    """
    max_sum = max(_list_)
    new_list_ = []
    for step in range(sum1):
        if max_sum != _list_[step]:
            new_list_.append(_list_[step])
    return new_list_


def video_cards_list(sum1):
    """
    Функция, печатающая старый список видеокард.
    """
    video_card_list = []
    for step in range(1, sum1 + 1):
        print(step,'Видеокарта: ', end = '')
        number = int(input())
        video_card_list.append(number)
    return video_card_list


def main():
    """
    Главная функция
    """
    sum2 = int(input('Количество видеокарт:'))
    print('Старый список видеокарт:', list1 := video_cards_list(sum2))
    print('Новый список видеокарт:', new_list_video_card(list1, sum2))


main()
# Конец файла
