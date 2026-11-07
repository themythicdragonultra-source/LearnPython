a = int(input("Введите число: "))
if  a > 0:
    if (a == 1):
        print("Число не является простым")
    elif (a == 2):
        print("Число является простым")
    else:
        for i in range(2, a):
            if a % i == 0:
                print("Число не является простым")
                break
        else:
            print("Число является простым")
else:
    print("Число не является простым")