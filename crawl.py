import requests
import json 
from bs4 import BeautifulSoup
import re
response = requests.get(
    "https://foodsafety.family.com.tw/Web_FFD/Page/FFD_1_2.aspx?CatNa=2F8BF38E932812A29D50A09490280B038A150772E67BA540&CatNo=C018977062F3E7E4&CmnoCode=08C2324880F88EDA&Img=003004.0612026.jpg")
soup = BeautifulSoup(response.text, "html.parser")
item = {}
for h in soup.find('h4'):
    item['name'] = h[5:]
i = 0
allItems = {}

attr = ['calories', 'protein', 'fat', 'carb', 'sodium', 'sugar', 'image']
for h in soup.find_all('h5')[4:7]:
    item[attr[i]] = float(re.findall("\d+\.?\d*", h.text)[0])
    i = i + 1
for h in soup.find_all('h5')[9:12]:
    item[attr[i]] = float(re.findall("\d+\.?\d*", h.text)[0])
    i = i + 1

allItems[0] = item
y = json.dumps(allItems, ensure_ascii=False)
print(y)
