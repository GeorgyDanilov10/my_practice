"""Задача 05. Надёжные вычисления"""

from math import sqrt


def get_sage_sqrt(num):
    """get_sage_sqrt

    Args:
        num (int): 123

    Returns:
        int: 123
    """
    try:
        return sqrt(num)
    except (TypeError, ValueError) as erorr:
        return erorr


def main():
    """main function
    """
    numbers = [16, 25, -9, 0, 4.5, "abc"]
    for number in numbers:
        result = get_sage_sqrt(number)
        print(f"Квадратный корень numbers {number}: {result}")


main()
