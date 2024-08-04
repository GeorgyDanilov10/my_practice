"""Задача 8. Бегущая строка"""


def chek_line(line1, line2):
    """chek_line

    Args:
        line1 (str): line
        line2 (str): line
    """
    length = len(line1)
    score = 0
    flag = False
    for _ in range(length):
        if line1 != line2:
            score += 1
            line2 = line2[1:] + line2[0]
        else:
            flag = True
            print(f'Первая строка получается из второй со сдвигом {score}.')
            break
    if not flag:
        print('Первую строку нельзя получить из второй с' +
              ' помощью циклического сдвига.')


def main():
    """main function
    """
    line1 = input('Первая строка: ')
    line2 = input('Вторая строка: ')
    chek_line(line1, line2)


main()
