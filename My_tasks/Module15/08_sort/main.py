"""Нет модуля"""


def sort_list(_list_):
    """
    Функция, делает список упорядоченным по.
    """
    sum_list = len(_list_)
    for i in range(sum_list):
        for j in range(i + 1, sum_list):
            if _list_[i] > _list_[j]:
                _list_[i], _list_[j] = _list_[j], _list_[i]
    return _list_


def main():
    """
    Главная функция
    """
    number_list = [1, 4, -3, 0, 10]
    print('Изначальный список:', number_list)
    print('Отсортированный список:', sort_list(number_list))


main()
