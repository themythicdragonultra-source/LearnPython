a = set(map(int, input("Введите числа для множества A: ").split()))
b = set(map(int, input("Введите числа множества B: ").split()))
c = set(map(int, input("Введите числа для множества C: ").split()))
d = set(map(int, input("Введите числа для множества D: ").split()))

temp = set()

temp.update(a)
temp.update(b)
temp.difference_update(c)
temp.intersection_update(d)
# print(temp)

temp = sorted(temp)
print(*temp)