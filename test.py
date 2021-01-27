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


def b():
    while True:
        print("System On")
        yield
        return '1000'


def c():
    return '1000'

co = hi()
c1 = b()
c2 = c()
print(co, c1, c2)
next(co)
next(c1)
#print(c1.send('1'))
time.sleep(3)
co.send(string)
time.sleep(5)
co.send("Good Sleep")
time.sleep(3)
# co.send(next(c1))
# print(next(c1))




