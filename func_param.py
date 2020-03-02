def PrintMax(a,b):
    if a>b:
        print(a,'Максимально')
    elif a==b:
        print(a,'Равно',b)
    else:
        print(b,'Максимально')

PrintMax(7,99) #Прямая передача значений

param = input('Веведите цыфру')
param2 = input('Веведите цыфру')

PrintMax(param,param2)
