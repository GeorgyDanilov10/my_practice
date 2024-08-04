"""Задача 4. Гистограмма частоты 2"""


def inverter(diction):
    """inverter

    Args:
        diction (dict): {_description_}
    """
    print('\nИнвертированный словарь частот:\n')
    new_dic = {}
    for step1 in diction:
        list_ = []
        for step2 in diction:
            if diction.get(step1) == diction.get(step2):
                list_.append(step2)
        new_dic[diction.get(step1)] = list_

    print(new_dic)


def origin(text):
    """origin

    Args:
        text (_type_): _description_

    Returns:
        _type_: _description_
    """
    print('Оригинальный словарь частот:')
    dict_ = {}
    text_list = [i for i in text]
    for step1 in text_list:
        if dict_.get(step1):
            del step1
        else:
            dict_[step1] = text.count(step1)
            print(f'{step1} : {dict_[step1]}')
            del step1
    return inverter(dict_)


def main():
    """main function
    """
    text = input('Введите текст: ')

    origin(text)


main()
