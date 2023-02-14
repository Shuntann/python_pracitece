import time
from selenium import webdriver

#Chromeドライバの設定
options = webdriver.ChromeOptions()
driver_path = 'C:/Users/chromedriver.exe'
driver = webdriver.Chrome(executable_path = driver_path, chrome_options = options)

#画面遷移
driver.get('https://www.amazon.co.jp/')

# ログイン画面へ遷移
mailad = driver.find_element_by_id("nav-link-accountList")
mailad.click()

# ログインIDを入力
login_id = driver.find_element_by_id("ap_email")
login_id.send_keys('example@example.com')

# 「次に進む」をクリック
nextb = driver.find_element_by_class_name("a-button-input")
nextb.click()
time.sleep(1)

# パスワードを入力
password = driver.find_element_by_name("password")
password.send_keys('example')

# 「ログイン」をクリック
nextb = driver.find_element_by_id("signInSubmit")
nextb.click()
time.sleep(1)

#作業途中