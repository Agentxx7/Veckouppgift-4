def uppgift4a():
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if x == y:
                s += "#"
            else:
                s += "."
        print(s)


def uppgift4b():
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if x == y + 1:
                s += "#"
            else:
                s += "."
        print(s)


def uppgift4c():
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if x == 9 - y:
                s += "#"
            else:
                s += "."
        print(s)


def uppgift4d():
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if y == 3:
                s += "#"
            else:
                s += "."
        print(s)


def uppgift4e():
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if x == 4:
                s += "#"
            else:
                s += "."
        print(s)


def uppgift4f():
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if y == 1 or y == 6 or x == 1 or x == 8:
                s += "#"
            else:
                s += "."
        print(s)


def uppgift4g():
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if x <= y:
                s += "#"
            else:
                s += "."
        print(s)


def uppgift4h():
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if x >= y:
                s += "#"
            else:
                s += "."
        print(s)


def uppgift4i():
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if x == y or x == 9 - y:
                s += "#"
            else:
                s += "."
        print(s)


def uppgift4j():
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if x >= y and x <= 9 - y:
                s += "#"
            else:
                s += "."
        print(s)