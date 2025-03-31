while True:
    n = int(input("Введите число: "))
    if n < 1:
        print("Введите положительное число!")
    else:
        for i in range(1, n + 1):
            print(i)
        break

