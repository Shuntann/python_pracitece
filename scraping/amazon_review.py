from importlib.resources import open_binary
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from pprint import pprint
from selenium.webdriver.chrome.options import Options
import os
import pandas as pd

url = "https://www.amazon.co.jp/?&tag=hydraamazonav-22&ref=pd_sl_7ibq2d37on_e&adgrpid=56100363354&hvpone=&hvptwo=&hvadid=592007363477&hvpos=&hvnetw=g&hvrand=6454312364382363435&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=1009345&hvlocphy=9045629&hvtargid=kwd-10573980&hydadcr=27922_14541005&gclid=Cj0KCQjwhLKUBhDiARIsAMaTLnFxLUwlITaB8ktBdewzl1bY5HTaMsBIKMR0cn_ul5BG8c4sqv09U3QaApDOEALw_wcB"

options = Options()
options.add_argument("--incognito")

driver = webdriver.Chrome(ChromeDriverManager().install())

def open_window(url):

    d_list=[]


    driver.get(url)
    driver.maximize_window()

    driver.implicitly_wait(10)

    searchword = str(input("enter what you want : "))

    search = driver.find_element_by_xpath("/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div[1]/input")
    search.send_keys(searchword)
    search.submit()

    sleep(2)

    c_url = driver.current_url
    print(c_url)
    
    sleep(3)

    content = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]")

    contents = content.find_elements_by_class_name("sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 AdHolder sg-col s-widget-spacing-small sg-col-4-of-20")

    for i, content in enumerate(contents, start = 1):
        name = f"{searchword}_{i}"
        raw_url = content.find_element_by_class_name("a-link-normal s-no-outline").get_attribute("href")
        img_url = content.find_element_by_tag_name("img").get_attribute("src")
        title = content.find_element_by_class_name("a-size-base-plus a-color-base a-text-normal").text
        star = content.find_element_by_tag_name("i").find_element_by_tag_name("span").text
        numbers_of_review = content.find_element_by_class_name("a-size-base s-underline-text").text
        price = content.find_element_by_class_name("a-price").find_element_by_class_name("a-offscreen").text
        coment_out = content.find_element_by_class("a-row a-size-base a-color-secondary").find_element_by_tag_name("span").get_attribute("aria-label")

        dic = {"name":name, "title":title,"img_url":img_url , "raw_url":raw_url, "price":price, "star":star, "review_numbers":numbers_of_review, "coment":coment_out}

        print(dic)

        d_list.append(dic)

        print(d_list)

        sleep(0.5)

    pprint(d_list)
    sleep(3)
    driver.quit()
    
    return d_list


li = open_window(url)


df = pd.DataFrame(li)
df.to_csv("amazon_review.csv", encoding="utf-8-sig")




    



