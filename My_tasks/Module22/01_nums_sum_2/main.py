"""Задача 01. Сумма чисел 2"""


def main():
    """main function
    """
    with open("Module22/01_nums_sum_2/numbers.txt",
              "r", encoding="utf8") as file:
        data = []
        score = 0
        for line in file:
            data.append([int(x) for x in line.split()])
        for step1 in data:
            for step2 in step1:
                score += step2
    with open("answer_task1.txt", "w+", encoding="utf8") as file:
        file.write(str(score))
        file.seek(0)
        text = file.read()
        print(text)


main()
