from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page2.html")
bsobj = BeautifulSoup(html.read())
print(bsobj.h1)

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsobj = BeautifulSoup(html)

namelist = bsobj.findAll("span",{"class":"green"})
for name in namelist:
    print(name.get_text())

html = urlopen("http://172.31.20.233:6260/swagger-ui.html")
bsobj = BeautifulSoup(html)

namelist = bsobj.findAll("span",{"class":"green"})
for name in namelist:
    print(name.get_text())
