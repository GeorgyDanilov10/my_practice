"""Задача 9. Анализ комментариев"""


def count_upper_lower(text):
    """count_upper_lower

    Args:
        text (str): text

    Returns:
        int: number
        int: number
    """
    score1 = 0
    score2 = 0
    for step in text:
        if step.isupper():
            score1 += 1
        if step.islower():
            score2 += 1
    return score1, score2


def main():
    """main function
    """
    text = input("Введите строку для анализа: ")
    uppercase, lowercase = count_upper_lower(text)
    print("Количество заглавных букв:", uppercase)
    print("Количество строчных букв:", lowercase)


main()
