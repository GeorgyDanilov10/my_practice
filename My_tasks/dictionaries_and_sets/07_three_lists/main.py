"""Задача 7. Три списка"""


def plenty(ple1, ple2, ple3):
    """_summary_

    Args:
        ple1 (set): _description_
        ple2 (set): _description_
        ple3 (set): _description_
    """
    print('Задача 1 с множеством -', set(ple1) & set(ple2) & set(ple3))
    print('Задача 2 с множеством -', set(ple1) - set(ple2) - set(ple3))


def not_set(list1, list2, list3):
    """not_set

    Args:
        list1 (list): [_description_]
        list2 (list): [_description_]
        list3 (list): [_description_]
    """
    new_list = [step1 for step1 in list1
                if step1 in list2 and step1 in list3]
    print('Задача 1 без множества -', new_list)
    new_list = [step1 for step1 in list1
                if step1 not in list2 and list3]
    print('Задача 2 без множества -', new_list)


def main():
    """main function
    """
    array_1 = [1, 5, 10, 20, 40, 80, 100]
    array_2 = [6, 7, 20, 80, 100]
    array_3 = [3, 4, 15, 20, 30, 70, 80, 120]
    plenty(array_1, array_2, array_3)
    not_set(array_1, array_2, array_3)


main()
