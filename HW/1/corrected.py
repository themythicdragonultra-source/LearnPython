# 1) Убрал else: continue
# a = 0
# while True:
#     number =  int(input("Введите число (0 для выхода): "))
#     a = a + number
#     if number == 0:
#         print("Сумма:", a)
#         break


# 2)
# a = int(input("Введите число: "))
# for  i in range (1, 11):
#     print(a, "x", i, "=", a * i)

# 3) Else поставил вместе с for, чтобы если не делилось, сразу не выходило
# a = int(input("Введите число: "))
# if  a > 0:
#     if (a == 1):
#         print("Число не является простым")
#     elif (a == 2):
#         print("Число является простым")
#     else:
#         for i in range(2, a):
#             if a % i == 0:
#                 print("Число не является простым")
#                 break
#         else:
#             print("Число является простым")
# else:
#     print("Число не является простым")
    
# более быстрый метод

# a = int(input("Введите число: "))
# if a >= 2:
#     if a == 2:
#         print("Число является простым")
#     else:
#         for i in range(2, int(a ** 0.5) + 1):
#             if a % i == 0:
#                 print("Число не является простым")
#                 break
#         else:
#             print("Число является простым")
# else:
#     print("Число не является простым")