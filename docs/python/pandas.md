# pandas

## Introduction

As the last topic in our `Python` :fontawesome-brands-python: Crash Course,
we provide a brief introduction to `pandas` in order to handle data 
sets. The package will be heavily used in the upcoming 
[Statistics](../statistics/index.md) course.
Therefore, knowledge of the package is needed to properly follow the course.

???+ info

    At the time of writing, `pandas` version `2.2.3` was used. Keep in mind,
    that `pandas` is actively developed and some functionalities might 
    change in the future. However, as always, we try to keep the content 
    up-to-date.

    This section is heavily based on the excellent [10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/index.html#user-guide) 
    guide.

---

## The data set

<figure markdown="span">
  ![Spotify Top 50 Austria](https://image-cdn-fa.spotifycdn.com/image/ab67706c0000da8498a2aad5322ac3f3a1ab16e9){ width="350" }
</figure>

We will use a custom Spotify data set, containing the current[^1] top 50 
songs in Austria. You can find the corresponding playlist
[here](https://open.spotify.com/playlist/37i9dQZEVXbKNHh6NIXu36).


???+ info

    If you're interested in the creation of the data set, you can find the code 
    below. Note, `pandas` was the only package needed, and we will cover some of 
    the used functionalities in this section.

    ??? code "Create Spotify data set"
    
        ```py
        --8<-- "docs/assets/python/pandas/spotify.py"
        ```

{{ read_raw("assets/python/pandas/spotify-top50.md") }}

Download the whole data set 
[here](../assets/python/pandas/spotify-top50.csv){:spotify-top50.csv} to 
follow this section.

[^1]:
    The full data set is available on [Kaggle](https://www.kaggle.com/datasets/asaniczka/top-spotify-songs-in-73-countries-daily-updated/data)
    and contains the most streamed songs for multiple different countries.
    For our purpose, the data was subset.


## Prerequisites

For this section, we recommend, to make a new project folder with a 
Jupyter notebook. Additionally, create a new virtual environment and 
**activate** it. Please refer to the previous section on [packages and virtual 
environments](packages.md) if you're having trouble. Lastly, install `pandas`.

## Getting started

Let's explore some of `pandas` functionalities on the example of the Spotify
data set. First, we need to import the package.

```py
import pandas as pd
```

The `#!python as` statement is used to create an alias for the package in 
order to quickly reference it within our next code snippets. An alias 
simply reduces the amount of characters you have to type. Moreover, the 
alias `pd` is commonly used for `pandas`. Therefore, you can more 
easily 
employ code snippets you find online.

With the package imported, we can already read the data set (given as `.csv`).

```py
data = pd.read_csv("spotify-top50.csv")
```

The above code snippet assumes, that both data set and notebook are located at
the same directory level. Else, you have to adjust the path 
`#!python "spotify-top50.csv"` accordingly.