n = int(input ("Введите n: "))
mass = list(map(int, input("Введите массив: ").split()))
k, m = map(int, input("Введите k,m: ").split())

if ( 0 < n <= 10000) and ( 0 < k <= n) and (k <= m <= m):
    temp = mass[k - 1:m]
    # print(temp)

    temp = temp[::-1]
    # print(temp)

    result = []
    result.append(*mass[:k - 1])
    
    l = len(temp)
    for i in range(0, l):
        result.append(temp[i])
    result.append(*mass[m:])
    
    print(*result)
else:
    print("Введенные числа не подходят!")