# Create a Spotify data set, containing the top 50 tracks in Austria

# Original data (Top Spotify Songs in 73 Countries (Daily Updated)) from:
# https://www.kaggle.com/datasets/asaniczka/top-spotify-songs-in-73-countries-daily-updated/data
from pathlib import Path

import pandas as pd

# read initial data set
data = pd.read_csv(Path("data/universal_top_spotify_songs.csv"))

# only Austrian chart topping songs
data = data[data["country"] == "AT"]

# subset by latest snapshot date
latest_snapshot = data["snapshot_date"].max()
data = data[data["snapshot_date"] == latest_snapshot]
# sort by daily_rank
data = data.sort_values(by="daily_rank").reset_index(drop=True)

# write data to csv
data.to_csv(Path("data/spotify-top50.csv"), index=False)

# excerpt of the data set for inclusion in markdown
with Path("data/spotify-top50.md").open("w", encoding="UTF-8") as f:
    prefix = (
        f"Excerpt of the data set (snapshot date: **{latest_snapshot}**):\n\n"
    )
    _data = data[
        [
            "daily_rank",
            "name",
            "artists",
            "popularity",
            "is_explicit",
            "energy",
        ]
    ]
    # only top 5 songs
    _data = _data.head(5)
    markdown = _data.to_markdown(index=False)
    f.write(prefix + markdown)
