from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("https://foodsafety.family.com.tw/Web_FFD/Page/FFD_1_1.aspx#header") 
button = driver.find_element_by_name("ctl00$ContentPlaceHolder1$ctl00")
button.click()
# try:
#     element = WebDriverWait(driver, 100).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, ".popup-with-zoom-anim"))
#     )
# finally:
#     driver.quit()
