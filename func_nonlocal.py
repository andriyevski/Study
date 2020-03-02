def func_outer():
    x = 2
    print('x ravno ', x)

    def func_inner():
        nonlocal x
        x = 5

    func_inner()
    print('Local x zamena na ',x)

func_outer()
