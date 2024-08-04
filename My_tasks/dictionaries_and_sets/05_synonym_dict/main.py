"""Задача 5. Словарь синонимов"""


def couple(number):
    """couple

    Args:
        number (int): 1233445
    """
    diction = {}
    for step in range(1, 1 + number):
        word = ''
        save = ''
        flag = True
        print(f'{step} пара: ', end='')
        answer = input()
        for step in answer:
            if step != ' ':
                word += step
            else:
                if flag:
                    save = word
                    flag = False
                diction[save] = word
                word = ''
        diction[save] = word
        print(diction)
    while True:
        find_word = input('Введите слово: ')
        for step1, step2 in diction.items():
            if step1 == find_word:
                print('Синоним:', step2)
                flag = True
                break
            if step2 == find_word:
                print('Синоним:', step1)
                flag = True
                break
        if not flag:
            print('Такого слова в словаре нет.')
        else:
            break


def main():
    """main function
    """
    couple_sum = int(input('Введите количество пар слов: '))
    couple(couple_sum)


main()
