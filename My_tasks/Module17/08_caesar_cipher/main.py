def code(message, shift):
    """code

    Args:
        message (str): 'text'
        shift (int): number

    Returns:
        str: 'code'
    """
    alp = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    alphabet = [i for i in alp]
    save = 0
    score = 0
    code_message = ''
    for step in message:
        for step2 in alphabet:
            if step2 != step:
                score += 1
        if score == 33:
            code_message += step
            score = 0
        else:
            save = alphabet.index(step)
            alphabet = alphabet[save:] + alphabet[:save]
            code_message += alphabet[shift]
            score = 0
    return code_message


def main():
    """main function
    """
    message = input('Введите сообщение: ')
    shift = int(input('Введите сдвиг: '))
    print('Зашифрованное сообщение:', code(message, shift))


main()
