# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#=======================================================================
# LESSON 1
#=======================================================================

# "abcde" - str()
# 12 - int()
# 12.6 - float()
# True/False - bool
# None

# комментарии

# a = int(input())

# == - равно ли

# if a % 2 == 0:
#     b = a + 5
#     a += 5
#     print("Четное")
# elif a > 15:
#     print("Число больше 15")
# else:
#     print("Не подходит")

# a = int(input())
# while a != 0:
#     print(a)
#     a -= 1

# count = 30
# while True:
#     print(count)
#     if 100 > count > 200:
#         count = 50
#         continue # он пропускает один шаг цикла в котором находится
#         # break  # Выходит из цикла
#     count += 1

# for i in # где мы смотрим:
#     # тело цикла

# for i in range(1, 10):
#     print(i)

# s = "Привет"
# for i in s:
#     if i == "П":
#         continue
#     else:
#         print(i)

# while True:
#     a = int(input())
#     b = int(input())
#     result = a+b
#     print(result)
#     print("Завершить ввод?")
#     c = input()
#     if (c == "y") or (c == "Y"):
#         break

#=======================================================================
# LESSON 2
#=======================================================================

# arr = [0, 1, 2, 3, 4]
# print(arr[4])
# print(arr[-1])
# arr = []
# arr = list()
# arr = [0] * 5
# print(arr)
# for i in arr:
#     print(i)

# 1)
# n = int(input())
# arr = list(range(1, n + 1))
# print(*arr)

# 2)
# x, d, n = map(int, input().split())
# arr = []
# for i in range(n):
#     arr.append(x + i * d)
# print(*arr)

# 3)
# k, n = map(int, input("Введите k и n: ").split())
# if (k > 0) and (k <= 30) and (n > 0) and (n <= 30):
#     l = []
#     for i in range(n, 0, -1):
#         l.append(k ** i)
#     print(*l)
# else:
#     print("n,k не взходят в 0 < n,k <= 30")

# 4)
# n = int(input())
# arr = [1, 1]
# for i in range(2, n):
#     arr.append(arr[i - 1] + arr[i - 2])
# print(*arr)