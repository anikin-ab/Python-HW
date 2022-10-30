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
    print("directory exported")
    with open("dir_export2.csv", "a") as file:
        # file.write("{}\n".format(direx))
        for i in range(len(direx)):
            # file.write("{}\n".format(direx))
            # итерируем список и записываем в файл каждый элемент каждой строки
            file.write("{};{};{};{}\n".format(direx[i][0], direx[i][1], direx[i][2], direx[i][3]))


# not used

# def dir_export(direx):
#     print("exporting in progress\n")
#     file = open("dir_export.csv", "a")
#     with file:
#         writer = csv.writer(file)
#         writer.writerows(direx)
#     print("directory was exported\n")



# export one after another

def dir_export3(idx, name, s_name_gen, tel):
    # print("directory exported")
    with open("dir_export3.csv", "a") as file:
        file.write("{};{};{};{}\n".format(idx, name, s_name_gen, tel))




