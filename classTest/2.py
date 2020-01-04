class AClass:
    a = 1
    b = 1.0
    c = "1"


def printType(v): return print(type(v))


if __name__ == '__main__':
    printType(AClass.a)
    printType(AClass.b)
    printType(AClass.c)
