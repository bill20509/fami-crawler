from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
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
f = open("source.txt", "w", encoding='utf-8')
f.write(source)
f.close()
for a in soup.find_all('a', href=True):
    print ("Found the URL:", "+", a['href'])
    driver.get("https://foodsafety.family.com.tw/Web_FFD/Page/" + a['href']) #https://foodsafety.family.com.tw/Web_FFD/Page/ + 
    item_source = driver.page_source
    item_soup = BeautifulSoup(item_source, "html.parser")
    for h in item_soup.find_all('h5'):
        print (h.text)

