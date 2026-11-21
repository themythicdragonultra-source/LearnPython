n = int(input ("Введите n: "))
mass = list(map(int, input("Введите массив: ").split()))
k, m = map(int, input("Введите k,m: ").split())

if ( 0 < n <= 10000) and ( 0 < k <= n) and (k <= m <= n):
    temp = mass[k - 1:m]
    l = len(temp)
    # print(temp)

    temp = temp[::-1]
    # print(temp)

    result = []

    result = mass[:k - 1] + temp + mass[m:]
    
    print(*result)
else:
    print("Введенные числа не подходят!")