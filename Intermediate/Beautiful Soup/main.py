import ssl
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
url = 'https://www.timeout.com/film/best-movies-of-all-time'
# Create an unverified context
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urlopen(req) as response:
    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.find_all('a'):
        try:
            if int(anchor.get_text().split('.')[0]) > 0:
                print(anchor.get_text().split('.')[1])
        except ValueError:
            continue
