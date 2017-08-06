from urllib.request import urlopen
html=urlopen("http://news.baidu.com/")
print(html.read())

from urllib.request import urlopen
from bs4 import  BeautifulSoup
html=urlopen("http://news.cctv.com/2017/07/17/ARTInZhLhgkbU5yi5qvKLMy1170717.shtml")
bsojt=BeautifulSoup(html.read())
print(bsojt.body)


