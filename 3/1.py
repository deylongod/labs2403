def read_file(file_path):
    choice = input("Выберите выбор чтения {построчное - П || целиком - Ц} : ")
    while True:
        if choice.lower() == 'ц':
            with open(file_path, 'r', encoding="utf-8") as file:
                print(file.read())
            break
        elif choice.lower() == 'п':
            with open(file_path, 'r', encoding="utf-8") as file:
                for line in file:
                    print(line)
            break
        else:
            print("Выберите выбор чтения {построчное - П || целиком - Ц} : ")


read_file('example.txt')



