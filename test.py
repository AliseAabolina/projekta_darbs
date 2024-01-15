import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from openpyxl import Workbook, load_workbook
import pandas as pd
service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)
print("Ievadiet lietu:")
input1 = input()
print("ievadiet budžetu:")
input2 = input()


url = "https://www.aboutyou.lv/jusu-veikals"
time.sleep(6)
driver.get(url)
time.sleep(5)
find_ok = driver.find_element(By.ID,"onetrust-accept-btn-handler")
find_ok.click()
time.sleep(2)

find_search = driver.find_element(By.XPATH,'//*[@id="react-root"]/header/div[4]/section/div[2]/div/input')
find_search.send_keys(input1)
time.sleep(4)
find_search.send_keys(Keys.ENTER)

time.sleep(6)

find_price = driver.find_element(By.XPATH, '//button/span[text()="Cena"]')
find_price.click()
time.sleep(4)
find_set_price = driver.find_element(By.XPATH,'//input[@data-testid="maximumInput"]')
find_set_price.send_keys(input2)
find_set_price.send_keys(Keys.ENTER)


time.sleep(3)
title_elements = driver.find_elements(By.CSS_SELECTOR, "[class*='sc-1vt6vwe-0 sc-1vt6vwe-1']")
titles = [title.text for title in title_elements]

time.sleep(2)
product_price_elements = driver.find_elements(By.XPATH, '//span[@data-testid="finalPrice"]')
prices = [price.text for price in product_price_elements]



if len(titles) == len(prices):
    combined_list = [f"{title} - {price}" for title, price in zip(titles, prices)]
    print("\nAbout you:")
    for item in combined_list:
        print(item)
else:
    print("\n error")
print(len(titles))
print(len(prices))

about_you_dati = pd.DataFrame({
    'Website': 'About You',
    'Title': titles,
    'Price': prices
})

############## ZALANDO-----------------------------------------------------------------
driver.get("https://www.zalando.lv/")
time.sleep(4)

find_search_input = driver.find_element(By.ID,"header-search-input")
find_search_input.send_keys(input1)
time.sleep(4)
find_search_input.send_keys(Keys.ENTER)

find_cena = driver.find_element(By.CSS_SELECTOR, '[aria-label="filtrēt pēc Cena"]')
find_cena.click()
time.sleep(3)


find_set_cena = driver.find_element(By.CSS_SELECTOR, '[aria-label="Augstākā cena"]')
actions = ActionChains(driver)
actions.double_click(find_set_cena).perform()


find_set_cena.send_keys(Keys.BACKSPACE)
find_set_cena.send_keys(input2)
find_set_cena.send_keys(Keys.ENTER)
time.sleep(2)

saglabat = driver.find_element(By.CSS_SELECTOR, '[aria-label="lietot filtru Cena"]')
saglabat.click()
time.sleep(4)

# ... previous code ...

title_elements2 = driver.find_elements(By.CSS_SELECTOR, "[class='sDq_FX lystZ1 FxZV-M HlZ_Tf ZkIJC- r9BRio qXofat EKabf7 nBq1-s _2MyPg2']")
nosaukumi = [title.text for title in title_elements2]

time.sleep(2)

product_price_elements2 = driver.find_elements(By.CSS_SELECTOR, "[class*='sDq_FX lystZ1 dgII7d Km7l2y']")
cenas = [price.text for price in product_price_elements2 if "No" not in price.text]

time.sleep(3)


if len(nosaukumi) == len(cenas):
    combined_list2 = [f"{title} - {price}" for title, price in zip(nosaukumi, cenas)]
    print("\nZALANDO:")
    for item in combined_list2:
        print(item)
else:
    print("\n error")
print(len(nosaukumi))
print(len(cenas))

zalando_dati = pd.DataFrame({
    'Website': 'ZALANDO',
    'Title': nosaukumi,
    'Price': cenas
})

visi_dati = pd.concat([about_you_dati, zalando_dati], ignore_index=True)

# Create an Excel workbook and sheet
excel_file_path = 'products1.xlsx'
visi_dati.to_excel(excel_file_path, index=False)

print(f"Data saved to {excel_file_path}")

driver.quit()