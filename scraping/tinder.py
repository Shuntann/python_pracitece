from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import tinder_sms
import sys,os
import signal
import chromedriver_binary
import pandas as pd
sys.path.append("../")
from file_fomula import file_moving
#import scraping.photo_download_web.py



chrome_path = r"C:\Users\SYUNTA\Desktop\chromedriver.exe"
my_number = ""

options=Options()
options.add_argument("--incognito")


driver = webdriver.Chrome(executable_path=chrome_path, options = options)

url = "https://tinder.com/"

try:
    driver.get(url)

    driver.maximize_window()
 
    driver.implicitly_wait(10)


    login = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a").click()

    #driver.implicitly_wait(10)
    sleep(1)

    phone_log_push = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[3]/button").click()

    """WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[1]/div[2]/div/div[1]"))"""

    driver.implicitly_wait(60)

    phone_number_send = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div[2]/div/input")
    phone_number_send.send_keys(my_number)
    phone_number_push = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/button").click()

    affir_phonenumber_input = tinder_sms.sms()

    affir_number = driver.find_elements_by_xpath("/html/body/div[2]/div/div/div[1]/div[3]/input")
    for affir, i in zip(affir_number, range(6)):
        affir.send_keys(affir_phonenumber_input[i])

    affir_push = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/button").click()


    affir_mail_input = str(input("enter your mail code:"))

    affir_mail_number = driver.find_elements_by_xpath("/html/body/div[2]/div/div/div[1]/div[3]/input")
    for affir, i in zip(affir_mail_number, range(6)):
        affir.send_keys(affir_mail_input[i])

    affir_push2 = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/button").click()
    sleep(5)
    wipe_url = driver.current_url

    print(wipe_url)
    sleep(4)

    print("login finished")
#ログイン終了

#swipe開始

    location = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[3]/button[1]").click()

    #driver.implicitly_wait(10)
    sleep(5)
    info = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[3]/button[2]").click()

    li_girls = []

    driver.implicitly_wait(10)
    like = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[1]/div[3]/div[3]/div/div[1]/div/span[2]")
    nope = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[1]/div[3]/div[3]/div/div[1]/div/span[2]")

    print(like.text)

    for i in range(3):
        #if like.text <= 22 and int(like.text) >= 20:

        name = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[1]/div[3]/div[3]/div/div[1]/div/div[1]/span").text
        age = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[1]/div[3]/div[3]/div/div[1]/div/span[2]").text
        intro = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[1]/div[2]/div[3]/div/div[2]/div/div").text
        image = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/span[1]/div").get_attribute("style")
            #https://images-ssl.gotinder.com/u/86Pay83hGrr9b8wwTVYeA7/hxcpQDvtASUgBCPig65WCB.webp?Policy=eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6IiovdS84NlBheTgzaEdycjliOHd3VFZZZUE3LyoiLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE2MjQ2NjAxNTd9fX1dfQ__&Signature=b7ZUHoskfb9bIiFq0EKYLxzJdfAg~qZ6n3yXSq-g40KKwvBWALdbv-QvhMxDUIYx6w9qBIm3jYRuUIX4y5rzY6XnKcaVo1PIkGL5FlsgvmYEXe~jhxp9G72UMxN9fUs1kCJ5ZmNYcrRSQhNANjvLSMXvaFzygH5hUJMKoXf8GH3u00Svjo-RZ743BTzuVIju1PCOY1wqpn6Lsisr7UgdxtaLgU4EaZyj9as87qEmxmhMDFbZKWI3XGqgiB9FkS3pPuHUGEuOyN6eZB0xZJ16vJ0k0b6ozg5rWQiHhoSgKBX9PutGqxu9neKrbrkWO5wYRk~CSS9cOlpnxT2xbQHxmQ__&Key-Pair-Id=K368TLDEUPA6OI

        swipe = like.click()

        dic_girls = {"name":name, "age":age, "introduction":intro, "image_url":image}

        li_girls.append(dic_girls)

        driver.implicitly_wait(10)

        #else:
        #    swipe = nope.click()

    df = pd.DataFrame(li_girls)
    df.to_csv("tinder.csv", encoding="utf-8-sig")






finally:
    os.kill(driver.service.process.pid, signal.SIGTERM)
    




