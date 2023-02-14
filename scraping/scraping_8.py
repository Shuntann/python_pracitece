from time import sleep
import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = "https://suumo.jp/chintai/tokyo/sc_shinjuku/?page={}"

d_list=[]

for i in range(1,4):
    target_url = url.format(i)
    r = requests.get(target_url)

    soup = BeautifulSoup(r.text, "html.parser")

    sleep(1)

    contents = soup.find_all("div", class_="cassetteitem")

    for content in contents:
        details = content.find("div", class_="cassetteitem-detail")
        table = content.find("table", class_="cassetteitem_other")

        title = content.find("div", class_="cassetteitem_content-title").text
        adress = content.find("li", class_="cassetteitem_detail-col1").text
        access = content.find("li", class_="cassetteitem_detail-col2").text
        ages = content.find("li", class_="cassetteitem_detail-col2").text

        tr_tags = table.find_all("tr", class_="js-cassette_link")

        for tr_tag in tr_tags:
            floor, money1, money2, M2 = tr_tag.find_all("td")[2:6]

            chin, kan = money1.find_all("li")
            shiki, rei =money2.find_all("li")
            madori, sen = M2.find_all("li")

            dic ={"title":title, "adress":adress, "access":access, "ages":ages, "floor":floor.text, "chin":chin.text, "kan":kan.text,"shiki":shiki.text, "rei":rei.text, "madori":madori.text, "sen":sen.text}

            d_list.append(dic)

pprint(d_list[11])
print()
pprint(d_list[1])
