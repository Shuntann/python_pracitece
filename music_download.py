from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
import shutil
import file_fomula
import sys



options = Options()
options.add_argument("--incognito")

driver = webdriver.Chrome(ChromeDriverManager().install())


def download():

    driver.get(url)
    ##driver.maximize_window()
    driver.implicitly_wait(5)

    youtube_url = sys.argv[1]
    print("Url is : {}" .format(youtube_url))

    driver.find_element_by_xpath("/html/body/div/div[1]/form/input").send_keys(youtube_url)
    driver.find_element_by_xpath("/html/body/div/div[1]/form/input").submit()

    driver.implicitly_wait(20)

    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/button").click()
    driver.implicitly_wait(7)
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/a[1]").click()

    sleep(20)
##    driver.quit()

download()

for music_name in os.listdir(d_path):
    if music_name[-3:] == "mp3":
        file_fomula.file_moving(d_path,new_path,music_name)

        i = os.path.join(new_path, music_name)

        print(i.replace("yt5s.com - ", ""))

        i.replace("yt5s.com - ", "")

        os.rename(i, i.replace("yt5s.com - ", "")[:-3]+"m4a")
        

driver.quit()
