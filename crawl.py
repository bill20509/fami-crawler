import requests
from bs4 import BeautifulSoup
response = requests.get(
    "https://foodsafety.family.com.tw/Web_FFD/Page/FFD_1_2.aspx?CatNa=2F8BF38E932812A29D50A09490280B038A150772E67BA540&CatNo=C018977062F3E7E4&CmnoCode=08C2324880F88EDA&Img=003004.0612026.jpg")
soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify())  #輸出排版後的HTML內容
