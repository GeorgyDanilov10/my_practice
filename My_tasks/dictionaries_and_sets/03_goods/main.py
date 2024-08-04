"""Задача 3. Товары"""


def account_pro(goods, store):
    """account_pro

    Args:
        goods (dict): [_description_]
        store (dict): [_description_]
    """
    for step in goods:
        score = 0
        n = 0
        sum_ = 0
        while n < len(store[goods.get(step)]):
            score = int(store[goods.get(step)][n]['quantity'] *
                        store[goods.get(step)][n]['price'] + score)
            sum_ += store[goods.get(step)][n]['quantity']
            n += 1
        print(f"{step} - {sum_}, стоимость {score} рубля")


def main():
    """main function
    """
    goods = {
        'Лампа': '12345',
        'Стол': '23456',
        'Диван': '34567',
        'Стул': '45678',
    }

    store = {
        '12345': [
            {'quantity': 27, 'price': 42},
        ],
        '23456': [
            {'quantity': 22, 'price': 510},
            {'quantity': 32, 'price': 520},
        ],
        '34567': [
            {'quantity': 2, 'price': 1200},
            {'quantity': 1, 'price': 1150},
        ],
        '45678': [
            {'quantity': 50, 'price': 100},
            {'quantity': 12, 'price': 95},
            {'quantity': 43, 'price': 97},
        ],
    }
    account_pro(goods, store)


main()
