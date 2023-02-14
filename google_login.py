from time import sleep 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyautogui as pgui

chrome_path = r"C:\Users\SYUNTA\Desktop\chromedriver.exe"
mail = ""
g_ps = ""

options = Options()
options.add_argument("--incognito")
options.add_argument("--user-data-dir=C:\Users\SYUNTA\AppData\Local\Google\Chrome\User Data\Default")

driver = webdriver.Chrome(executable_path = chrome_path, options = options)


url = "https://www.google.com/"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(10)

affirmation = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/button[2]").click()
sleep(2)

login_push = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div/div[2]/a").click()

gmail_send = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
gmail_send.send_keys(mail)

push1 = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button").click()

#作業途中