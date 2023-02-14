import requests
from bs4 import BeautifulSoup

url = "https://suumo.jp/chintai/tokyo/sc_shinjuku/?page={}"

target_url = url.format(1)

print(target_url)

r = requests.get(target_url)
soup = BeautifulSoup(r.text, "html.parser")

contents= soup.find_all("div", class_="cassetteitem")
print(len(contents))

content = contents[0]

detail = content.find("div", class_="cassetteitem-detail")
table = content.find("table", class_="cassetteitem_other")

title = detail.find("div", class_ = "cassetteitem_content-title").text

classadress = "cassetteitem_detail-col"

details =[]
for i in range(1,4):
    classadress = "cassetteitem_detail-col" + str(i)
    details.append(classadress)

print(details)

tr_tags = table.find_all("tr", class_="js-cassette_link")
tr_tag = tr_tags[0]

floor, tinkan, shikireikin, menseki = tr_tag.find_all("td")[2:6]

tinryou, kanri = tinkan.find_all("li")

shiki, reikin = shikireikin.find_all("li")

madori, senmenseki = menseki.find_all("li")




print(floor.text, tinryou.text, kanri.text, shiki.text, reikin.text, madori.text, senmenseki.text)