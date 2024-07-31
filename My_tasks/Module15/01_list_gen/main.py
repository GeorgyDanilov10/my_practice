"""Нет модуля"""


def odd_number_list(number):
    """
    Функция, печатающая список нечетных чисел.
    """
    odd_number = []
    for step in range(1, number + 1):
        if step % 2 == 1:
            odd_number.append(step)
    return odd_number


def main():
    """
    Главная функция
    """
    number = int(input('Введите число: '))
    print('Список из нечётных чисел от одного до N:', odd_number_list(number))


main()
# Конец файла
