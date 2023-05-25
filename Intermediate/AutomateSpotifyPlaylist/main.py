import ssl
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import Billboard
import Spotify

billboard = Billboard.Billboard(input("Enter the year: "))
print(billboard.get_songs())
spotify = Spotify.Spotify()
print(spotify.get_access_token())
print(spotify.searchsong())