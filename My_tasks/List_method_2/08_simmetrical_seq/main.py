"""_Модуль_"""


def symmetric_sequence(number):
    """Симметричная последовательность

    Args:
        number (int): number

    Returns:
        list: [number]
    """
    list_number1 = []
    n = 0
    for _ in range(number):
        answer = int(input('Число: '))
        list_number1.append(answer)
    print('\nПоследовательность:', list_number1)
    while n < number - 1:
        length = (number - n) // 2
        if list_number1[n: n+length] == list_number1[: number-length - 1: -1]:
            break
        n += 1
    print('Нужно приписать чисел:', n)
    print('Сами числа:', list_number1[:n][::-1])


def main():
    """
    Главная функция
    """
    numbers = int(input('Кол-во чисел: '))
    symmetric_sequence(numbers)


main()
