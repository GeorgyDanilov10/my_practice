"""_Модуль_"""


def find_number(first_list, _list_, last_list, number):
    """
    Args:
        first_list (list): _list_
        _list_ (list): _list_
        last_list (list): _list_
        number (int): number

    Returns:
        int: total, _list_
    Интересно то что если взять передаваемый список, и этот наш список
    как обЪект будет изменяться) если взять test_list = first_list
    или first_list.extend(_list_) и дальше работать с этой или с той
    переменой то после завершения функции _list_1 изменится)
    """
    test_list = first_list + _list_
    total = 0
    for i in test_list:
        if i == 5:
            total += 1
            test_list.remove(i)
    if number == 3:
        total = 0
        test_list.extend(last_list)
        for i in test_list:
            if i == 3:
                total += 1
    return total, test_list


def main():
    """
    Главная функция
    """
    find_number1, find_number2 = 5, 3
    _list_1 = [1, 5, 3]
    _list_2 = [1, 5, 1, 5]
    _list_3 = [1, 3, 1, 5, 3, 3]
    result1 = find_number(_list_1, _list_2, _list_3, find_number1)
    result2, res2_list = find_number(_list_1, _list_2, _list_3, find_number2)
    print('Результат работы программы:')
    print('Кол-во цифр 5 при первом объединении:', result1[0])
    print('Кол-во цифр 3 при втором объединении:', result2)
    print('Итоговый список:', res2_list)


main()

# переписать программу
# Конец файла
