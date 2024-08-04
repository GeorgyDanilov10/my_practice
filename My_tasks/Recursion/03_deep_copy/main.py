"""Задача 3. Глубокое копирование"""
import copy

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


def deep_copy(obj):
    """deep_copy

    Args:
        obj (): _description_

    Returns:
        obj: _description_
    """
    if isinstance(obj, (int, float, bool, str)):
        return obj
    if isinstance(obj, list):
        return [deep_copy(item) for item in obj]
    if isinstance(obj, dict):
        return {key: deep_copy(value) for key, value in obj.items()}
    return copy.deepcopy(obj)


def deep_copy_site(sum_):
    """deep_copying

    Args:
        sum_ (int): 12345
    """
    list_site = []
    for _ in range(sum_):
        name_product = input('Введите название продукта для нового сайта: ')
        site['html']['head']['title'] = 'Куплю/продам ' + \
            f'{name_product} недорого'
        site['html']['body']['h2'] = 'У нас самая низкая цена ' + \
            f'на {name_product}'
        list_site += (name_product, deep_copy(site))
        for step1, step2 in enumerate(list_site):
            if step1 % 2 == 0:
                print(f'Сайт для {step2}')
            else:
                print(f'site = {step2}')


def main():
    """main function
    """
    sum_site = int(input('Сколько сайтов: '))
    deep_copy_site(sum_site)


main()
