def sort_line(line):
    """sort_line

    Args:
        line (str): text

    Returns:
        str: text
    """
    length = len(line)
    save1 = 0
    save2 = 0
    for step in range(1, length + 1):
        if line[-step] == 'h':
            save1 = length - step - 1
            break
    for step in range(length):
        if line[step] == 'h':
            save2 = step
            break
    return line[save1:save2: -1]


def main():
    """main function
    """
    line = input('Введите строку: ')
    print('Развёрнутая последовательность между первым и последним h:',
          sort_line(line))


main()
