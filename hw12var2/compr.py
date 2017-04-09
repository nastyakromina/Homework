def open_text():
    with open('green.txt', "r", encoding = "utf-8") as f:
        text = f.read()
        arr = text.split('.')
    return arr
def deli():
    txt = open_text()
    for i, w in enumerate(txt):
        for s in '.,!?-;:“"”''()«»–':
            txt[i] = txt[i].replace(s, "")
    return txt
def des():
    txt = deli()
    dlina = [x for x in txt if len(x.split()) > 10]
    return dlina
def big():
    txt = des()
    f = []
    for i in txt:
        f += [x for x in i.split() if x[0].isupper()]
    return f
print (big())
