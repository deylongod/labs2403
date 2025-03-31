def greet(name):
    print(f"Привет, {name}!")


def square(number):
  return number ** 2


def max_of_two(x, y):
  if x > y:
    return x
  elif x < y:
    return y
  else:
    return "Большего числа нет, они равны"


greet(input("Введите ваше имя: "))
print(square(float(input("Введите ваше число: "))))
print(max_of_two(float(input("Введите первое число: ")), float(input("Введите второе число: "))))


