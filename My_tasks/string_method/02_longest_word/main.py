"""Задача 2. Самое длинное слово"""


def find_long_word(text):
    """find_long_word

    Args:
        text (str): 'hello sd ss'
    """
    list1 = text.split()
    score = 0
    save = ''
    for step in list1:
        if len(step) > score:
            score = len(step)
            save = step
    print(f'Самое длинное слово: {save}')
    print(f'Самое длинное слово: {score}')


def main():
    """main function
    """
    line = input('Введите строку: ')
    find_long_word(line)


main()
