import codecs
import os
import glob
from bs4 import BeautifulSoup 

directory = os.fsencode("C:\\projects\\FB\\messages\\just_messages")

index = 0
nameDict = {}


for subdir, dirs, files in os.walk(directory):
    for eff in files:
        fstr = eff.decode(encoding="utf8")
        if ".html" in fstr:
            with open("C:\\projects\\FB\\messages\\just_messages\\" + fstr, encoding="utf8") as pf:
                soup = BeautifulSoup(pf, "lxml")
                name = soup.find("span", class_="user").get_text().strip()
                if name != '':
                    if name not in nameDict:
                        nameDict[name] = 1
                    else:
                        nameDict[name] += 1

        else:
            print("=============NOPE==================")
            print(fstr)

print("The following is formatted: 'Name' : 'Count'")
for name in nameDict:
    print(name, " : ", nameDict[name])