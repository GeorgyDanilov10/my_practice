"""Нет модуля"""


def shift_list(_list_, shift_number):
    """
    Функция, сдвигает список на определенное количество позиций.
    """
    new_list = []
    for step in range(0, len(_list_)):
        new_list.append(_list_[step - shift_number])
    return new_list


def main():
    """
    Главная функция
    """
    shift_number = int(input('Насколько позиций нужно сдвинуть список? '))
    _list_ = [1, 2, 3, 4, 5]
    print('Сдвиг:', shift_number)
    print('Изначальный список:', _list_)
    print('Сдвинутый список:', shift_list(_list_, shift_number))


main()
