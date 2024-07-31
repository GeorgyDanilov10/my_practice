"""Задача 7. Своя функция zip"""


def zip_2(data1, data2):
    """zip_2

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Yields:
        tuple: _description_
    """
    for step1, step2 in enumerate(data1):
        yield (step2, data2[step1])


def main():
    """main function
    """
    line = 'abcd'
    tpl = (10, 20, 30, 40)
    list1 = [10, (2, 3, 4), 30, 40]
    list2 = ['a', 1, 'c', 2]
    print(gen1 := zip_2(line, tpl))
    for step in gen1:
        print(step)
    print(gen2 := zip_2(list1, list2))
    for step in gen2:
        print(step)


main()
