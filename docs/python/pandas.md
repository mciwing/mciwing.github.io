# pandas

???+ info

    At the time of writing, `pandas` version `2.2.3` was used. Keep in mind,
    that `pandas` is actively developed and some functionalities might 
    change in the future. However, as always, we try to keep the content 
    up-to-date.

    This section is heavily based on the excellent [10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/index.html#user-guide) 
    guide.


<figure markdown="span">
  ![Spotify Top 50 Austria](https://image-cdn-fa.spotifycdn.com/image/ab67706c0000da8498a2aad5322ac3f3a1ab16e9){ width="350" }
</figure>

We will use a custom Spotify data set, containing the current[^1] top 50 
songs in Austria. You can find the corresponding playlist
[here](https://open.spotify.com/playlist/7r36EDSbzLnsGHtjV2qkcf).


???+ info

    If you're interested in the creation of the data set, you can find the code 
    below. Note, `pandas` was the only package needed, and we will cover some of 
    the used functionalities in this section.

    ??? code "Create Spotify data set"
    
        ```py
        --8<-- "docs/assets/python/pandas/spotify.py"
        ```


## The data set

{{ read_raw("assets/python/pandas/spotify-top50.md") }}

Download the whole data set 
[here](/assets/python/pandas/spotify-top50.csv){:spotify-top50.csv}.

[^1]:
    The full data set is available on [Kaggle](https://www.kaggle.com/datasets/asaniczka/top-spotify-songs-in-73-countries-daily-updated/data)
    and contains the most streamed songs for multiple different countries.
    For our purpose, the data was subset.

