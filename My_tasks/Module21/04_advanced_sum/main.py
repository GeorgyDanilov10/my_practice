"""Задача 4. Продвинутая функция sum """
list_1 = [[1, 2, [3]], [1], 3, [5, [5, [5, 5]]]]


def my_sum(*obj):
    """my_sum

    Returns:
        int: 12345
    """
    score = 0
    list_number = list(obj)
    for step in list_number:
        if isinstance(step, list):
            list_number.extend(step)
        else:
            score += step
    return score


def main():
    """main function
    """
    print(my_sum(1, 2, 3, 4, 5))
    print(my_sum(list_1))


main()
