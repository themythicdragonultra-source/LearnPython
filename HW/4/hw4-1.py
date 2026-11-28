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

# Попытка передвижения чисел во множествах что ставятся не по порядку ({8, 9, 10, 7}):
# tempresult1 = []
# tempresult2 = []

# io = 0
# for i in temp:
#     if i < io:
#         tempresult1.append(i)
#     else:
#         tempresult2.append(i)
#     io = i

# print(tempresult1, tempresult2)
# result = tempresult1 + tempresult2
# print(result)

result = set()
result.update(temp)
print(result)
