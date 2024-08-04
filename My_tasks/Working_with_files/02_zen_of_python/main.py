"""Задача 02. Дзен Пайтона"""


def main():
    """main function
    """
    with open("Module22/02_zen_of_python/zen.txt",
              "r", encoding="utf8") as f:
        content = f.readlines()
        length = len(content)
        print(content[-1])
        for step in range(2, length + 1):
            print(content[step * -1], end='')


main()
