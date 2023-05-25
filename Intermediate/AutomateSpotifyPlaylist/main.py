from urllib.request import urlopen, Request
import Billboard
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Which year do you want to travel to? ")
billboard = Billboard.Billboard(date)
song_names = billboard.get_songs()
print(song_names)

#Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="c198e162ca1840c28762ef0ca456d9e4",
        client_secret=open("Python100day/Intermediate/AutomateSpotifyPlaylist/spotify.bd", "r").read(),
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]
print(user_id)

#Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)