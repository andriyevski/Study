import sys
import using_name # Подключение модуля

using_name.check_include() # Подключение функции модуля
print('Version module: ',using_name.__version__) #Проверка версии модуля
print(' Argument string: ')
for i in sys.argv:
    print(i)
print('\n\n string PATH : ' , sys.path, '\n')