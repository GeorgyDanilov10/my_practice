"""Задача 3. Файлы"""


def checking_the_name(namefile):
    """checking_the_nameFile

    Args:
        name_File (str): example.txt
    """
    ban_char1 = "@№$%^&\\*()"
    ban_char2 = '.txt .docx'
    ban_char_list2 = ban_char2.split()
    flag = True
    for step in ban_char1:
        if namefile.startswith(step):
            print('Ошибка: название начинается ' +
                  'на один из специальных символов.')
            flag = False
            break
    if flag:
        flag = False
        for step in ban_char_list2:
            if namefile.endswith(step):
                print('Файл назван верно.')
                flag = True
                break
        if not flag:
            print('Ошибка: неверное расширение файла. Ожидалось' +
                  '.txt или .docx.')


def main():
    """main function
    """
    file = input('Название файла: ')
    checking_the_name(file)


main()
