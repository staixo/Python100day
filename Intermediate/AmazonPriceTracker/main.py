from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import ssl

# Get the HTML
URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
context = ssl._create_unverified_context()
req = Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req, context=context).read()
soup = BeautifulSoup(html, "html.parser")
cost = 0
for price in soup.find_all(class_="a-price-whole", limit=1):
    cost=price.text.strip()
for price in soup.find_all(class_="a-price-fraction", limit=1):
    cost=float(cost + price.text.strip())
print(cost)
if cost < 100:
    print("Buy!")
