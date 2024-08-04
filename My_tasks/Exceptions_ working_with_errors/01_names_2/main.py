"""Задача 1. Имена 2"""


def count_char_name(list_text_line, length=1, line=0):
    """count_char_name

    Args:
        list_text_line (list): _description_
        length (int, optional): _description_. Defaults to 1.
        line (int, optional): _description_. Defaults to 0.

    Raises:
        ValueError: text

    Returns:
        int: length
    """
    copy_list = list_text_line[:]
    if len(copy_list) == 0:
        return print('Общее количество символов: ', length)
    try:
        line += 1
        length += len(copy_list[0]) - 1
        if len(copy_list[0]) - 2 < 3:
            raise ValueError
        copy_list.remove(copy_list[0])
        return count_char_name(copy_list, length, line)
    except ValueError:
        print(f'Ошибка: менее трёх символов в строке {line}')
        with open("Module23/01_names_2/errors_mod23_task_1.log",
                  "a", encoding="utf8") as f:
            f.write(f'Ошибка: менее трёх символов в строке {line}\n')
        copy_list.remove(copy_list[0])
        return count_char_name(copy_list, length, line)


def main():
    """main function
    """
    with open("Module23/01_names_2/people.txt",
              "r", encoding="utf8") as f:
        list_text_line = f.readlines()
        count_char_name(list_text_line)


main()
