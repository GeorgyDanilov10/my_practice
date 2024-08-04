"""Нет модуля"""


def find_new_containers(new_container_weight, new_lsit_containers, sum1):
    """
    Функция, находит индекс нового контейнера.
    """
    save = 0
    for step in range(sum1):
        if new_lsit_containers[step] == new_container_weight:
            save = step
    print('Номер, который получит новый контейнер: ', end='')
    return save + 1


def new_list_containers(containers_list, sum1):
    """
    Функция, печатающая новый упорядоченный список контейнеров.
    """
    new_lsit_containers = []
    new_container_weight = int(input('Введите вес нового контейнера: '))
    containers_list.append(new_container_weight)
    sum1 += 1
    print('Новый список из', sum1, 'контейнеров')
    for step in range(1, sum1 + 1):
        new_lsit_containers.append(max(containers_list))
        print(step, 'контейнер весит', max(containers_list))
        containers_list.remove(max(containers_list))
    return find_new_containers(new_container_weight, new_lsit_containers, sum1)


def containers(sum1):
    """
    Функция, печатающая список контейнеров.
    """
    containers_list = []
    for _ in range(sum1):
        weight = int(input('Введите вес контейнера: '))
        if weight <= 200:
            containers_list.append(weight)
        else:
            while weight > 200:
                weight = int(
                    input('Введите вес контейнера, что бы он не превышал 200: '))
                if weight <= 200:
                    containers_list.append(weight)
    return new_list_containers(containers_list, sum1)


def main():
    """
    Главная функция
    """
    sum_containers = int(input('Количество контейнеров: '))
    print('Список из', sum_containers, 'контейнеров')
    print(containers(sum_containers))


main()
