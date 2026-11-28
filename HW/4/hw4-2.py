a = set(map(int, input("Введите числа для множества: ").split()))

# Если границ бы не было размер можно было бы угадать:
#  Единственное ограничение - верхняя граница,но ее можно спросить
# c = 0
# n = 0
# k = 0
# for i in a:
#     if c == 0:
#         n = i
#     elif c == len(a) - 1:
#         k = i
#     c = c + 1
# print(k, " - это верхняя граница? (Y/n)")
# anwser = input()
# if anwser == "n":
#     k = int(input("Введите верхнюю границу множества: "))
# print(n, k)

b = set()
result = set()

# Немного был бы изменен блок for:
# for i in range(n, k + 1):
#     b.add(i)
# print(b)

for i in range(1, 21):
    b.add(i)
print(b)

result = b - a
result = list(result)
result = result[::-1]
print("Стертые числа:", *result)



