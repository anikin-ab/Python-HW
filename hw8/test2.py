finder = "0 Olde NOw 89277616072"
x = 0

def oo(a):
    global x
    # global y
    x = a
    # y = b
    for i in finder:
        if i == "0":
            print("its", finder)
            x += 1


# x = 0
def on(a):
    return x + 2

oo(0)
print(on(0))