"""Задача 5. Список списков 2"""


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


def straightening_the_list(list1):
    """straightening_the_list

    Args:
        list1 (list):[ _description_]

    Returns:
        obj: obj
    """
    if isinstance(list1, int):
        return list1
    return [straightening_the_list(item) for item in list1]


def sort_list(nice_list2):
    """sort_list

    Args:
        nice_list2 (list): [_description_]

    Returns:
        list: [_description_]
    """
    flag = True
    for step in nice_list2.copy():
        if isinstance(step, list):
            nice_list2.extend(straightening_the_list(step))
            nice_list2.remove(step)
            flag = False
    if flag:
        return nice_list2
    return sort_list(nice_list2)


def main():
    """main function
    """
    print(sort_list(nice_list))


main()
