a = 0
while True:
    number = int(input("Введите число (0 для выхода): "))
    a = a + number
    if number == 0:
        print("Сумма:", a)
        break
    else:
        continue