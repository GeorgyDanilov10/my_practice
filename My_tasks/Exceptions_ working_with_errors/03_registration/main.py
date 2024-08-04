"""Задача 3. Регистрация"""


def chek_name(name):
    """chek_name

    Args:
        name (str): georgy

    Returns:
        bool: True or False
    """
    return name.isalpha()


def chek_mail(mail):
    """chek_mail

    Args:
        mail (str): test@test.ru

    Returns:
        bool: True or False
    """
    return mail.find('@') != -1 and mail.find('.') != -1


def chek_year(year):
    """chek_year

    Args:
        year (int): number

    Returns:
        bool: True or False
    """
    return 10 < int(year) < 99


def chek_user_data(text_line):
    """chek_user_data

    Args:
        text_line (list): [_description_]

    Raises:
        IndexError: Error
        NameError: Error
        SyntaxError: Error
        ValueError: Error

    Returns:
        str: 'text'
    """
    try:
        if len(text_line) == 0:
            return 'Программа завершена'
        for user in text_line:
            list_user = user.split()
            flag_name = chek_name(list_user[0])
            flag_mail = chek_mail(list_user[1])
            flag_year = chek_year(list_user[2])
            del text_line[0]
            if flag_name and flag_mail and flag_year:
                with open("Module23/03_registration" +
                          "/registrations_good.log",
                          "a", encoding="utf8") as f:
                    f.write(f'{user}\n')
            else:
                with open("Module23/03_registration/registrations_bad.log",
                          "a", encoding="utf8") as f:
                    if not flag_name and flag_mail and flag_year:
                        f.write(f'{user}  НЕ присутствуют все три поля\n')
                        raise IndexError
                    if not flag_name:
                        f.write(
                            f'{user}  Поле «Имя» содержит' +
                            ' НЕ только буквы:\n')
                        raise NameError
                    if not flag_mail:
                        f.write(
                            f'{user}  Поле «Имейл» НЕ ' +
                            'содержит @ и . (точку)\n')
                        raise SyntaxError
                    f.write(
                        f'{user} Поле «Возраст» НЕ является ' +
                        'числом от 10 до 99 \n')
                    raise ValueError
    except (ValueError, SyntaxError, NameError, IndexError):
        return chek_user_data(text_line)
    return None


def main():
    """main function
    """
    with open("Module23/03_registration/registrations.txt",
              "r", encoding="utf8") as f:
        text_line = f.readlines()
        text_line = [line.rstrip() for line in text_line]
        print(text_line[0])
    chek_user_data(text_line)


main()
