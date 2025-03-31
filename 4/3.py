import my_package.text_module as tm
import my_package.number_module as nm

print(tm.reverse(input("Введите текст: ")))
print(tm.isPalindrome(input("Введите текст: ")))

print(nm.isEven(int(input("Введите число: "))))
print(nm.isPrime(int(input("Введите число:"
                           " "))))