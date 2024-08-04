"""Задача 2. Универсальная программа 2"""


def is_prime(number):
    """is_prime

    Args:
        number (int): _description_

    Returns:
        bool: _description_
    """
    return bool(number > 4 and number % 2 != 0 and number % 3 != 0)


def crypto(set_):
    """crypto

    Args:
        set (): _description_

    Returns:
        list: _description_
    """
    answer = []
    for step1, step2 in enumerate(set_):
        if is_prime(step1) or step1 in (2, 3):
            answer.append(step2)
    return answer


def main():
    """main fuction
    """
    print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(crypto('О Дивный Новый мир!'))


main()
