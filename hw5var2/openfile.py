file = open("text.txt", "r", encoding = "utf-8")
lmin = lmax = len(file.readline())
for line in file:
    lp = len(line)
    if lp > 0:
        if lmin > lp:
            lmin = lp
        if lmax < lp:
            lmax = lp
print (lmax / lmin) 

