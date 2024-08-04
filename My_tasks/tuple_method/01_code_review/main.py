"""Задача 1. Ревью кода"""

students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def stud_ip_year(dict_):
    """stud_ip_year

    Args:
        dict_ (dict): {_description_}

    Returns:
        list: [_description_]
    """
    return [(step, dict_[step]["age"]) for step in dict_]


def surname_len(dict_):
    """surname_len

    Args:
        dict_ (dict): {_description_}

    Returns:
        int: 12345
    """
    surname_length = 0
    for step in dict_:
        surname_length += len(dict_[step]['surname'])
    return surname_length


def stud_interests(dict_):
    """stud_interests

    Args:
        dict_ (dict): {_description_}

    Returns:
        list: [_description_]
    """
    interest_list = []
    new_list = [dict_[step]['interests'] for step in dict_]
    for step1 in new_list:
        for step2 in step1:
            interest_list.append(step2)
    return interest_list


def main():
    """main function
    """
    print('Список пар "ID студента — возраст":', stud_ip_year(students))
    print('Полный список интересов всех студентов:', stud_interests(students))
    print('Общая длина всех фамилий студентов:', surname_len(students))


main()
