"""Задача 6. Сжатие"""


def space(line):
    """space

    Args:
        line (str): text

    Returns:
        list: [list]
    """
    i = 0
    new_line = ''
    for step1 in line:
        if i < len(line) - 1:
            i += 1
        if step1 == line[i]:
            new_line += step1
        else:
            new_line += step1
            new_line += ' '
    return new_line.split()


def cod_line(line):
    """cod_line

    Args:
        line (str): text

    Returns:
        str: text
    """
    new_line = ''
    list_word = space(line)
    for step in list_word:
        new_line = new_line + step[0] + str(len(step))
    return new_line


def main():
    """main function
    """
    line = input('Введите строку: ')
    print(f'Закодированная строка: {cod_line(line)}')


main()
