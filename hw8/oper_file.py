# импорт и экспорт справочника


import csv
import os.path

# global fwi
# file_was_imp = 0
fwi = 0
global import_file
import_file = []

#импорт справочника
def dir_import():
    global fwi
    fwi = 0
    # file_was_imp = 0
    print("1 import", fwi)
    global import_file
    import_file = []
    f_name = (input("Write filename to open:")) # вводим название файла, который надо экспортировать
    check_file = os.path.exists(f_name) # проверяем, существует ли такой файл
    if check_file:
        print("#ID Name S_name #Tel")
        with open(f_name, newline='') as file: # импорт Указанного файла
            reader = csv.reader(file)
            for row in reader:
                row1 = ";".join(row)
                print(row1.replace(";", " "))
                row2 = row1.replace(";", " ")
                import_file.append(row2)
        print(f" \nфайл записан в список {import_file}")

        fwi = 1
        if fwi == 1:
            print("\ndirectory was imported")
        # print(file_was_imp)
        file.close()
    else: print("\nNo such file")
    return fwi


# export form list
def dir_export2(direx):
    f_name = (input("Write filename to save it:"))  # вводим название файла для сохран
    print("exporting is in progress")
    with open(f_name, "w") as file: # запись файла
        file.seek(0) # перезаписываем файл
        for i in range(len(direx)):
            # итерируем список и записываем в файл каждый элемент каждой строки
            file.write("{};{};{};{}\n".format(direx[i][0], direx[i][1], direx[i][2], direx[i][3]))
    print("\ndirectory was exported")
    file.close()

# функция поиска по созданному справочнику

def search(finder):

    print(f"Searching in file", fwi)
    print("search by:\nID"
          "\nName"
          "\ns_Name"
          "\ntel"
          "\nall")
    find_w = "ID, Name, s_Name, tel, all"
    s_per = input("\ninput parameter for search: ")
    print("\n#ID Name S_name #Tel")
    for i in finder:
        for j in i:
            if j == s_per:
                print(i)
    if s_per == "all":
        for i in finder:
            print(i)





# export one after another

def dir_export3(idx, name, s_name_gen, tel):
    # print("directory exported")
    with open("dir_export3.csv", "a") as file:
        file.write("{};{};{};{}\n".format(idx, name, s_name_gen, tel))




