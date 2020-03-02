x = 50

def func(x):
    print('х равен', x)
    x = 2
    print('Замена локального х на', x)

func(x)
print ('Переменная все еще ', x)
