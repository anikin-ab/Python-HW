# Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты
# у своего конкурента?
#
# a) Добавьте игру против бота
#
# b) Подумайте как наделить бота ""интеллектом""
import random

print("игроки P1 and bot:")
print()


sweets = int(input("напишите количество конфет: ")) #всего конфет
max_sweets = 28 #сколько можно взять за раз
count = 0
FirstP = random.randint(0, 1) #определяем, кто первый ходит
print(f"жребий = {FirstP}")
SecondP = 0
if FirstP == 0:
    print(f"первым ходит P1")
    SecondP = 1
    count = 1
else:
    print(f"Первым ходит bot")

P1 = FirstP + 1
bot = SecondP + 1

print(f'всего {sweets} конфет.')
print()

if sweets < max_sweets:
    max_sweets = sweets
# метод игры
#test4

# test 5 - добавляем бота

if sweets > 0:
    while sweets != 0:

        if sweets > 0:
            if bot == 1:
                bot1 = random.randint(1, max_sweets)
                print(f' bot взял {bot1} конфет')
                sweets = sweets - bot1 #забираем конфеты, пишем остаток
            else:
                print(f" P1 возьми не больше {max_sweets} конфет:")  # подставляем первого игрока и макс конфет
                sweets = sweets - int(input())  # забираем конфеты, пишем остаток
            if sweets < 0:
                print("столько конфет нет! попробуте заново.")
                break
            print(f" -- осталось {sweets} конфет --")
            if sweets == 0:
                if bot == 1:
                   print(f"\n*** выиграл bot! ***")  # определяем победителя bot
                else: print(f"\n*** ВЫ выиграли! ***") # определяем победителя P1
            if count % 2 == 0:
                P1 = 1 # чередуем игроков
                bot = 2
            else:
                P1 = 2
                bot = 1
            count += 1
            if sweets < max_sweets: #определяем сколько макс можно взять конфет
                max_sweets = sweets
