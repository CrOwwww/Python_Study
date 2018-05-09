import urllib.request
url = "http://blog.csdn.net/weiwie_pig/article/details/52123738"
opener = urllib.request.build_opener()
opener.addheaders = [headers]
data = opener.open(url).read()
fh = open("文件名称","wb")
fh.write(data)
fh.close()
