"""Задача 6. Контакты 3"""

contacts = {}


def find_contact():
    """find_contact
    """
    surname = input('Введите фамилию для поиска: ')
    flag = True
    for step1, step2 in contacts.items():
        if step1[1] == surname:
            flag = False
            st = str(' '.join(step1))
            print(f'{st} {step2}')
            break
    if flag:
        print('Такого человека нет')


def add_contact():
    """add_contact
    """
    name = input('Введите имя и фамилию нового контакта (через пробел): ')
    list1 = tuple(name.split())
    if contacts.get(list1):
        print('Такой человек уже есть в контактах.')
    else:
        number = int(input('Введите номер телефона: '))
        contacts[list1] = number
        del list1
    print(f'Текущий словарь контактов: {contacts}')


def main():
    """main function
    """
    print('Введите номер действия:')
    print('1. Добавить контакт')
    print('2. Найти человека')
    answer = int(input('Введите число '))
    if answer == 1:
        add_contact()
    else:
        find_contact()
    main()


main()
