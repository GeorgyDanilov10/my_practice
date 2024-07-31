"""_Модуль_"""


def play_count(players, number_count):
    """Игра считалка

    Args:
        players (int): number
        number_count (int): number

    Returns:
        int: number
    """
    list_players = []
    list_table_players = []
    for step in range(1, players + 1):
        list_players.append(step)
        list_table_players.append(step)
    for _ in range(players - 1):
        print('Текущий круг людей:', list_table_players)
        print('Начало счёта с номера ', list_players[0])
        if players < number_count:
            number_shift = max(len(list_players), number_count) - \
                min(len(list_players), number_count)
            for _ in range(number_shift - 1):
                list_players.append(list_players.pop(0))
            list_table_players.remove(list_players[0])
        else:
            for _ in range(number_count - 1):
                list_players.append(list_players.pop(0))
            list_table_players.remove(list_players[0])
        print('Выбывает человек под номером ', list_players.pop(0), end='\n\n')
    return list_players.pop(0)


def main():
    """
    Главная функция
    """
    players = int(input('Кол-во человек: '))
    number_count = int(input('Какое число в считалке? '))
    print('Значит, выбывает каждый ' +
          str(number_count) + '-й человек', end='\n\n')
    print('Остался человек под номером', play_count(players, number_count))


main()
