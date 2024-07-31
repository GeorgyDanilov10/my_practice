"""Нет модуля"""


def palindrom(text):
    """
    Функция, проверяет палиндром или нет.
    """
    save = text
    palindrome = ''
    for step in range(len(text)):
        palindrome += text[len(text) - 1 - step]
    if save == palindrome:
        print('Да, это палиндром!')
    else:
        print('Нет, это не палиндром!')


def main():
    """
    Главная функция
    """
    text = input('Введите слово: ')
    palindrom(text)


main()
