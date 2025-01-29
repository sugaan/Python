import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Spotify API credentials
load_dotenv()
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# Extract data from Spotify API for artist Anirudh
results = sp.search(q="artist:Anirudh", type="album", limit=50)

data = []
for album in results["albums"]["items"]:
    album_details = {
        "album_name": album["name"],
        "album_id": album["id"],
        "release_date": album["release_date"],
        "total_tracks": album["total_tracks"],
        "spotify_url": album["external_urls"]["spotify"],
        "artist_name": album["artists"][0]["name"],
        "album_cover": album["images"][0]["url"],
    }
    data.append(album_details)

df = pd.DataFrame(data)

# Transform data
# Extract year from release_date
df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")
df["year"] = df["release_date"].dt.year

# Load data to postgres
engine = create_engine("postgresql://postgres@localhost:5432/postgres")
df.to_sql("anirudh_albums", engine, if_exists="replace", index=False)

print("Data loaded to postgres")

#visualize data
