adder = [["jff", 'fdf', "fdf", "fdff"]]
print(adder)
adder1 = adder
a = "stop"
while True:

    new_data = [list(map(str, input().split()))]
    adder1 = adder1 + new_data
    for i in adder1:
        print(str(i))

    if input("stop? y/n: ") == "y":
        break
    else:
        continue

def deleter(deller):
    print(f"\n WARNING: Info will be deleted")
    print("search by:")
    s_per = input("\ninput parameter for search to delete: ")
    for i in deller:
        for j in i:
            if j == s_per:
                deller.pop(deller.index(i))
                break
    if s_per == "all":
        deller.clear()
    print(deller)
    print("Info was deleted")

# deleter(adder1)

def deleter2(deller):
    print(f"\n WARNING: Info will be deleted")
    print("search by:")
    dell = deller  #
    global import_file
    while True:
        s_per = input("\ninput parameter for search to delete: ")
        for i in dell:
            for j in i:
                if j == s_per:
                    dell.pop(dell.index(i))
                    break
        if s_per == "all":
            dell.clear()
        print(dell)
        if input("stop? y/n: ") == "y":
            import_file = adder1 #
            # dir_export2(adder1)
            break
        else:
            continue
    print("Info was deleted")

deleter2(adder1)