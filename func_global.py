x = 50

def func():
    global x
    print('x ravno', x)
    x = 2
    print('zamena x na ',x)

func()
print('Znachenie x est : ', x)
