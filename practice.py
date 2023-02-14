from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import textwrap
import csv
from webdriver_manager.chrome import ChromeDriverManager
import re


# ダウンロードしたい画像のurlを取得
def get_url_search(search):

    text_bs4 = ""


    url = "https://www.google.de/imghp?hl=ja&authuser=0&ogbl"
    text =""#初期化
    options = Options()
    options.add_argument("--incognito")

    driver = webdriver.Chrome(ChromeDriverManager().install(), options = options)

    driver.get(url)#open window

    affir = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[2]/div"
    ).click()

    ##affir_two = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/button[2]").click()



    """    if driver.find_element_by_class_name("VDity").get_attribute("class") == "VDity":
        big_affir = driver.find_element_by_class_name("VDity")
        affir = big_affir.find_element_by_tag_name("button")[1].click()
    
    elif driver.find_element_by_class_name.get_attribute("class") == "GzLjMd":
        big_affir = driver.find_element_by_class_name("GzLjMd")
        affir = big_affir.find_element_by_tag_name("button")[1].click()"""

    

    sleep(1)



    #検索したい画像のキーワード検索
    ss = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
    ss.send_keys(search)
    ss.submit()

    driver.implicitly_wait(10)

    text_bs4 = driver.page_source#検索ページ情報取得

    driver.quit()

    return text_bs4


def get_all_url(search):#各ページのurlを取得しそれをリスト化し受け渡す関数
    all_url = [] #全てのページのurl情報を格納

    

    text = get_url_search(search)#上の関数で得たurlテキスト情報取得

    soup = BeautifulSoup(text, features="lxml") #htmlの解析

    main_content = soup.find("div", class_="islrc")#画像検索エリアのおおもとを取得
    contents = main_content.find_all("div", class_="isv-r PNCib MSM1fd BUooTd")[:10]

    for content , i in zip(contents, range(0,10)):#10個分を取得

        url = content.find("a", class_="VFACy kGQAp sMi44c d0NI4c lNHeqe WGvvNb").get("href")#各ページのurlを抽出

        all_url.append(url)#取得したurlをリストに入れる

    return all_url

def open_each_page(all_url):#各ページを実際に開いて全ての画像を取得する関数

    img_li = []

    options = Options()
    options.add_argument("--incognito")

    driver = webdriver.Chrome(ChromeDriverManager().install(), options = options)

    for url in all_url:

        dic={}#初期化

        one_li =[]#初期化
        img_li= []#初期化


        driver.get(url)#page open with selenium

        sleep(1)

        imgs = driver.find_elements_by_tag_name("img")#全てのimgタグのhtml情報取得

        driver.implicitly_wait(10)

        driver.quit()

        for one_img in imgs:
            img_one =one_img.get_attribute("src")#one_imgにimgのurlを格納
            one_li.append(img_one)#liに格納

        

        for img, i in zip(one_li,range(len(one_li))):#画像のurlを辞書に格納する
            number = "No. " + str(i)#i番目の画像

            dic[number] = img#i個目の画像のurl
        
        img_li.append(dic)#img_liに全ての画像のurlを格納

    return img_li


"""def open_each_page_with_bs4(all_url):
    while True:

        for url in all_url:
            r = requests.get(url)
            soup = BeautifulSoup(r.text,"html.parser")

            sleep(1)

            imgs = soup.find_all("img")

            for img_url in imgs:
                one_img = img_url.get("src")
                


"""
            


    

#メインのみで実行
if __name__ == "__main__":
    
    search = str(input("search : "))

    bs4 = get_url_search(search)

    urls = []#初期化

    import_li =[]#初期化

    urls = get_all_url(search)

    import_li =open_each_page(urls)

    print(import_li)

#作業中