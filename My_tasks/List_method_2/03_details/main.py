"""_Модуль_"""


def sorted_shop(_list_):
    """Сортирует товары в магазине

    Args:
        _list_ (list): [list]
    """
    answer = input('Название детали: ')
    save = 0
    total = 0
    for step1 in _list_:
        for step2 in step1:
            if step2 == answer:
                save += step1[1]
                total += 1
    print('Кол-во деталей —', total)
    print('Общая стоимость —', save)


def main():
    """
    Главная функция
    """
    shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
            ['педаль', 100], ['седло', 1500], ['рама', 12000],
            ['обод', 2000], ['шатун', 200], ['седло', 2700]]
    sorted_shop(shop)


main()
