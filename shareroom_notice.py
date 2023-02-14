import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

chrome_path = r"C:\Users\SYUNTA\Desktop\python_lesson\chromedriver.exe"
name=""
password=""



options = Options()
options.add_argument("--icognito")

driver = webdriver.Chrome(executable_path=chrome_path, options=options)

url = "https://m.spareroom.co.uk/"

driver.get(url)
sleep(2)

login = driver.find_element_by_link_text("Log In").click()

sleep(1)

id = driver.find_element_by_name("email")
ps = driver.find_element_by_name("password")

id.send_keys(name)
ps.send_keys(password)

#checkbox =driver.find_element_by_id("Remember me").click()

signin = driver.find_element_by_class_name("sign-in__button").submit()

sleep(2)

new_content = driver.find_element_by_class_name("counterNew").text
print(new_content)

if int(new_content) >= 1:
    print("新しいメッセージが来ています")
else:
    print("新しいメッセージはありません")


driver.close()
driver.quit()