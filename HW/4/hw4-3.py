a = set(input("Введите первое слово: "))
b = set(input("Введите второе слово: "))
# print(a, b)

result = True

temp1 = a - b
temp2 = b - a

if temp1 != set():
    result = False
    l = temp1
    l = list(l)
    print("Результат:", result, "(лишняя буква:", *l, ")")
elif temp2 != set():
    result = False
    l = temp2
    l = list(l)
    print("Результат:", result, "(лишняя буква:", *l, ")")
else:
    print("Результат:", result)