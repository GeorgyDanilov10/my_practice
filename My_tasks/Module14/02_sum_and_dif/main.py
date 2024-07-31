# TODO здесь писать код
def len_number(number):
    sum = 0
    for step in str(number):
        sum += 1
    return sum

def sum_number(number):
    sum = 0
    for step in str(number):
        sum += int(step)
    return sum

def main():
    number = int(input('Введите число: '))
    print('Сумма чисел:', sum_number(number))
    print('Количество цифр в числе:', len_number(number))
    print('Разность суммы и количества цифр:', sum_number(number) - len_number(number))
main()