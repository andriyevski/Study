f = 1
f2 = 0
f3 = 0
for n in range(10):
    f += f2 #1,2,3
    #print("fibonachi: ",f)
    f2 += f3
    if f3 != f2:
        print("fibonachi: ",f2)
    f3=f2+f
    print("fibonachi: ",f3)