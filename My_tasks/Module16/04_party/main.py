"""_Модуль_"""


def party(_list_):
    """Функция, для вечеринок

    Args:
        _list_ (list): [list]
    """
    while True:
        print('Сейчас на вечеринке', len(_list_), 'человек:', _list_)
        answer = input('Гость пришёл или ушёл? ')
        if answer == 'пришёл':
            name = input('Имя гостя: ')
            if len(_list_) == 6:
                print('Прости, ' + name + ', но мест нет.')
            else:
                print('Привет, ' + name + '!')
                _list_.append(name)
        elif answer == 'ушёл':
            name = input('Имя гостя: ')
            print('Пока, ' + name + '!')
            _list_.remove(name)
        else:
            print('Вечеринка закончилась, все легли спать.')
            break


def main():
    """
    Главная функция
    """
    guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
    party(guests)


main()
