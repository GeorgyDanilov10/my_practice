def list_number(number):
    """list_number

    Args:
        number (int): 1,2,3

    Returns:
        list: [1, 2, 3]
    """
    list_num = [(1 if step % 2 == 0 else step % 5)
                for step in range(number)]
    return list_num


def main():
    """main function
    """
    number = int(input('Введите длину списка: '))
    print('Результат:', list_number(number))


main()
