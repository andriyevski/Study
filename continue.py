# -*- coding: utf-8 -*-
while True:
    s = input('\n\nВведите ваш пароль: \nДля выхода введите \'exit\' ')
    if s == 'exit':
        break
    if len(s) <6:
        print('Введенный пароль {} слишком простой!\n\n'.format(s))
        continue
    print('Пароль {} нужной длинны! \n\n'.format(s))
