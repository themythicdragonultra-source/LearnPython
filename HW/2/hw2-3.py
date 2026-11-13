n = int(input("Введите число: "))
fact = []
f = 1
if (n > 0) and (n <= 15):
    for i in range(1, n + 1):
        f = f * i
        fact.append(f)
    print(*fact)
else:
    print("Число не входит в диапазон 0 < n <= 15")