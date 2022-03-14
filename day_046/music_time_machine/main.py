"""Music Time machine with scrapping"""
import sys

import requests
from bs4 import BeautifulSoup

sys.path.insert(0, "../..")


from personal_config import my_info

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

spotify_id = my_info["spoty_client_id"]
spotify_secret = my_info["spoty_client_secret"]
spotify_redirect_uri = "http://example.com"

BILLBOARD_BASE_URL = "https://www.billboard.com/charts/hot-100/"


def get_song_lists(some_date):
    """get the top 100 song list from billboard of a specific date"""
    URL = f"{BILLBOARD_BASE_URL}/{some_date}/"
    response = requests.get(URL)
    billboard_content = response.text
    # with open("The Hot 100 – Billboard.html", "r", encoding="utf-8") as f_in:
    #     billboard_content = f_in.read()
    soup = BeautifulSoup(billboard_content, "html.parser")
    top_100_tags = soup.select(selector="li ul li h3")
    top_100_songs = [song.getText().strip() for song in top_100_tags]

    return top_100_songs


def spotify_action(list_of_songs, some_date):
    """provide a list of songs and the date, create a spotify playlist"""
    # spotipy setup
    auth_manager = SpotifyOAuth(
        client_id=spotify_id,
        client_secret=spotify_secret,
        redirect_uri=spotify_redirect_uri,
        scope="playlist-modify-private",
    )
    sp = spotipy.Spotify(auth_manager=auth_manager)

    # extract the year for searching conveninece
    year = some_date.split("-")[0]

    # song_uri to store all the spotify uris from the search
    song_uris = []
    for song in list_of_songs:
        try:
            result = sp.search(q=f"track:{song} year:{year}", type="track")
            song_uris.append(result["tracks"]["items"][0]["uri"])
        except Exception as e:
            print(f"{song} not found from spotify")

    # user_id for creating playlist
    user_id = sp.current_user()["id"]
    playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard Top 100", public=False)
    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)


if __name__ == "__main__":
    date_correct = False
    while not date_correct:
        date = input("Which year do you want to travel to? Tye the date in this format YYYY-MM-DD: ")
        if len(date) != 10 or date[4] != "-" or date[7] != "-":
            print("You have entered an invalid date format.")
        else:
            date_correct = True
    songs = get_song_lists(date)
    print(spotify_action(songs, date))
