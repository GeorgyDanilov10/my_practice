"""Задача 4. По парам"""


def main():
    """main function
    """
    list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f'Оригинальный список: {list1}')
    new_list = [(step2, step2 + 1)
                for step1, step2 in enumerate(list1) if step1 % 2 == 0]
    print(f'Новый список:: {new_list}')
    length = len(list1)
    print(f'Оригинальный список: {list1}')
    new_list = [(list1[step], list1[step] + 1)
                for step in range(length) if step % 2 == 0]
    print(f'Новый список:: {new_list}')


main()
