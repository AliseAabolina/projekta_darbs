import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from openpyxl import Workbook, load_workbook
service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url2 = "https://www.zalando.lv/"
time.sleep(6)
driver.get(url2)
time.sleep(3)
print("Ievadietlietu:")
input3= input()


time.sleep(5)

find_search_input = driver.find_element(By.ID,"header-search-input")
find_search_input.send_keys(input3)
time.sleep(4)
find_search_input.send_keys(Keys.ENTER)




#title CLASS_NAME -productdescriptionname