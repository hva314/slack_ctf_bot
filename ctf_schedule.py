#!/usr/bin/python
import urllib2
from bs4 import BeautifulSoup
import texttable

def remove_non_ascii_1(text):
    return ''.join([i if ord(i) < 128 else '\n' for i in text])

URL = "https://ctftime.org/"
response = urllib2.urlopen(URL+"event/list/upcoming")
html = response.read()
soup = BeautifulSoup(html, "lxml")

ctf = [[]]

elements = soup.find_all("td")
links = soup.find_all("a")

for i in range(7):
    
    ctf_info = []
    ctf_link = "N/A"
    
    for k in range(4):
        ctf_info.append( remove_non_ascii_1(elements[7*i+k].get_text()).lstrip().replace("\n","") )

    link = str(links[i+49].get("href"))
    info_URL = URL+link[1:]
    small_soup = BeautifulSoup( urllib2.urlopen(info_URL).read(), "lxml")
    info = small_soup.find_all("p")
    for i in range(10):
        if ("Official URL" in info[i].get_text()):
            ctf_link = info[i].get_text()[14:]

    ctf_info.append(ctf_link)
    ctf.append(ctf_info)

table = texttable.Texttable()
table.add_rows(ctf)
table.set_cols_align(['l','r','r','r','l'])
table.set_cols_width([20,28,15,20,35])
table.header(['CTF','Time','Type','Location','Link'])
print table.draw()
