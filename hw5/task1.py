# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
import re
# Импортируем функцию регулярного выражения

# print("input text:")
# text3 = list(map(str,input().split())) #преобразование строк в список с элементами
#пишем (вводим) текст
text3 = "абв апв аы, авав, аабва, два! абв, три, четыре."
print(f"original text: \n{text3}")

words = "абв"

new_text = re.sub(r'([.,!?])', r' \1 ', text3)  # функц добавляет 1пробел перед знаками
# print(new_text)
text4 = list(map(str,new_text.split())) #преобразуем текст в список
# print(text4)

text3 = [i for i in text4 if words not in i] #убираем слова с words
# print(text3)
new_text2 = " ".join(text3) #переводим список в строку
# print(new_text2)

new_text3 = re.sub(r' ([.,!?])', r'\1', new_text2) #убираем пробел перед знаками
print(f"текст без {words} : \n{new_text3}")
