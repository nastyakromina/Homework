import re

def open_text():
    with open('Викинги — Википедия.html', "r", encoding = "utf-8") as f:
        text = f.read()
    return text

def replacement():
    result1 = re.sub('викинг((и|у|е|а(х|м(и)?)?)|о(в|м)?)?[^\w]', 'бурундук\\1', open_text())
    result2 = re.sub('Викинг((и|у|е|а(х|м(и)?)?)|о(в|м)?)?[^\w]', 'Бурундук\\1', result1)
    return result2

def record():
    r = replacement()
    f = open("result.txt","w", encoding = "utf-8")
    f.write(r)
    f.close()
    return f 

record()
