"""Задача 5. Частотный анализ"""


def count_character(list_line):
    """count_character

    Args:
        list_line (list): [_description_]
    """
    with open("analysis_task5.txt",
              "w+", encoding="utf8") as f:
        char = {}
        length = 0
        for step1 in list_line:
            length += len(step1)
            step1 = step1.lower()
            for step2 in step1:
                score1 = 0
                if step2.isalpha():
                    if char.get(step2):
                        score1 += char.get(step2)
                    char[step2] = score1 + 1
                else:
                    length -= 1
        char = dict(
            sorted(char.items(), key=lambda
                   item: item[1], reverse=True))
        for step in char:
            char[step] = round((char[step] / length), 3)
            f.write(f'{step} {char[step]}\n')
        f.seek(0)
        text = f.read()
        print(text)


def main():
    """main function
    """
    with open("Module22/05_frequency_analysis/text.txt",
              "r", encoding="utf8") as f:
        list_text_line = f.readlines()
    count_character(list_text_line)


main()
