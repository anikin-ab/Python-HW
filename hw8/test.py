adder = [["jff", 'fdf', "fdf", "fdff"]]
print(adder)
# new_data = [list(map(str, input().split()))]
# adder1 = adder + new_data
# for i in adder1:
#     print(i)
adder1 = adder
a = "stop"
while True:
    # adder1 = adder
    # if input() == "stop": break
    new_data = [list(map(str, input().split()))]
    adder1 = adder1 + new_data
    for i in adder1:
        print(str(i))

    if input("stop? y/n: ") == "y":
        break
    else:
        continue

