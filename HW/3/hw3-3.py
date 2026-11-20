n = int(input ("Введите n: "))
mass = list(map(int, input("Введите массив: ").split()))
k, m = map(int, input("Введите k,m: ").split())
r = int(input("Введите r: "))

if ( 0 < n <= 10000) and ( 0 < k <= n) and (k <= m <= m):
    temp = mass[k - 1:m]
    # print(temp)

    if (r >= 0) and (r <= n):
        r = r
    else:
        r = r % n

    temp = temp[::-1]
    temp = temp[r:] + temp[:r]
    temp = temp[::-1]

    result = []

    for i in range(0, k - 1):
        result.append(mass[i])
    
    l = len(temp)
    for i in range(0, l):
        result.append(temp[i])
    

    for i in range(m, n):
        result.append(mass[i])
    
    print(*result)
else:
    print("Введенные числа не подходят!")