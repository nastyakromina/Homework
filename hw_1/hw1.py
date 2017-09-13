import urllib.request  # импортируем модуль
req = urllib.request.Request('http://www.vestnik.udm.net/')
with urllib.request.urlopen(req) as response:
   html = response.read().decode('utf-8')
import re
regTitle = re.compile('<h2 class="entry-title">.*?</h2>', flags= re.DOTALL)
titles = regTitle.findall(html)
new_titles = []
regTag = re.compile('<.*?>', re.DOTALL)
regSpace = re.compile('\s{2,}', re.DOTALL)
for t in titles:
    clean_t = regSpace.sub("", t)
    clean_t = regTag.sub("", clean_t)
    new_titles.append(clean_t)
f = open('text.txt', 'w', encoding = "utf-8")
for i in range(len(new_titles)):
    f.write(new_titles[i]+'\n')
f.close()
