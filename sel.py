from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re
import json
attr = ['calories', 'protein', 'fat', 'carb', 'sodium', 'sugar', 'image']
allItems = []

driver = webdriver.Chrome()
driver.get("https://foodsafety.family.com.tw/Web_FFD/Page/FFD_1_1.aspx#header") 
button = driver.find_element_by_name("ctl00$ContentPlaceHolder1$ctl00")
button.click()
try:
    element = WebDriverWait(driver, 5000).until(
        EC.presence_of_element_located((By.CLASS_NAME, "bann-strip"))
    )
except:
    driver.quit()
source = driver.page_source
soup = BeautifulSoup(source, 'html.parser')
for a in soup.find_all('a', href=True):
    if(re.match("^FFD.*", a['href']) ):
        print ("Found the URL:", "+", a['href'])
        driver.get("https://foodsafety.family.com.tw/Web_FFD/Page/" + a['href']) #https://foodsafety.family.com.tw/Web_FFD/Page/ + 
        try:
            element = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.ID, "demo"))
            )
        except:
            continue
        item = {}
        item_source = driver.page_source
        item_soup = BeautifulSoup(item_source, "html.parser")
        ingredient = item_soup.find_all('h5')
        if(len(ingredient[4].text) == 0): continue
        for h in item_soup.find('h4'):
            item['name'] = h[3:]
        i = 0
        for h in ingredient[4:7]:
            item[attr[i]] = float(re.findall("\d+\.?\d*", h.text)[0])
            i = i + 1
        for h in ingredient[9:12]:
            item[attr[i]] = float(re.findall("\d+\.?\d*", h.text)[0])
            i = i + 1
        item['image'] = re.findall("Img=\d+\.\d+.jpg",a['href'])[0][4:]
        allItems.append(item)
f = open("result.json", "w", encoding='utf-8')
f.write(json.dumps(allItems, ensure_ascii=False))
f.close()

