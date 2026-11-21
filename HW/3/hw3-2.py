n = int(input("Введите n: "))
mass = list(map(int, input("Введите массив: ").split()))
r = int(input("Введите r: "))

if (0 < n <= 10000):
    r = r % n
    # print(r)

    # mass = mass[::-1]
    # mass = mass[r:] + mass[:r]
    # mass = mass[::-1]
    mass = mass[-r:] + mass[:r]

    print(*mass)
else:
    print("Число n не входит в диапазон!")