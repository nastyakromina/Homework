import os
import re
def main():
    Sum = 0
    for root, dirs, files in os.walk('.'):
        for d in dirs:
            cir = 0
            for i in range(len(d)):
                a = re.search(r'[а-яёЁ А-Я]+',d[i])
                if a == None:
                    cir = 1
            if cir == 0:
                Sum += 1
    return Sum

print(main()) 
