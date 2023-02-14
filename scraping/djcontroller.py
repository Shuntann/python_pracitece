import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_path = r"C:\Users\SYUNTA\Desktop\chromedriver.exe"

options = Options()
options.add_argument("--icognite")

driver = webdriver.Chrome(executable_path = chrome_path, options = options)

url = "https://www.gumtree.com/"
driver.get(url)

sleep(5)
