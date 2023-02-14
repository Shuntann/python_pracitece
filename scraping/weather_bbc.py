import requests
from bs4 import BeautifulSoup
from time import sleep
from pprint import pprint
import pandas as pd
import sys,os
import pyautogui as pg

sys.path.append("../")
import file_fomula


#import urllib.parse

#EnglandAddress = "https://www.bbc.co.uk/weather"


#cardiff="2653822"
#Lodon = "2643743"
#Tokyo = "1850147"
#Sapporo = "2128295"

#Address = urllib.parse.urljoin(EnglandAddress,cardiff)

#print(Address)



url = "https://www.bbc.co.uk/weather/2653822"

r=requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")

d_list=[]



sleep(1)

home = soup.find("div", class_="wr-unit--temperature--c wr-unit--windspeed--mph")

forecast = home.find("div", class_="wr-forecast gs-u-box-size wr-forecast--no-day")

li=forecast.find("ol",class_="wr-day-carousel__list wr-js-day-carousel-list clearfix")

weeks = []
weeks = li.find_all("li")



today = weeks[0].find("span", class_="wr-date").text
weather_type = weeks[0].find("div",class_="wr-weather-type__text").text
weather_detail=weeks[0].find("div",class_="wr-day__details__weather-type-description").text
high = weeks[0].find("span", class_="wr-value--temperature--c").text
wind = weeks[0].find("span",class_="wr-value--windspeed wr-value--windspeed--mph").text

dic = {"day":today, "weather_type":weather_type, "weather_detail":weather_detail, "tem":high, "wind":wind}
if "rain" in dic["weather_detail"]:
    reputation = "傘持っていけ"
    print(reputation)
else:
    reputation = "傘邪魔"
    print(reputation)

dic.update(reputation = reputation)

d_list.append(dic)

pprint(dic)


for day in weeks[1:]:
    week = day.find("span", class_="wr-date__longish").text
    date = day.find("sapn", class_="wr-date__longish__dotm")
    month = day.find("span", class_="wr-date__long__month").text
    weather_detail = day.find("div", class_="wr-day__weather-type-description wr-js-day-content-weather-type-description wr-day__content__weather-type-description--opaque").text
    weather_type=day.find("div", class_="wr-weather-type__text").text
    high, low = day.find_all("span", class_="wr-value--temperature--c")
    wind = day.find("span",class_="wr-value--windspeed wr-value--windspeed--mph").text


    dic= {"week":week, "date":date, "month":month, "weather_type":weather_type, "weather_detail":weather_detail, "tem":(high.text, low.text),"wind":wind}

    if "rain" in dic["weather_detail"]: 
        reputation = "傘持っていけ"
        print("傘持っていけ")
    else:
        reputation = "傘邪魔"
        print("傘邪魔")

    dic.update(reputation =reputation)

    d_list.append(dic)
        


pprint(d_list[4])

df = pd.DataFrame(d_list)

print(df.shape)

df.to_csv("weather_bbc.csv",index=None ,encoding="utf-8-sig")

new_path = "C:\\Users\\SYUNTA\\Documents\\python"
c_path = os.getcwd()
file_fomula.file_moving(c_path, new_path, "weather_bbc.csv")

try:

    position = pg.locateOnScreen("Folder.jpg")
    print(position)
    pg.click(position)
finally:
    print("finished")