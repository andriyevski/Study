def printMax(x,y):
    '''
    Выводит максимум!
    '''
    x = int(x) #Privodit v tip
    y = int(y)
    
    if x > y:
        print(x,'blshe! ',y)
    else:
        print(y,'bolshe!', x)
printMax(12,4)
print(printMax.__doc__)