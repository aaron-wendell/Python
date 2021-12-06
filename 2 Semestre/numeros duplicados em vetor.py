def duplicado(num):
    x = num[0]
    y = num[0]
    while True:
        x = num[x]
        y = num[num[y]]
        if x == y:
            break
        
        
    a = num[0]
    b = x
    while a!= b:
        a = num[a]
        b = num[b]
    return a


print(duplicado([1,2,8,0,4,8,9]))