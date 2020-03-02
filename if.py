number = 23
guess = int(input('Введите целове число: '))

if guess == number:
    print('Поздровляю вы угадали,',number)
    print('хотя и не выиграли никакого приза')
elif guess < number:
    print('Нет, число немного больше...')
else:
    print('Нет, число немного меньше')
print('END GAME')