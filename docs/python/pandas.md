# pandas

## Introduction

<figure markdown="span">
  ![Spotify Top 50 Austria](https://pandas.pydata.org/static/img/pandas_white.svg){ width="250" }
</figure>

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

You should end up with a project structure similar to the following:

```
📁 pandas-course/
├── 📁 .venv/
├── 📄 spotify-top50.csv
└── 📄 pandas-course.ipynb
```

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


### Reading files

With the package imported, we can already read the data set (given as `.csv`).

```py
data = pd.read_csv("spotify-top50.csv")
```

The above code snippet assumes, that both data set and notebook are located at
the same directory level. Else, you have to adjust the path 
`#!python "spotify-top50.csv"` accordingly.

Besides `.csv` files, `pandas` supports reading from various other file types
like Excel, text files or a SQL database. The [`pandas` documentation](https://pandas.pydata.org/docs/user_guide/io.html#io-tools-text-csv-hdf5) 
provides a comprehensive overview of different file types and their corresponding
function. Have a look, to get an idea which file formats are supported not 
only for reading but also for writing. 

### Displaying data

With a data set at hand, we will most likely want to view it. To view the 
first rows of our data frame use the `#!python head()` method.

```py
print(data.head())
```

```title=">>> Output"
               spotify_id                   name  ...    tempo  time_signature
0  2PnlsTsOTLE5jnBnNe2K0A  The Emptiness Machine  ...  184.115               4
1  7bkUa9kDFGxgCC7d36dzFI           Rote Flaggen  ...  109.940               3
2  64f3yNXsi2Vk76odcHCOnw         Bauch Beine Po  ...  123.969               4
3  2plbrEY59IikOBgBGLjaoe       Die With A Smile  ...  157.969               3
4  6dOtVTDdiauQNBQEDOtlAB     BIRDS OF A FEATHER  ...  104.978               4
```

To display the last rows of the data frame, use the `#!python tail()` method.

```py
print(data.tail())
```

```title=">>> Output"
                spotify_id  ... time_signature
45  6leQi7NakJQS1vHRtZsroe  ...              4
46  5E4jBLx4P0UBji68bBThSw  ...              4
47  6qzetQfgRVyAGEg8QhqzYD  ...              4
48  3WOhcATHxK2SLNeP5W3v1v  ...              4
49  7xLbQTeLpeqlxxTPLSiM20  ...              4
```

Columns can be viewed with:

```py
print(data.columns)
```

```title=">>> Output"
Index(['spotify_id', 'name', 'artists', 'daily_rank', 'daily_movement',
       'weekly_movement', 'country', 'snapshot_date', 'popularity',
       'is_explicit', 'duration_ms', 'album_name', 'album_release_date',
       'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness',
       'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo',
       'time_signature'],
      dtype='object')
```

Similarly, we can print the row indices.

```py
print(data.index)
```

```title=">>> Output"
RangeIndex(start=0, stop=50, step=1)
```
This data set is consecutively indexed from `#!python 0` to `#!python 49`. If 
you recall, a range does not include its `stop` value (`#!python 50`).

By default, (if not otherwise specified) `pandas` will assign a range index
to a data set in order to label the rows.

### Data structures

`pandas` has two main data structures: `Series` and `DataFrame`.
As you would expect, a `DataFrame` is a two-dimensional data structure such as 
our whole Spotify data set assigned to the variable `data`:

```py
print(type(data))
```

```title=">>> Output"
<class 'pandas.core.frame.DataFrame'>
```

Whereas, a single column of a `DataFrame` is referred to as a `Series`. 
Generally, selections of the `DataFrame` can be accessed with square 
brackets (`#!python []`). To get a column, you can simply use its
name.

```py
print(data["artists"])

print(type(data["artists"]))
```

```title=">>> Output"
0                                       Linkin Park
1                                              Berq
2                                      Shirin David
3                             Lady Gaga, Bruno Mars
...                                             ...

<class 'pandas.core.series.Series'>
```