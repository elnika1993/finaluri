def sia():
    a = []
    b = int(input("sheiyvane ricvi: "))
    list.append(a, b)
    c = int(input("sheiyvane ricvi: "))
    list.append(a, c)
    d = int(input("sheiyvane ricvi: "))
    list.append(a, d)
    e = int(input("sheiyvane ricvi: "))
    list.append(a, e)
    f = int(input("sheiyvane ricvi: "))
    list.append(a, f)
    print(a)
    for i in range(1, 5):
        if a[i] > a[i-1]:
            print(a[i], end="")
sia()