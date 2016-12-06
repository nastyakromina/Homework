#1
file = open ("цитаты1.txt", "r", encoding = "utf-8")
stroki = 0
for line in file:
    arr = line.split('—')
    ar = arr[0].split()
    if len(arr) > 0:
        if len(ar) < 10:
            print (arr[0])
#    if "разум" in line:
#        stroki = stroki + 1
#    print (stroki)
