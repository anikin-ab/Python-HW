# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

new_file = open("eql.txt", "r+")
read_f = new_file.read()
print(f" Данные из файла: ")
print(read_f)
# print(list(read_f))

new_file2 = open("eql1.txt", "r+")
read_f2 = new_file2.read()
print(f" Данные из файла 2: ")
print(read_f2)

f = ""
list3 = []
for i in range(len(read_f)):
    if read_f[i] == "x":
        f = read_f[(i - 2):i]
        list3.append(int(f))
        print(f, end=" ")
print()

list4 = []
f2 = ""
for i in range(len(read_f2)):
    if read_f2[i] == "x":
        f2 = read_f2[(i - 2):i]
        list4.append(int(f2))
        print(f2, end=" ")
print()
print(list3)
print(list4)

# далее не знаю как решить до конца