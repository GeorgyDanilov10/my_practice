"""Нет модуля"""

def even_list(_list_):
    """
    Функция, печатающая список четных индексов.
    """
    even_list1 = []
    for step in range (len(_list_), 0, -1):
        if step % 2 == 0:
            even_list1.append(_list_[step * -1])
    return even_list1


def main():
    """
    Главная функция
    """
    name_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
    print('Первый день:', even_list(name_list))


main()
# Конец файла
