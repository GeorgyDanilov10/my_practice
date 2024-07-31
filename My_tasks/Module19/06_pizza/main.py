"""Задача 6. Пицца"""


def order_chek(number):
    """order_chek

    Args:
        number (int): 123456
    """
    name = {}
    list_1 = []
    for step in range(1, number + 1):
        print(f'{step} заказ: ', end='')
        order = input()
        list_1 = order.split()
        if name.get(list_1[0]):
            pizza = name.get(list_1[0])
            name[list_1[0]] = pizza
        else:
            pizza = {}
            name[list_1[0]] = pizza
        if pizza.get(list_1[1]):
            pizza[list_1[1]] = int(list_1[2]) + pizza.get(list_1[1])
        else:
            pizza[list_1[1]] = int(list_1[2])
    for step1, step2 in name.items():
        for step3, step4 in step2.items():
            print(f'{step1}:')
            print(' ' * 5, f"{step3}: {step4}")


def main():
    """main funcion
    """
    order_sum = int(input('Введите количество заказов: '))
    order_chek(order_sum)


main()
