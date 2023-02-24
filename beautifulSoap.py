import requests
import json
from bs4 import BeautifulSoup

URL = "https://www.cnnindonesia.com/olahraga"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
latest = soup.find(class_="box feed")

title = latest.find_all("h2", class_="title") 
category = latest.find_all("span", class_="kanal")
picture = latest.find_all('img')
link = latest.find_all('article')

result = []
for i in range(len(title)):
    result.append({"id":i+1, "judul": title[i].text.strip(), "kategori":category[i - int(1)].text.strip(), "picture":str(picture[i]).split('"')[3], "link":str(link[i]).split('"')[15]})

HasilJSON = json.dumps(result)
JSONFile = open("BeritaTerkini.json", "w")
JSONFile.write(HasilJSON)
JSONFile.close()
