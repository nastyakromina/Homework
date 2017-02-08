import re

def get_text(fn):
    a = []
    with open(fn, 'r', encoding = "utf-8") as f:
        for line in f:
            a.append(line)
    return a
def main():
    text = get_text('Санкт-Петербург — Википедия.html')
    reg = '<div><a [^>]*?>(UTC[+-]?\d{1,2}:?\d{0,2})</a>'
    for ti in text:
        m = re.search(reg, ti)
        if m != None:
            print(m.group(1))
            return m.group(1)
def record():
    r = main()
    f = open("result.txt","w")
    f.write("Часовой пояс - " + r)
    f.close()
    
record()
