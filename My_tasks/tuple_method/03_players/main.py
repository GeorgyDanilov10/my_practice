"""Задача 3. Игроки"""

players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}


def main():
    """main function
    """
    new_list = []
    for name, score in players.items():
        new_list += (name + score,)
    print(new_list)


main()
