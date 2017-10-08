import urllib.request
import re
import os
#
#   Программа загрузки страниц сайта
#
def download_page(pageUrl): #
    req = urllib.request.Request(pageUrl)
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
    except:
        print('Error at', pageUrl)
    return html
#
#   Программа выделения заголовков
#
def find_post(page):
    reg = re.compile('<h2 class="entry-title">.*?<a href=".*?"', flags= re.DOTALL)
    titles = reg.findall(page)
    new = []
    for title in titles:
        m = re.sub('<h2 class="entry-title">.*?<a href="', '', title)
        m = re.sub('"', '', m)
        new.append(m)
#    print(new)
    return new
#
#   Программа создания файлов с разметкой xml
#
def do_xml(root, mon, real_text, topik, pfile, year):
    path = root+'/mystem-xml/'+year+'/'+mon
    try:
        os.makedirs(path)
    except:
        None
    ofile = path + r'/article'+str(topik)+'.xml'
    os.system(r'\mystem.exe' + ' ' +'-nid' + ' ' + pfile +' ' + ofile)
    return
#
#   Программа создания файлов с разметкой txt
#
def do_txt(root, mon, real_text, topik, pfile, year):
    path = root+'/mystem-plain/'+year+'/'+mon
    try:
        os.makedirs(path)
    except:
        None
    ofile = path + r'/article'+str(topik)+'.txt'
    os.system(r'\mystem.exe' + ' ' +'-nid' + ' ' + pfile +' ' + ofile)
    return
#
#   Программа выделения атрибутов поста
#
def get_meta(topik, new, root, cfile):
    for i in new:
        text = download_page(i)
        dt = re.compile('<span class="entry-date">.*?</span>', flags= re.DOTALL)
        dat = str(dt.findall(text))
        d = re.sub('<span class="entry-date">', '', dat)
        d = re.sub('</span>', '', d) 
        d = re.sub(r'\[\'', '',d)
        d = re.sub(r'\'\]', '', d) #дата
        year = d[-4::] #год
        mon = d[-7:-5] #месяц
        te = re.compile('<div class="entry-content">.*?</div>', flags= re.DOTALL)
        tex = str(te.findall(text))
        t = re.sub('<.*?>', '', tex)
        t = re.sub(r'\\n', '', t)
        t = re.sub(r'\\t', '', t)
        t = re.sub('&#8212;', '-', t)
        t = re.sub(r'\\xa0', '', t)
        t = re.sub(r'\[\'', '',t)
        t = re.sub(r'\'\]', '', t)
        t = re.sub('&#171;', '«',t)
        t = re.sub('&#187;', '»',t)
        t = re.sub('&nbsp;', '',t) #текст поста
        aut = re.compile('<span class="author vcard">.*?</span>', flags= re.DOTALL)
        autr = str(aut.findall(text))
        autt = re.compile('title="Посмотреть все записи автора .*?">.*?</a>')
        author = str(autt.findall(autr))
        a = re.sub('title="Посмотреть все записи автора .*?">', '', author)
        a = re.sub('</a>', '', a) 
        a = re.sub(r'\[\'', '',a)
        a = re.sub(r'\'\]', '', a) #автор
        nam = re.compile('<h1 class="entry-title">.*?</h1>', flags= re.DOTALL)
        name = str(nam.findall(text))
        n = re.sub('<h1 class="entry-title">', '', name)
        n = re.sub('</h1>', '', n) 
        n = re.sub(r'\[\'', '',n)
        n = re.sub(r'\'\]', '', n) #название статьи
        top = re.compile('<div class="entry-utility">.*?</a>', flags= re.DOTALL)
        topi = str(top.findall(text))
        topy = re.compile('rel="category">.*?</a>', flags= re.DOTALL)
        topic = str(topy.findall(topi))
        to = re.sub('rel="category">', '', topic)
        to = re.sub('</a>', '', to) 
        to = re.sub(r'\[\'', '',to)
        to = re.sub(r'\'\]', '', to) #категории(topics)
        t_ap = '@au %s\n@ti %s\n@da %s\n@topic %s\n@url URL %s\n'
        t_ap_s = t_ap % (a, n, d, to, i)
        real_text = t_ap_s + '\n' + t
        path = root+'/plain/'+year+'/'+mon
        try:
            os.makedirs(path)
        except:
            None
        pfile = path + '/article'+str(topik)+'.txt'
        file = open(pfile, "w", encoding = "utf-8")
        file.write(real_text)
        file.close()
        metacsv = '%s\t%s\t\t\t%s\t%s\tпублицистика\t\t\t%s\t\tнейтральный\tн-возраст\tн-уровень\tрайонная\t%s\tВестник\t\t%s\tгазета\tРоссия\tШарканский регион\tru\n'
        cfile.write(metacsv % (pfile, a, n, d, to, i, year)) #созание csv файла с метаданными
        do_xml(root, mon, real_text, topik, pfile, year)
        do_txt(root, mon, real_text, topik, pfile, year)
        topik += 1
    return topik

#
#   Основная программа
#
root = 'vestnik'
try:
    os.mkdir(root)  #   Создание корневойпапки
except:
    None
csvroot =  root + '/metadata.csv'
commonUrl = 'http://www.vestnik.udm.net/?paged='
try:
    os.remove(csvroot)  #   Удаление файла, для возможности повторного запуска программы
except:
    None
cfile = open(csvroot, "a", encoding = "utf-8")
topik = 1
#   Цикл вызова страниц с заголовками топиков
for i in range(1, 122):
    pageUrl = commonUrl + str(i)
    try:
        text = download_page(pageUrl)
        post = find_post(text)
        topik = get_meta(topik, post, root, cfile)
    except:
        print("Обработка закончена")
cfile.close()
    
