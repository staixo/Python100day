import ssl
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request


URL = "https://www.billboard.com/charts/year-end/"

class Billboard:
    def __init__(self, year):
        self.html = None
        self.soup = None
        self.songs = []
        self.year = year
        self.url = URL + self.year + "/hot-100-songs/"
        print(self.url)

    def get_html(self):
        context = ssl._create_unverified_context()
        req = Request(self.url, headers={'User-Agent': 'Mozilla/5.0'})
        self.html = urlopen(req, context=context).read()
        return self.html

    def get_soup(self):
        self.soup = BeautifulSoup(self.html, "html.parser")
        return self.soup

    def get_songs(self):
        self.get_html()
        self.get_soup()
        for song in self.soup.find_all('h3', id='title-of-a-story',limit=100):
            self.songs.append(song.text.strip())
        return self.songs