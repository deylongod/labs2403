def write_to_file():
    user_input = input("Введите текст: ")
    with open("user_input.txt", "a", encoding='utf-8') as file:
        file.write(user_input + "\n")
    print("Текст успешно записан в файл user_input.txt")


write_to_file()
