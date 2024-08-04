"""Задача 6. Быстрая сортировка"""


def sort_list_met_haon(list_1):
    """sort_list_met_haon

    Args:
        list_1 (list): [_description_]

    Returns:
        list: [_description_]
    """
    if len(list_1) <= 1:
        return list_1
    list_num_1 = [step for step in list_1 if step < list_1[-1]]
    list_num_2 = [step for step in list_1 if step == list_1[-1]]
    list_num_3 = [step for step in list_1 if step > list_1[-1]]
    result = sort_list_met_haon(list_num_1) + \
        list_num_2 + sort_list_met_haon(list_num_3)
    return result


def main():
    """main function
    """
    number_list = [5, 8, 9, 4, 2, 9, 1, 8]
    print(sort_list_met_haon(number_list))


main()
