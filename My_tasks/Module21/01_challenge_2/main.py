"""Задача 1. Challenge 2"""


def score_fun(number, num=0):
    """score_fun

    Args:
        number (int): 12345
        num (int): 12345

    Returns:
        int: 12345
    """
    if num == number:
        return number
    else:
        num += 1
        print(num)
        return score_fun(number, num)


def main():
    """main function
    """
    number = int(input('Введите num: '))
    score_fun(number)


main()
