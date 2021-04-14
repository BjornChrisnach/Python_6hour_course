# global vs local
var = 9
loop = True


def func(x):
    global loop

    loop = 7

    if x == 5:
        return newVar


def otherFunc():
    newVar = 5


func(2)
print(loop)
