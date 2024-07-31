"""Задача 03. Файлы и папки"""
import os


def count_files_dirs_size(__path__):
    """count_files_dirs_size

    Args:
        path (str): _description_

    Returns:
        _type_: _description_
    """
    size = 0
    files = 0
    dirs = 0
    for dirpath, dirnames, filenames in os.walk(__path__):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            size += os.path.getsize(fp)
            files += 1
        dirs += len(dirnames)
    return (files, dirs, size)


def main():
    """main function
    """
    __path__ = input("Введите путь до каталога: ")
    (files1, dirs2, size3) = count_files_dirs_size(__path__)

    print("Размер каталога (в Кб):", size3/1024)
    print("Количество подкаталогов:", dirs2)
    print("Количество файлов:", files1)


main()
