# импорт и экспорт справочника


import csv
import os.path



fwi4 = 0

import_file = []

# импорт справочника

def dir_import(fwi):
    global fwi4
    fwi4 = fwi
    print("1 import", fwi4)
    global import_file
    row2 = []

    f_name = (input("Write filename to open:"))  # вводим название файла, который надо экспортировать
    check_file = os.path.exists(f_name)  # проверяем, существует ли такой файл
    if check_file:
        print("#ID Name S_name #Tel")
        with open(f_name, newline='', encoding="utf-8") as file:  # импорт Указанного файла
            reader = csv.reader(file)
            for row in reader:
                row1 = ";".join(row)
                print(row1.replace(";", " "))
                row2 = row1.split(";")  #каждый элмент ряда записываем отдельно в список
                import_file.append(row2)  #сохраняем импортированный файл в список
        print(f" \nфайл записан в список {import_file}")

        fwi4 = 1
        if fwi4 == 1:
            print("\ndirectory was imported")
        # file.close()

    else:
        print("\nNo such file")
    return fwi4


# export form list
def dir_export2(direx):
    f_name = (input("Write filename to save it:"))  # вводим название файла для сохран
    print("exporting is in progress")
    with open(f_name, "w", encoding="utf-8") as file:  # запись файла
        file.seek(0)  # перезаписываем файл
        for i in range(len(direx)):
            #  итерируем список и записываем в файл каждый элемент каждой строки
            file.write("{};{};{};{}\n".format(direx[i][0], direx[i][1], direx[i][2], direx[i][3]))
    print("\ndirectory was exported")
    file.close()

# функция поиска по созданному справочнику
def search(finder):
    global fwi4
    if fwi4 == 0:
        print(f"Searching in created file", fwi4)
    else: print("Searching in imported file", fwi4)
    print("search by:\nID"
          "\nName"
          "\ns_Name"
          "\ntel"
          "\nall")
    s_per = input("\ninput parameter for search: ")
    print("\n#ID Name S_name #Tel")

    # for i in finder:
    #     if i == s_per:
    #         print(i)

    for i in finder:
        for j in i:
            if j == s_per:
                print(i)
                break

    if s_per == "all":
        for i in finder:
            print(i)





# export one after another

def dir_export3(idx, name, s_name_gen, tel):
    # print("directory exported")
    with open("dir_export3.csv", "a") as file:
        file.write("{};{};{};{}\n".format(idx, name, s_name_gen, tel))
