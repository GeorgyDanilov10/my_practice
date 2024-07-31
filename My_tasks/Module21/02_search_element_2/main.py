"""Задача 2. Поиск элемента 2"""
site = {
    'html': {
        'head': {
            'title': 'Мой сайт',
            'meta': {'Мой сайт': 'Главный'}
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац',
            '1': {'2': {'3': {'4': {'5': 'Привет'}}}}
        }
    }
}


def find_key(answer1, answer3, list_1=None, score=1):
    """find_key

    Args:
        answer1 (str): _description_
        answer3 (int): _description_
        list_1 (list, optional): _description_. Defaults to [site].
        score (int, optional): _description_. Defaults to 1.

    Returns:
        key: value
    """
    if list_1 is None:
        list_1 = [site]
    length = len(list_1)
    for step in range(length):
        save = list_1[step]
        for key, value in save.items():
            if key == answer1:
                return print(f'{key} : {value}')
            if isinstance(value, dict):
                list_1.append(value)
        list_1.remove(save)
    if len(list_1) == 0 or answer3 == score:
        return print('Значение ключа: None')
    score += 1
    return find_key(answer1, answer3, list_1, score)


def main():
    """main function
    """
    answer1 = input('Введите искомый ключ: ')
    answer2 = input('Хотите ввести максимальную глубину? Y/N: ')
    if 'y' == answer2.lower():
        answer3 = int(input('Введите максимальную глубину: '))
        find_key(answer1, answer3, list_1=[site])
    else:
        find_key(answer1, answer3=None)


main()
