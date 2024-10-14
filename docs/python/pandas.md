# pandas

## Introduction

<figure markdown="span">
  ![Spotify Top 50 Austria](https://pandas.pydata.org/static/img/pandas_white.svg){ width="250" }
</figure>

As the last topic in our `Python` :fontawesome-brands-python: Crash Course,
we provide a brief introduction to `pandas` in order to handle data 
sets. The package will be heavily used in the upcoming chapters (e.g.,
[Statistics](../statistics/index.md)).
Therefore, knowledge of the package is needed to properly follow the 
chapters from now on.

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

Download the whole data set to follow this section:

[Spotify Top 50 Austria :fontawesome-solid-download:](../assets/python/pandas/spotify-top50.csv){ .md-button }

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

The data set dimensions are accessed with the `#!python shape` attribute.

```py 
print(data.shape)
```

```title=">>> Output"
(50, 25)
```

The data set has `#!python 50` rows and `#!python 25` columns.

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

A `DataFrame` is composed of at least one `Series`.

### Selecting data

Let's dive deeper into selecting data. To access specific rows, you can use 
a slice (just like with lists).

```py
# rows 5 and 6
print(data[5:7])
```

```title=">>> Output"
               spotify_id        name  ...    tempo  time_signature
5  0io16MKpbeDIdYzmGpQaES  Embrace It  ...  114.933               4
6  3aJT51ya8amzpT3TKDVipL         FTW  ...   91.937               4
```

Select multiple columns by passing a list of column names.

```py
print(data[["name", "artists"]])
```

```title=">>> Output"
                                  name    artists
0                The Emptiness Machine    Linkin Park
1                         Rote Flaggen    Berq
2                       Bauch Beine Po    Shirin David
...
```

#### Boolean indexing

Most of the time, we want to filter the data based on criterias. 
For example, we can select the tracks with a tempo higher than `#!python 120`
beats per minute (BPM).

```py
high_tempo = data[data["tempo"] > 120]
```

Let's break the example down:

- First, we select the column `tempo` from the data set with `#!python data["tempo"]`.
- Next, we expand our expression to `#!python data["tempo"] > 120`.
  This will return a `Series` of boolean values.
- Lastly, we wrap the expression in another set of square brackets to 
  filter the whole data set based on our boolean values.

We end up with 27 tracks that meet the criteria. `high_tempo` is a new 
`DataFrame` containing entries that exceed `#!python 120` BPM.


???+ question "Danceable tracks"

    <figure markdown="span">
      ![Saturday Night Fever](https://pics.filmaffinity.com/saturday_night_fever-812741122-large.jpg){ width="350" }
    <figcaption>Saturday Night Fever</figcaption>
    </figure>

    We assume that tracks with a danceability score higher than `#!python 0.8`
    are danceable. :fontawesome-solid-martini-glass-citrus:

    How many of the tracks are danceable?
    
    > Danceability describes how suitable a track is for dancing based on a 
    combination of musical elements including tempo, rhythm stability, beat 
    strength, and overall regularity. A value of 0.0 is least danceable and 
    1.0 is most danceable.
    >
    > -- <cite>[Spotify for Developers][1]</cite>
    
    [1]: https://developer.spotify.com/documentation/web-api/reference/get-audio-features

### Mathematical operations

`pandas` supports mathematical operations on both `Series` and `DataFrame`.
For instance, we weigh the popularity of a track by its energy level.

> Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of
> intensity and activity. 
>
> -- <cite>[Spotify for Developers][1]</cite>

[1]: https://developer.spotify.com/documentation/web-api/reference/get-audio-features

```py
weighted_popularity = data["popularity"].mul(data["energy"])
print(type(weighted_popularity))

# assign the Series to the DataFrame
data["weighted_popularity"] = weighted_popularity
```

The `mul()` method is used to multiply the `popularity` and `energy` columns.
The resulting `Series` is assigned to `data` as a new column.

```title=">>> Output"
<class 'pandas.core.series.Series'>
```

???+ question "Track length"
    
    <figure markdown="span">
      ![Spotify App](https://duet-cdn.vox-cdn.com/thumbor/0x0:2040x1360/640x427/filters:focal(1020x680:1021x681):format(webp)/cdn.vox-cdn.com/uploads/chorus_asset/file/11596505/akrales_180620_1777_0169.jpg){ width="350" }
    </figure>
    
    Since songs are [getting shorter](https://www.theverge.com/2019/5/28/18642978/music-streaming-spotify-song-length-distribution-production-switched-on-pop-vergecast-interview)
    and shorter, we want to know how long the tracks in our data set are. 
    To do so, calculate the length in **minutes**.
    
    - Explore the given data set to find the appropriate column (which 
      holds information on the song length). 
    - Calculate the length in minutes (hint: use the `pandas` 
      [documentation](https://pandas.pydata.org/docs/reference/api/pandas.Series.div.html) 
      or Google.)
    - Assign the result to the data frame.
    - Use boolean indexing, to check if there are any tracks longer than 
      `#!python 4` minutes.
    - Lastly, calculate the average track length in minutes.


### Basic statistics

`pandas` provides a variety of methods to calculate basic statistics. For 
instance, `min()`, `max()`, `mean()` can be easily retrieved for a numeric 
`Series` in the data set.

```py
print(data["tempo"].min())
```

```title=">>> Output"
80.969
```

Conveniently, statistics can be calculated for each column at once using 
the `DataFrame`. In this example, we calculate the standard deviation.

```py
print(data.std())
```

If you execute the above snippet, a `#!python TypeError` is raised.

???+ question "Fix the error"
    
    Try to determine, why the error was raised in the first place.
    Now, circumvent/fix the error.

    **Hint:** Look at the documentation of the `std()` method and its 
    parameters.

If you want to calculate multiple statistics, you can call the `describe()` 
method.

```py
stats = data.describe()
print(stats)
```

```title=">>> Output"
       daily_rank  daily_movement  ...       tempo  time_signature
count    50.00000        50.00000  ...   50.000000       50.000000
mean     25.50000         1.04000  ...  125.087260        3.920000
std      14.57738         8.14902  ...   26.751323        0.340468
min       1.00000       -22.00000  ...   80.969000        3.000000
25%      13.25000        -3.00000  ...  104.990750        4.000000
50%      25.50000         1.00000  ...  123.981500        4.000000
75%      37.75000         3.00000  ...  137.487250        4.000000
max      50.00000        29.00000  ...  184.115000        5.000000
```

`describe()` provides descriptive statistics for each column. The result of 
`describe()` is a `DataFrame` itself.

### Other functionalities

`pandas` offers a plethora of functionalities. There's simply too much to 
cover in a brief introductory section. Still, there are some common 
`DataFrame` methods/properties that are worth mentioning:

- [`sort_values()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html): Sort the data frame by a specific column.
- [`groupby()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html): Group the data frame by a column.
- [`merge()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html): Merge two data frames.
- [`T`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.T.html): Transpose of the data frame.
- [`drop_duplicates()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html): Remove duplicates.
- [`dropna()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html): Remove missing values.

All methods are linked to its corresponding documentation with examples 
that help you get started.

## Recap

We covered `pandas` and some selected functionalities which should provide 
you with a solid foundation to work with tabular data sets. Moreover, you 
should be able to follow the code portions in the upcoming chapters (e.g., 
[Statistics](../statistics/index.md)) course more easily.

???+ info "🎉"
    
    Congratulations, you've reached the end of the
    **Python :fontawesome-brands-python:** Crash Course!

    <blockquote class="reddit-embed-bq" style="height:500px" data-embed-height="659"><a href="https://www.reddit.com/r/ProgrammerHumor/comments/1g2tv7a/parsertongue/">parserTongue</a><br> by<a href="https://www.reddit.com/user/Ange1ofD4rkness/">u/Ange1ofD4rkness</a> in<a href="https://www.reddit.com/r/ProgrammerHumor/">ProgrammerHumor</a></blockquote><script async="" src="https://embed.reddit.com/widgets.js" charset="UTF-8"></script>

    With the knowledge gained, you're now well-equipped to write your own 
    scripts. Additionally, you're able to automate tasks, write functions to 
    tackle complex problems and work with data sets. You can leverage
    the functionalities of **Python :fontawesome-brands-python:** packages and
    using virtual environments, you can efficiently manage the packages required
    for your projects.

    Lastly, let's have a brief look at the upcoming chapter.

## What's next?

The upcoming statistics chapter introduces foundational tools to further 
analyse data. Among the topics are descriptive and inferential
statistics which are previewed in this section. After completion, you 
will be equipped with methods to explore, summarize and effectively visualize
your data sets. 

<figure markdown="span">
  ![Apple Keynote](https://www.techjunkie.com/wp-content/uploads/2013/09/20130911_cumulativeiphonesales4.jpg){ width="550" }
<figcaption>Maybe a not so effective chart, if the actual sales numbers are missing...
</figcaption>
</figure>

### Example: Descriptive statistics

One common tool within the descriptive realm is the box plot. For instance,
using our Spotify data set, we can visualize the loudness (in dB) based on 
whether a track contains explicit lyrics.

<div style="text-align: center;">
    <iframe src="/assets/python/pandas/boxplot-loudness.html" width="100%" height="550px">
    </iframe>
</div>

The above plot suggests that songs with explicit lyrics 
tend to be slightly louder than those without (looking at the median). 
Apart from the more in-depth explanation of box plot, concepts are 
introduced to further validate such claims.

---

### Example: Inferential statistics

To illustrate another example, the inferential statistics part contains a 
section on linear regression which equips you with the necessary knowledge to 
fit your first model. The following code snippet models the popularity of a
track with the given features (such as danceability, loudness, tempo, liveness, 
etc.).

```py
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("spotify-top50.csv")

X = data[
    [
        "danceability",
        "loudness",
        "speechiness",
        "acousticness",
        "instrumentalness",
        "liveness",
        "valence",
        "tempo",
    ]
]
y = data["popularity"]

# fit the model
reg = LinearRegression().fit(X, y)
```

With the model at hand, we can predict the popularity of a track and compare
it to the actual value.

<div style="text-align: center;">
    <iframe src="/assets/python/pandas/real-vs-predicted.html" width="100%" height="550px">
    </iframe>
</div>

You will learn how to interpret these results and measure the goodness of 
fit (i.e., if the popularity is accurately modelled) and apply it to your 
own data sets.

---

See you in the Statistics chapter! :waving_hand:
