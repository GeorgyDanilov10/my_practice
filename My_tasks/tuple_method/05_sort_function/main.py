"""Задача 5. Функция сортировки"""


def sort_tuple(tpl):
    flag = True
    for step in tpl:
        if not isinstance(step, int):
            save = tpl
            flag = False
            break
    if flag:
        tpl = list(tpl)
        length = len(tpl)
        for step1 in range(length):
            for step2 in range(step1 + 1, length):
                if tpl[step1] > tpl[step2]:
                    tpl[step1], tpl[step2] = tpl[step2], tpl[step1]
        save = tuple(tpl)
    return save


def main():
    """main function
    """
    tpl = (6, 3, -1, 8, 4, 10, -5)
    print(sort_tuple(tpl))


main()
