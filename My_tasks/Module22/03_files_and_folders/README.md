## Задача 03. Файлы и папки
### Что нужно сделать
Напишите программу, которая получает на вход путь до каталога (это может быть и просто корень диска) и выводит общее количество файлов и подкаталогов в нём. Также выведите на экран размер каталога в килобайтах (1 килобайт = 1024 байт).

Важный момент: чтобы посчитать, сколько весит каталог, нужно найти сумму размеров всех вложенных в него файлов. 

Результат работы программы на примере `python_basic\Module14`:
```
E:\PycharmProjects\python_basic\Module14
Размер каталога (в Кб):  9.61
Количество подкаталогов:  3
Количество файлов:  7
```
### Что оценивается
- Результат вычислений корректен.
- Формат вывода соответствует примеру.
- input содержит корректные приглашения для ввода. 
- Основной функционал описан в отдельных функциях.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).