import time
string = "Github Action Testing. . . "
print(string)
a = 1


def hi():
    global a
    while True:
        print("[ Wait ] :", a)
        a += 1
        x = (yield)
        print(x)


co = hi()
next(co)
time.sleep(3)
co.send(string)
time.sleep(10)
co.send("Good Sleep")



