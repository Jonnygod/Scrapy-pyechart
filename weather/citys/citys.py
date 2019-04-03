import urllib.request
from bs4 import BeautifulSoup
import sys
import time
import codecs

class Item(object):
    pin = None
    title = None
    shipin = None
    shititle = None
    protitle = None


class Citys(object):
    def __init__(self):
        self.url = 'https://www.tianqi.com/chinacity.html'
        self.items = self.spider(self.url)
        self.piplines(self.items)

    def spider(self,url):
        items =[]
        htmlContent = self.getResponseContent(url)
        soup = BeautifulSoup(htmlContent, 'lxml')
        tagss = soup.find('div', attrs={'class':'citybox'})
        tags = tagss.find_all('a')
        tags2 = tagss.find_all('h2') #市级
        tags3 = tagss.find_all('h3') #市级
        # print(tags2)
        for tag in tags:
            item = Item()
            item.pin = tag.get('href').strip('/')       #只要获取这个拼音即可
            item.title = tag.get_text().strip()
            items.append(item)
        for tag in tags3:
            item = Item()
            item.shipin = tag.a.get('href').strip('/')       #只要获取这个拼音即可
            item.shititle = tag.get_text().strip()
            items.append(item)
        for tag in tags2:
            item = Item()
            item.protitle = tag.get_text().strip()
            items.append(item)
        return items


    def piplines(self,items):
        for item in items:
            with codecs.open('./city/citys.txt','a','utf8') as fp:
                fp.write(' "%s",\n' % (item.pin))
            with codecs.open('./city/pins.txt','a','utf8') as fd:
                fd.write(" '%s':'%s',\n" % (item.pin, item.pin))
            with codecs.open('./shi/shicitys.txt','a','utf8') as fp2:
                fp2.write(' "%s",\n' %(item.shipin))
            with codecs.open('./shi/shipins.txt','a','utf8') as fd2:
                fd2.write(" '%s':'%s',\n" %(item.shipin,item.shipin))
            with codecs.open('./city/provin.txt','a','utf8') as fd3:
                fd3.write(" '%s',\n" %(item.protitle))



    def getResponseContent(self, url):
        # headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"}
        try:
            # print(url)
            response = urllib.request.urlopen(url)
            # print(response.read())
        except:
            print('错误')
            time.sleep(1)
            sys.exit(-1)
        else:
            return response.read()

def No():
    with codecs.open('./city/citys.txt', 'w', 'utf8') as fp:
        fp.truncate()
        fp.close()
    with codecs.open('./city/pins.txt', 'w', 'utf8') as fp2:
        fp2.truncate()
        fp2.close()
    with codecs.open('./city/provin.txt', 'w', 'utf8') as fp5:
        fp5.truncate()
        fp5.close()
    with codecs.open('./shi/shicitys.txt', 'w', 'utf8') as fp3:
        fp3.truncate()
        fp3.close()
    with codecs.open('./shi/shipins.txt', 'w', 'utf8') as fp4:
        fp4.truncate()
        fp4.close()

def wash():
    with open("./city/citys.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    with open("./city/citys.txt", "w", encoding="utf-8") as f_a:
        for line in lines:
            if "None" in line:
                continue
            f_a.write(line)
        f_a.close()

    with open("./city/pins.txt", "r", encoding="utf-8") as f2:
        lines = f2.readlines()
    with open("./city/pins.txt", "w", encoding="utf-8") as f_b:
        for line in lines:
            if "None" in line:
                continue
            f_b.write(line)
        f_b.close()

    with open("./shi/shicitys.txt", "r", encoding="utf-8") as f3:
        lines = f3.readlines()
    with open("./shi/shicitys.txt", "w", encoding="utf-8") as f_c:
        for line in lines:
            if "None" in line:
                continue
            f_c.write(line)
        f_c.close()

    with open("./shi/shipins.txt", "r", encoding="utf-8") as f4:
        lines = f4.readlines()
    with open("./shi/shipins.txt", "w", encoding="utf-8") as f_d:
        for line in lines:
            if "None" in line:
                continue
            f_d.write(line)
        f_d.close()

    with open("./city/provin.txt", "r", encoding="utf-8") as f5:
        lines = f5.readlines()
    with open("./city/provin.txt", "w", encoding="utf-8") as f_v:
        for line in lines:
            if "None" in line:
                continue
            f_v.write(line)
        f_v.close()




if __name__ == '__main__':
    No()
    GTI = Citys()
    wash()





