a = int(input("Введите число: "))
b = 0
number = []
if (a > 0) and (a <= 10000):
    for i in range(1,a + 1):
        b = i * 2
        number.append(b)
    print(*number)
else:
    print("Число не входит в диапазон 0 < n <= 10000")
