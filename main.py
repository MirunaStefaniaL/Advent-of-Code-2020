

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

def p4():
    f = open("f1.txt")
    a = f.read().split('\n')

    eyecolour = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    n = len(a)
    i = 0
    total = 0
    while i < n:
        pas = a[i]
        while (i < n) and (len(a[i]) != 0 ):
            pas = pas + a[i]
            i += 1
        i += 1 #sarim peste cea goala

        pas.replace(":"," ")
        v1 = pas.find("byr")
        v2 = pas.find("iyr")
        v3 = pas.find("eyr")
        v4 = pas.find("hgt")
        v5 = pas.find("hcl")
        v6 = pas.find("ecl")
        v7 = pas.find("pid")

        if not( (v1 == -1) or (v2 == -1) or (v3 == -1) or (v4 == -1) or (v5 == -1) or (v6 == -1) or (v7 == -1)):
            check1 = check2 = False
            birthyear = pas[v1 + 3 : v1 + 7]
            if birthyear.isalpha():
                if ((int(birthyear) >= 1920) and (int(birthyear) <= 2002)) :
                    check1 = True

            issueyear = pas[v2 + 3 : v2 + 7]
            if issueyear.isalpha():
                if ((int(issueyear) >= 2010) and (int(issueyear) <= 2020)) :
                    check2 = True

            expirationyear = pas[v3 + 3 : v3 + 7]
            if expirationyear.isalpha():
                if ((int(expirationyear) >= 2020) and (int(expirationyear) <= 2030)) :
                    check3 = True

            ######

    print(total)

p4()


###############
def create_dict(s):
    d ={}
    s = s.split()
    for x in s:
        poz = x.find(":")
        key = x[:poz]
        value = x[(poz + 1):]
        d[key] = value
    return d


def verify1(d):
    if len(d.keys()) == 8:
        return 1
    if len(d.keys()) == 7 and "cid" not in d.keys():
        return 1
    return 0


def verify2(d):
    if verify1(d) == 0:
        return 0
    for k in d.keys():
        if k == "byr":
            if int(d[k]) < 1920 or int(d[k]) > 2002:
                return 0
        if k == "iyr":
            if int(d[k]) < 2010 or int(d[k]) > 2020:
                return 0
        if k == "eyr":
            if int(d[k]) < 2020 or int (d[k]) > 2030:
                return 0
        if k == "hgt":
            pozcm = d[k].find("cm")
            pozin = d[k].find("in")
            poz = max(pozin, pozcm)
            if poz == -1:
                return 0
            if poz == pozcm:
                if(int(d[k][:poz]) < 150) or (int(d[k][:poz]) > 193):
                    return 0
            if poz == pozin:
                if (int(d[k][:poz]) < 59) or (int (d[k][:poz]) > 76):
                    return 0
        if k == "hcl":
            if d[k][0] != "#":
                return 0
            if len(d[k]) != 7:
                return 0
            for i in range(1, 6):
                x = d[k][i]
                if x.isdigit() == False and (x <'a' or x >'f'):
                    return 0
        if k =="ecl":
            if d[k] not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
                return 0
        if k =="pid":
            if len(d[k]) != 9:
                return 0
            for i in range(len(d[k])):
                x = d[k][i]
                if x.isdigit() == False:
                    return 0

        return 1

f = open("f1.txt")
L = f.read().split("\n\n")

ct1 = 0 #number of valid passports in task1
ct2 = 0 #number of valid passports in task2

for i in L:
    d = create_dict(i) #we create a new dictionary for each pasport
    #print(d)
    if verify1(d):
        ct1 += 1 #for task1
    if verify2(d):
        ct2 += 1 #for task2

#print(ct1)
print(ct2)
exit()

######


def p5():
    f = open("f1.txt")
    str = f.readlines()
    maxi = 0
    mini = 1030
    f = [0] * 1030
    for s in str:
        l = 0
        r = 127
        for i in range(7):
            m = (r + l)//2
            if s[i] == 'F':
                r = m
            else:
                l = m + 1
        row = r
        l = 0
        r = 7
        for i in range(7, len(s)):
            m = (r + l + 1) // 2
            if s[i] == 'L':
                r = m - 1
            else:
                l = m
        column = l
        id = row * 8 +column
        if id > maxi:
            maxi = id
        if id < mini:
            mini = id

        f[id] = 1
    for i in range(mini, maxi):
        if f[i] == 0:
             print(i)

p5()
