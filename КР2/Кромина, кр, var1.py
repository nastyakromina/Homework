#Задание 1
def open_text_1():
# Функция считывает файл
    with open('islandcorp.xml', "r", encoding = "utf-8") as f:
        Line = 0
        for i in f:
            if i != '</teiHeader>\n':
                Line += 1
            else:
                break
    return Line

def record():
    with open("result1.txt","w", encoding = "utf-8") as f:
        f.write(str(open_text_1()))
        return
    
import re

#Задание 2
def keys():
# Функция записывает слова в список и считает частотность каждого слова
    with open('islandcorp.xml', "r", encoding = "utf-8") as f:
        text = f.read()
        Dic = {}
        reg = '<w lemma=".*?" type="(.*?)">.*?</w>'
        res = re.findall(reg, text)
        #print(res)
        for i in range(len(res)):
            if res[i] not in Dic:
                Dic[res[i]] = 1
            else:
                Dic[res[i]] += 1
        #print(Dic)
        return Dic

def record1():
    with open("result2.txt","w", encoding = "utf-8") as f:
        a = keys()
        for key in a:
            f.write(key + ',' + str(a[key])+ '\n')
record()
record1()
