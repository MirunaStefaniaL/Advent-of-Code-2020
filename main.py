

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