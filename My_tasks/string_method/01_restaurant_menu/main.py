"""Задача 1. Меню ресторана"""


def main():
    """main function
    """
    menu = input('Введите Доступное меню: ')
    print('На данный момент в меню есть:', ", ".join(menu.split(';')))


main()
