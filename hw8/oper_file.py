# импорт и экспорт справочника
# работа со справочником


import csv
import os.path # для поиска файла




f_name = "" #имя созд файла
f_namei = ""  #имя импортир файла
import_file = []

# импорт справочника

def dir_import():
    global import_file
    global f_namei
    import_file = []  # обноваляем список
    f_namei = (input("Write filename to open:"))  # вводим название файла, который надо экспортировать
    check_file = os.path.exists(f_namei)  # проверяем, существует ли такой файл
    if check_file:
        # with open(f_namei, newline='', encoding="utf-8") as file:  # импорт Указанного файла
        with open(f_namei, newline='', encoding='cp1251') as file:
            reader = csv.reader(file)
            for row in reader:
                row1 = ";".join(row)
                print(row1.replace(";", " "))
                row2 = row1.split(";")  #каждый элмент ряда записываем отдельно в список
                import_file.append(row2)  #сохраняем импортированный файл в список
        # print(f" \nфайл записан в список {import_file}")  #показываем созданный список целиком
        print("\ndirectory was imported")
        # file.close()
    else:
        print("\nNo such file")  #если файл не найден



# export form list
def dir_export2(direx):
    global f_name
    f_name = (input("Write filename to save it:"))  # вводим название файла для сохран
    print("exporting is in progress")
    with open(f_name, "w") as file:  # запись файла # убрал encoding="utf-8"
        file.seek(0)  # перезаписываем файл
        for i in range(len(direx)):
            #  итерируем список и записываем в файл каждый элемент каждой строки
            file.write("{};{};{};{}\n".format(direx[i][0], direx[i][1], direx[i][2], direx[i][3]))
    print("\ndirectory was exported")
    # file.close()

# функция поиска по справочнику
def search(finder):
    print(f"\nSearching in CREATED file {f_name}")
    print("search by: № Имя Фамилия Телефон")
    s_per = input("\ninput parameter for search: ")
    for i in finder:
        for j in i:
            if j == s_per:
                print(i)
                break
    if s_per == "all":
        for i in finder:
            print(i)


# функция поиска по импортированному справочнику
def search2(finder1):
    print(f"\nSearching in IMPORTED file {f_namei}")
    print("search by: № Имя Фамилия Телефон")
    s_per = input("\ninput parameter for search: ")
    # print("\n#ID Name S_name #Tel")
    for i in finder1:
        for j in i:
            if j == s_per:
                print(i)
                break
    if s_per == "all":
        for i in finder1:
            print(i)



# export one after another

def dir_export3(idx, name, s_name_gen, tel):
    with open("dir_export3.csv", "a") as file:
        file.write("{};{};{};{}\n".format(idx, name, s_name_gen, tel))

def adding(adder):
    adder1 = adder
    while True:
        print("\nДобавь: # Имя Фамилию Телефон (через пробел)")
        new_data = [list(map(str, input().split()))]
        adder1 = adder1 + new_data
        for i in adder1:
            print(i)
        if input("stop? y/n: ") == "y":
            break
        else: continue



