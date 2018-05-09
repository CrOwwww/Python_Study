import urllib.request
import re

url = "http://blog.csdn.net/"
headers = ("User-Aent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")


opener = urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)

data = urllib.request.urlopen(url).read().decode("UTF-8","ignore")
pat = '<h2 class="csdn-tracking-statistics" data-mod="popu_459" data-poputype="feed" data-feed-show="false" data-dsm="post"><a strategy="(*?)"'
rs = re.compile(pat).findall(data)
for i in range(0,len(rs)):
    file = "E:\爬虫文件" + str(i) +".html"
    urllib.request.urlretrieve(rs[i],filename=file)
    print("No: "+str[i]+"  success")
