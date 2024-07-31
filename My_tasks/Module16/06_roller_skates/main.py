"""_Модуль_"""


def roller(list1, list2):
    """_summary_

    Args:
        list1 (list): [list]
        list2 (list): [list]

    Returns:
        int: number
    """
    score = 0
    number_skates = int(input('Кол-во коньков: '))
    for step1 in range(1, number_skates + 1):
        print('Размер ' + str(step1) + '-й пары:', end=' ')
        answer = int(input())
        list1.append(answer)
    number_human = int(input('Кол-во людей: '))
    for step2 in range(1, number_human + 1):
        print('Размер ноги ' + str(step2) + '-го человека:', end=' ')
        answer = int(input())
        list2.append(answer)
    if len(list1) < len(list2):
        list1, list2 = list2, list1
    for step1 in list1:
        for step2 in list2:
            if step1 == step2:
                score += 1
                list1.remove(step1)
                list2.remove(step1)
    return score


def main():
    """
    Главная функция
    """
    list_skates = []
    list_human = []
    print('Наибольшее кол-во людей, которые могут взять ролики:',
          roller(list_skates, list_human))


main()
