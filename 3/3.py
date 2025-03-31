def read_file(file_path):
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            choice = input("Выберите выбор чтения {построчное - П  целиком - Ц} : ")
            if choice.lower() == 'ц':
                print(file.read())
            elif choice.lower() == 'п':
                for line in file:
                    print(line)
            else:
                print("Некорректный выбор. Выберите {построчное - П  целиком - Ц}.")
    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден. Пожалуйста, проверьте путь к файлу и попробуйте снова.")

read_file('example.txt')
