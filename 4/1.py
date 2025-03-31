import math, datetime

while True:
    try:
        n = int(input("Введите число: "))
        if n < 0:
            print("Корень из отрицательного числа не существует")
            continue
        print(f"Корень числа {n} = {math.sqrt(n)}" + "\n" + f"Текущая дата и время: {datetime.datetime.now()}")
        break
    except ValueError:
        print("Введены некорректные значения, попробуйте снова")
