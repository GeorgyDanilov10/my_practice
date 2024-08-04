"""Задача 5. Пароль"""


def chek_password(password):
    """chek_password

    Args:
        password (str): text
    """
    flag = True
    while flag:
        score1 = 0
        score2 = 0
        for step in password:
            if step.isdigit():
                score1 += 1
            if step.isupper():
                score2 += 1
        if len(password) >= 8 and score1 >= 3 and score2 >= 1:
            print('Это надёжный пароль!')
            flag = False
        else:
            print('Пароль ненадёжный. Попробуйте ещё раз.')
            password = input('Придумайте пароль: ')


def main():
    """main function
    """
    password = input('Придумайте пароль: ')
    chek_password(password)


main()
