def avg(*num):
    a = []
    suma = 0
    for val in num:
        a.append(val)

    for b in a:
        suma+=b

    print(suma/len(a))
    print(sum(num)/len(num))

avg(10,10,20)
