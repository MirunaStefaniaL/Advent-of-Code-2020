

def p2():
    v = []
    f = open("f1.txt")
    sir = f.read().replace(":"," ").replace("-"," ")
    sir = sir.split()
    n = len(sir)
    ct = 0
    for i in range(0, n, 4):
        mini = int(sir[i])
        maxi = int(sir[i + 1])
        litera = sir[i + 2]
        s = sir[i + 3]

        ap = 0

        for caracter in s:
            if caracter == litera:
                ap += 1
        if ap >= mini and ap <= maxi:
            ct += 1

    return ct

print(p2())



def p3():
    f = open("f1.txt")
    a = f.readlines()
    n = len(a) #nr linii
    linie = a[0]
    m = len(linie) - 1#nr coloane
    matrix = [['0' for x in range(m)] for y in range(n)]
    for i in range(n):
        linie = a[i]
        for j in range(m):
            x = linie[j]
            matrix[i][j] = x
    line = 0
    column = 0
    ct1 = 0

    while line <= n - 1:
        if (matrix[line][column] == '#'):
            ct1 += 1
        line += 1
        column += 1
        if column >= m:
            column = column % m

    line = 0
    column = 0
    ct2 = 0

    while line <= n - 1:
        if (matrix[line][column] == '#'):
            ct2 += 1
        line += 1
        column += 3
        if column >= m:
            column = column % m

    line = 0
    column = 0
    ct3 = 0

    while line <= n - 1:
        if (matrix[line][column] == '#'):
            ct3 += 1
        line += 1
        column += 5
        if column >= m:
            column = column % m

    line = 0
    column = 0
    ct4 = 0

    while line <= n - 1:
        if (matrix[line][column] == '#'):
            ct4 += 1
        line += 1
        column += 7
        if column >= m:
            column = column % m

    line = 0
    column = 0
    ct5 = 0

    while line <= n - 1:
        if (matrix[line][column] == '#'):
            ct5 += 1
        line += 2
        column += 1
        if column >= m:
            column = column % m

    ct = ct1 * ct2 * ct3 * ct4 * ct5
    print(ct)

p3()
