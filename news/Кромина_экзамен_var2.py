#1
import re
import os
import csv

def first():
    reg = '<se>'
    for i in os.listdir('.'): #смотрим файлы в текущей папке
        if i.endswith('.xhtml'):
            m = []
            with open(os.path.join('.', i), 'r', encoding = 'utf-8') as t: #все файлы перекодированы в utf-8 
                text = t.read()
            for t in re.findall(reg, text): #находим регулярное выражение в тексте
                m.append(t) #добавляем в массив
            with open('new_text.txt', 'a', encoding = 'utf-8') as f: #записываем в файл
                f.write(i+'\t'+str(len(m)) + '\n')
first()

#2
def second():
    for i in os.listdir('.'):
        reg = '<meta content="(\w*)" name="author"></meta>' #находим автора
        with open(os.path.join('.', i), 'r', encoding = 'utf-8') as t:
            text = t.read()
            for t in re.findall(reg, text): #для каждого автора находим тематику текста
                if re.search('<meta content="(\w*)" name="topic"></meta>', text):
                    with open('table.csv', 'a', encoding = 'utf-8') as f:
                        f.write(i+','+re.search('<meta content="(\w*)" name="topic"></meta>', text))
second()            
        
        

