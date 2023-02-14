from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import os
import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://www.google.co.jp/?gws_rd=ssl"

options = Options()
options.add_argument("--incognito")

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get(url)
driver.maximize_window()

driver.implicitly_wait(5)

searchword = str(input("enter : "))


driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(searchword)
driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").submit()

tags = driver.find_element_by_class_name("MUFPAc")

img_tag = tags.find_element_by_link_text("画像").click()

sleep(3)

newurl = driver.current_url

print(newurl)

height = 200

while height <=1400:
    driver.execute_script("window.scrollTo(0.,{});".format(height))
    height += 200
    print(height)
    sleep(0.25)

r = requests.get(newurl)
soup = BeautifulSoup(r.text,"html.parser")

contents = soup.find_all("div", class_="isv-r PNCib MSM1fd BUooTd")

for content, i in zip(contents, range(10)):
    img_url = content.find("img", )

#作業中