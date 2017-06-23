import re
import requests
from bs4 import BeautifulSoup
import os
headers = {'User-agent': 'Mozilla/5.0'}

userWeb = input("Website: ")

r = requests.get(userWeb, headers=headers)
data = r.text
soup = BeautifulSoup(data, "lxml")

print(soup)



for link in soup.find_all('img'):

    image = link.get("src")
    imag = image.replace("image", "original")
    # print(imag.find("http"))
    if(imag.find("http")==0):
        print(imag)

        imgSplit=os.path.split(imag)
        imgNam = imgSplit[1]+".jpg"
        r2=requests.get(imag,headers=headers)
        # print(imgNam)
        with open(imgNam,"wb") as f:
            f.write(r2.content)




