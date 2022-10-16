# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

#функция кодирования текста
def encode(text):
    encoding = ""  # сохраняет выходную строку

    i = 0
    while i < len(text):
        # подсчитывает количество вхождений символа в индексе `i`
        count = 1

        while i + 1 < len(text) and text[i] == text[i + 1]:
            count = count + 1
            i = i + 1

        # добавляет к результату текущий символ и его количество
        encoding += str(count) + text[i]
        i = i + 1

    return encoding

# функция декодирования
def decode(text2):
    count = "" #принимает счетчик как символ строки
    decode = ""
    for i in text2:
        if i.isdigit():
            count += i # если это цифра, то присвой счетчику эту цифру
        else:
            decode += i * int(count) #если это буква, умножай ее на счетчик
            count = "" #обновляем счетчик
    return decode

#текст берем из файла
if __name__ == '__main__':
    file = "data1.txt"
    new_file = open(file, "r")
    text1 = ""
    for line in new_file:
        text1 += line
    print(f"исходный текст: {text1}")

    print(f"кодированный текст: {encode(text1)}")
    code = encode(text1)
    new_file.close()

    print(f"раскодированный текст: {decode(code)}")
