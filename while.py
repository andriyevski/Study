number = 23
running = True

while running:
    quess = int(input('Введите число что бы угадать: '))

    if quess == number:
        print('Поздравляю вы угадали!')
        running = False
    elif quess < number:
        print('Число немного больше')
    else:
        print('Нет число немного меньше')
print('Цыкл While закончен!')