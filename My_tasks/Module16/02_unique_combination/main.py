"""_Модуль_"""


def merge_sorted_lists(list1, list2):
    """Функция сортировки двух списков.

    Args:
        list1 (list): [list]
        list2 (list): [list]

    Returns:
        list: [list]
    """
    for i in list1:
        for j in list2:
            if i == j:
                list2.remove(j)
    _list_ = list1 + list2
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
    list1 = [1, 3, 5, 7, 9]
    list2 = [2, 4, 5, 6, 8, 10]
    merged = merge_sorted_lists(list1, list2)
    print(merged)


main()
