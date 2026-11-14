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

# for i in range(5, 0, -1)

#=======================================================================
# LESSON 3
#=======================================================================

# import random
#
# x = random.randint(1,100)

# from random import randint
# x = randint(1,100)

# import random as rnd
# x = rnd.randint(1,100)
# from random import randint

# 1)
# from random import randint


# a, b, n = map(int, input().split())

# arr = []
# for i in range(n):
#     arr.append(randint(a, b))
# count = 0
# for el in arr:
#     des9t = el // 10 % 10
#     if des9t % 2 == 0:
#         count = count + 1

# print(*arr)
# print(count)

# min()
# max()
# len() - определяет длину всего (строки,массива, ...)

# 2)
# n = int(input())
# arr = list(map(int, input().split()))

# even_pos = []
# for el in arr:
#     if el > 0 and el % 2 == 0:
#         even_pos.append(el)

# if len(even_pos) == 0:
#     print(-1, -1)
# else:
#     print(min(even_pos), max(even_pos))

# 3)
# n = int(input())
# arr = list(map(int, input().split()))

# best_val = cur_val = arr[0]
# best_len = cur_len = 1

# for i in range(1, n):
#     if arr[i] == arr[i - 1]:
#         cur_len = cur_len + 1
#     else:
#         if cur_len > best_len:
#             best_val = cur_val
#             best_len = cur_len
#         cur_val = arr[i]
#         cur_len = 1
# print(best_val, best_len)

# arr = [1, 2, 3, 4, 5, 6]

# new_arr = arr[::1]
# print(*new_arr)

# 4)
# n = int(input())
# arr = list(map(int, input().split()))
# print(*arr[::-1])

# 5)
# n = int(input())
# arr = list(map(int, input().split()))

# result = []
# zeros = 0

# for el in arr:
#     if el == 0:
#         zeros = zeros + 1
#     else:
#         flag = False
#         for y in result:
#             if el == y:
#                 flag = True
#                 break
#         if flag:
#             zeros = zeros + 1
#         else:
#             result.append(el)

# for i in range(zeros):
#     result.append(0)
# print(*result)

# 6)
# n = int(input())
# arr = list(map(int, input().split()))

# r = int(input())
# r = r % n

# arr = arr[r:] + arr[:r]
# print(*arr)
