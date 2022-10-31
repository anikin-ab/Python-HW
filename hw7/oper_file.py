# импорт и экспорт справочника

import data_prov as prov
import csv


#импорт справочника
def dir_import(x):
    print("#ID Name S_name #Tel")
    # with open('dir_import.csv', newline='') as file: # импорт стороннего файла
    with open('dir_export2.csv', newline='') as file: #импорт созданного файла
        reader = csv.reader(file)
        for row in reader:
            row1 = ";".join(row)
            print(row1.replace(";", " "))
    print("\ndirectory was imported")

# export form list
def dir_export2(direx):
    print("exporting is in progress")
    with open("dir_export2.csv", "w") as file: # дозапись файла
        file.seek(0) # перезаписываем файл
        for i in range(len(direx)):
            # итерируем список и записываем в файл каждый элемент каждой строки
            file.write("{};{};{};{}\n".format(direx[i][0], direx[i][1], direx[i][2], direx[i][3]))
    print("\ndirectory was exported")
    file.close()

# функция поиска

def search(direx2):
    print("search by:\nID"
          "\nName"
          "\ns_Name"
          "\ntel")
    s_per = input("input parameter for search: ")
    for i in direx2:
        for j in i:
            if j == s_per:
                print(i, end=" ")





# export one after another

def dir_export3(idx, name, s_name_gen, tel):
    # print("directory exported")
    with open("dir_export3.csv", "a") as file:
        file.write("{};{};{};{}\n".format(idx, name, s_name_gen, tel))




