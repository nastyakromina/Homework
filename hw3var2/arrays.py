arr =[]
word = input("Введите слово: ")
while word:
    arr.append(word)
    word = input ("Введите слово: ")
w = 0
for w in range (len(arr)):
    if len(arr[w]) > 5:
        print (arr[w])
print ("Для завершения работы нажмите ENTER")
ENTER = input ('')
