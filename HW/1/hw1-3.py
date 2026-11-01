a = int(input("Введите число: "))
if a > 2:
    for i in range(2, a):
        if a % i == 0:
            print("Число", a , "не является простым")
            break
        else:
            print("Число", a , "является простым")
            break
else:
    for i in range(a, 2):
        if a == 0:
            print("Число", a , "не является простым")
            break
        elif a % i == 0:
            print("Число", a , "не является простым")
            break
        else:
            print("Число", a , "является простым")
            break