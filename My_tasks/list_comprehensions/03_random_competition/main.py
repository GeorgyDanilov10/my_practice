from random import uniform


def win(list1, list2):
    """win

    Args:
        list1 (list): [float]
        list2 (list): [float]

    Returns:
        list: [float]
    """
    return [(list1[step] if list1[step] > list2[step] else list2[step])
            for step in range(20)]


def main():
    """main function
    """
    team_list1 = [round(uniform(5, 10), 2) for _ in range(20)]
    team_list2 = [round(uniform(5, 10), 2) for _ in range(20)]
    print('Первая команда:', team_list1)
    print('Вторая команда:', team_list2)
    print('Победители тура:', win(team_list1, team_list2))


main()
