import os
import re
def papka():
    folder = [f for f in os.listdir('.')if not re.search(r'[0-9]+',f)if os.path.isfile(f)]
    print(len(folder))
    return folder
papka()

def dop():
    arr = []
    astr = 0
    exist = 0
    folder = [f for f in os.listdir('.')]
    for p in range(len(folder)):
        for j in range(len(folder[p])):
            if folder[p][j] == '.':
                astr = folder[p][0:j]
                exist = 0
                for k in range(len(arr)):
                    if arr[k] == astr:
                        exist = 1
                if exist == 0:
                    arr.append(astr)
    return arr
print(dop())
            
