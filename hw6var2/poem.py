import random
# Эта программа генерирует стихотворение с соблюдением метрической схемы - четырехстопный хорей

def read_words(filename):
    #Эта функция читает слова из файлов
    file = open(filename, "r", encoding = "utf-8")
    arr = []
    for line in file:
        arr += line.strip().split(', ')
    file.close()
    return arr

def verb(number):
    # эта функция возвращает случайный глагол; у неё есть один аргумент - число глагола
    # чтобы получился хороший хорей, нужно подобрать глаголы с ударением на первый слог
    if number == 's':
        return random.choice(read_words("singular_verbs.txt"))
    else:
        return random.choice(read_words("plural_verbs.txt"))

def noun(number):
    # эта функция возвращает случайное существительное; у неё есть один аргумент - число существительного
    # чтобы получился хороший хорей, нужно подобрать слова с ударением на первый слог
    if number == 's':
        return random.choice(read_words("singular_nouns.txt"))
    else:
        return random.choice(read_words("plural_nouns.txt"))

def clinoun():
    # эта функция возвращает случайную из записанных в файле комбинаций: предлог + существительное; у нее нет аргументов
    # чтобы получился хороший хорей, нужно подобрать слова с ударением на первый слог
    return random.choice(read_words("clitic_noun.txt"))

def adverb():
    # эта функция возвращает случайное наречие из файла; у нее нет аргументов
    # чтобы получился хороший хорей, нужно подобрать слова с ударением на первый слог
    return random.choice(read_words("adverb.txt"))

def punctuation():
    # эта функция возвращает случайный знак препинания из небольшого списка; у неё нет аргументов
    return random.choice(read_words("punctuation.txt"))

def verse1():
    # эта функция собирает строчку из предл. с сущ. + сущ. в ед.ч + нареч. + глаг. в ед.ч. + знак препинания
    return clinoun() + ' ' + noun('s') + ' ' + adverb() + ' ' + verb('s') + punctuation()

def verse2():
    # эта функция собирает строчку из сущ. во мн.ч. + глаг. во мн.ч. + нареч. + предл. с сущ. + знак препинания
    return noun('pl') + ' ' + verb('pl') + ' ' + adverb() + ' ' + clinoun() + punctuation()

def verse3():
    # эта функция собирает строчку из сущ. в ед.ч. + нареч. + предл. с сущ. + глаг. в ед.ч. + знак препинания
    return noun('s') + ' ' + adverb() + ' ' + clinoun() + ' ' + verb('s') + punctuation()

def make_verse():
    # эта функция выбирает случайный номер из 1,2,3 и возвращает соответствующую строчку
    verse = random.choice([1,2,3])
    if verse == 1:
        return verse1()
    elif verse == 2:
        return verse2()
    else:
        return verse3()
    
for n in range(4):
    print(make_verse())
