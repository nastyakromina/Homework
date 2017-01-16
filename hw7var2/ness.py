def open_text():
# Функция считывает файл и разделяет на слова
    with open('Austen Jane. Pride and Prejudice.txt', "r", encoding = "utf-8") as f:
        text = f.read()
        text = text.lower()
        arr = text.split()
        for i, w in enumerate(arr):
            arr[i] = arr[i].strip('.,!?-;:“"”''')
    return arr
#print(open_text())

def isness(word):
# Функция проверяет, заканчивается ли слово на -ness
    Ret = 0
    if len(word) > 4:
        if word[-4:] == 'ness':
             Ret = 1
        else:
            Ret = 0
    return Ret

def AddInList(word, List, Qn):
# Функция записывает слова в список и считает частотность каждого слова
    Yes = 0
    for i in range(len(List)):
        if (List[i] == word):
            Qn[i] +=1
            Yes = 1
    if (Yes == 0):
        List.append(word)
        Qn.append(1)
            
Inarr = open_text()
List = list()
Qn = list()
for i in range (len(Inarr)):
    if isness(Inarr[i]) == 1:
        AddInList(Inarr[i], List, Qn)
print('Количество разных сущ. с суффиксом -ness равно: ' + str(len(List)))
Max = 0
Ind = 0
for i in range(len(List)):
    if Qn[i] > Max:
        Ind = i
        Max = Qn[i]
print('Максимальную частотность имеет слово: ' + List[Ind] + ', с частотностью: ' + str(Qn[Ind]))
