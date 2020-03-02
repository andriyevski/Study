def total(int=5, *num, **key):
    count = int
    for number in num:
        count += number
    for key_a in key:
        count += key[key_a]
        return[count]
print(total(10,vegetables = 50, fruits = 100))