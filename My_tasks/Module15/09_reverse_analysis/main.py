"""Нет модуля"""


numbers_list = [7, 14, 3, 18, 21, 10, 9, 2, 3, 4, 6]


def sort_list(_list_):
    """
    Функция, сортирует список, удаляет нечетные числа и пишит четные числа в обратном порядке.
    """
    for step in range(len(_list_), 0, -1):
        if _list_[step * -1] % 2 == 1:
            _list_.remove(_list_[step * -1])
    for step in range(int(len(_list_)/2)):
        save = _list_[step]
        _list_[step] = _list_[len(_list_) - step - 1]
        _list_[len(_list_) - step - 1] = save
    return _list_


def main():
    """
    Главная функция
    """
    print(numbers_list)
    print(sort_list(numbers_list))


main()
