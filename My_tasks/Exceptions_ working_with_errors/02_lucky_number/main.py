"""Задача 2. Счастливое число"""
from random import randint


def main():
    """main function
    """
    save_number = 0
    with open("Module23/02_lucky_number/out_file.txt",
              "w+", encoding="utf8") as f:
        while True:
            number = int(input('Введите число: '))
            save_number += number
            if randint(1, 13) == 1:
                raise ValueError('Вас постигла неудача!')
            f.write(f'{number}\n')
            if save_number >= 777:
                print('Вы успешно выполнили условие для выхода из' +
                      'порочного цикла!')
                break


main()
