# TODO здесь писать код
def nod(number):
    save = 0
    nod = number
    while nod >= 2:
        if number % nod == 0:
            save = nod
        nod -= 1
    return save
def main():
    number = int(input('Введите число: '))
    print('Наименьший делитель, отличный от единицы:', nod(number))
main()