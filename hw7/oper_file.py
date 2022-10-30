# импорт и экспорт справочника

import data_prov as prov
import csv

def dir_import(x):
    print("#ID Name S_name #Tel")
    # with open('dir_import.csv', newline='') as file: # импорт стороннего файла
    with open('dir_export.csv', newline='') as file: #импорт созданного файла
        reader = csv.reader(file)
        for row in reader:
            row1 = " ".join(row)
            print(row1)
    print("\ndirectory was imported")

# export form list

# def dir_export(direx):
#     print("directory exported")
#     with open("dir_import.csv", "a") as file:
#         # file.write("{}\n".format(direx))
#         for i in range(4):
#             file.write("{}\n".format(direx))

def dir_export(direx):
    print("exporting in progress\n")
    file = open("dir_export.csv", "a")
    with file:
        writer = csv.writer(file)
        writer.writerows(direx)
    print("directory was exported\n")



# export one after another

def dir_export3(idx, name, s_name_gen, tel):
    print("directory exported")
    with open("dir_export2.csv", "a") as file:
        file.write("{} ; {}; {}; {}\n".format(idx, name, s_name_gen, tel))




