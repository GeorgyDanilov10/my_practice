"""Задача 7. IP-адрес 2"""


def chek_list(_list_):
    """chek_list

    Args:
        list (list): [number]

    Returns:
        bool: bool
    """
    line = '.'.join(_list_)
    score = 0
    flag = False
    for step in line:
        if step == '.':
            score += 1
    if score == 3:
        flag = True
    return flag


def chek_ip(ip):
    """chek_ip

    Args:
        ip (str): 22.22.22.22
    """
    list_number = ip.split('.')
    flag = True
    if not chek_list(list_number):
        print('Адрес — это четыре числа, разделённые точками.')
        flag = False
    else:
        for step in list_number:
            if not step.isdigit():
                print(f'{step} - это не целое число')
                flag = False
                break
            if int(step) > 255:
                print(f'{step} превышает 255.')
                flag = False
                break
    if flag:
        print('IP-адрес корректен.')


def main():
    """main function
    """
    ip = input('Введите IP: ')
    chek_ip(ip)


main()
