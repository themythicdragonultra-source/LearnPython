a, d, n = map(int, input().split())
mass = []
if (n > 0) and (n <= 10000):
    for i in range(0, n):
        r = (a + i * d) ** 2
        mass.append(r)
    print(*mass)
else:
    print("n не входит в диапазон 0 < n <= 10000")
