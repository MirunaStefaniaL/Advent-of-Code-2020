

def p1():
    v = []
    f = open("f1.txt")
    for x in f.read().split():
        val = int(x)
        v.append(val)
    for i in range(len(v)):
        for j in range(i + 1, len(v)):
            for k in range(j + 1, len(v)):
                if v[i] + v[j] + v[k] == 2020:
                    return v[i] * v[j] * v[k]
    f.close()

print(p1())