import time
string = "Github Action Testing. . . "
print(string)


def hi():
    while True:
        print("[ Wait ]")
        x = (yield)
        print(x)


co = hi()
next(co)

co.send(string)
time.sleep(10)
co.send("Good Sleep")



