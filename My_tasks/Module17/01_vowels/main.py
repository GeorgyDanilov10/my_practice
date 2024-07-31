def vowel_letters(text):
    """vowel_letters

    Args:
        text (str): "text"

    Returns:
        list: [vowel]
    """
    vowel_list = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
    vowel = [step1
             for step1 in text
             for step2 in vowel_list
             if step1 == step2]
    return vowel


def main():
    """main function
    """
    text = input('Введите текст: ')
    print('\nСписок гласных букв: ', vowel_letters(text))
    print('Длина списка: ', len(vowel_letters(text)))


main()
