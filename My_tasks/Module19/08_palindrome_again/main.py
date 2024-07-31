"""Задача 8. Снова палиндром"""


def main():
    """main function
    """
    line = input('Введите строку: ')
    length = len(line)
    flag = False
    for _ in range(length):
        if line == line[::-1]:
            print('Можно сделать палиндромом')
            flag = True
            break
        else:
            line = line[1:] + line[0]
    if not flag:
        print('Нельзя сделать палиндромом')


main()
