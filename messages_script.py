import codecs
import os
import glob
from bs4 import BeautifulSoup 

directory = os.fsencode("C:\\projects\\FB\\messages\\just_messages")

index = 0
nameList = []

#for filename in os.listdir(directory):
for subdir, dirs, files in os.walk(directory):
    for eff in files:
        fstr = eff.decode(encoding="utf8")
        if ".html" in fstr:
            with open("C:\\projects\\FB\\messages\\just_messages\\" + fstr, encoding="utf8") as pf:
                soup = BeautifulSoup(pf, "lxml")
                name = soup.find("span", class_="user").get_text().strip()
                print(name)
                #print(soup.title)
                #title = soup.title.get_text()
                #print(title[18:])
                #print("index = ", index)
                #nameList.append(soup.title.get_text())
                #index = index + 1
                #if(index == 218):
                #break
        else:
            print("=============NOPE==================")
            print(fstr)

for name in nameList:
    print(name)