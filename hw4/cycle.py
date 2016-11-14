word = input ("Введите слово на кириллице:")
i = 0
while i < len(word):
    if word[i] == 'п' or word[i] == 'о' or word[i] == 'е':
           print (word[i])
    i = i+2
print ("Для завершения работы нажмите ENTER")
ENTER = input ('')
