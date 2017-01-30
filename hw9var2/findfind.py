import re

def open_text():
# Функция считывает файл и разделяет на слова
    with open('txtfind.txt', "r", encoding = "utf-8") as f:
        text = f.read()
        text = text.lower()
        arr = text.split()
        for i, w in enumerate(arr):
            arr[i] = arr[i].strip('.,!?-;:“"”''')
    return arr

def find_in_text():
# Функция создаёт список слов, которые удовлетворяют выражению regex (в этом списке слова могут повторяться)
    List = list()
    regex = '\W?(на(((й((д(у(т(ся)?)?|ёшь(ся)?|ёте?|ём(ся)?|и|ите|я|енный|ены))|ти(сь)?)))|(ш(ёл(ся)?|л(а|и|о)(сь)?|едш(и|(ий|ая|ее)(ся)?)))))\W?'
    words = open_text()
    for i in range (len(words)):
        m = re.search(regex, words[i])
        if m != None:
             List.append(words[i])
    return List

uList = list()
List = find_in_text()
for i in range(len(List)):
    Include = 0
    for j in range(len(uList)):
        if uList[j] == List[i]:
            Include = 1
    if Include == 0:
        print(List[i])
        uList.append(List[i])
