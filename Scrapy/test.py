import urllib.request
import re


data = "aaaaannniuif"
pat = "an"


 #rest = re.compile(pat).findall(data)
rest = re.compile(pat).findall(data)
print(rest)
