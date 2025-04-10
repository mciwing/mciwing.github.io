# API

Another source of data is an application programming interface (API). An API 
consists of a set of rules and protocols that allows one software application 
to interact with another.
In other words, it is a way to communicate with a server. Some of these
servers are openly available and host data that can be accessed by anyone.
Others require authentication and are therefore paid services.

To illustrate the practical interaction with APIs, we will retrieve
data from multiple different APIs.
<!-- TODO describe which APIs -->

## First example

???+ question "Open a website :wink:"
    
    Open the {JSON} Placeholder website 
    [here](https://jsonplaceholder.typicode.com/).

As the site says {JSON} Placeholder is a public API which serves some fake 
data. It is the perfect starting place, to try and retrieve some data.
Without any prior knowledge you can start to send your first request using your
browser.

???+ question "Send your first request"

    Open following link within your browser to send your first request:
    https://jsonplaceholder.typicode.com/comments

    Observe the response. The structure of the resulting data should already
    look familiar.

<?quiz?>
question: Which Python type does the output of your request most closely resemble?
answer: A pandas DataFrame
answer: A simple list
answer-correct: A simple dictionary
content:
<p>Correct! The server response you got was actually in the form of a 
<code>JSON</code> file. 
This is a common format for APIs to return data. Later, we can easily read the 
<code>JSON</code> with <code>Python</code> and convert it to a dictionary.
</p>
<?/quiz?>

In this case, you have sent a request to the `/comments` **endpoint** to 
retrieve some fake data containing comments. 

## Endpoints

An endpoint is a specific URL that the API uses to perform a specific action.
To send a request to the server, we need to specify the endpoint in the URL.
The server will then respond with the requested data (if everything went 
smoothly).

In our example, `https://jsonplaceholder.typicode.com/` is simply the URL of 
the API and `/comments` is the endpoint of our interest. 

???+ question "Explore different endpoints"

    Again, visit {JSON} Placeholder website and scroll down to the Resources
    section. This specific API has 6 different endpoints. Try other endpoints
    of your choice and observe the response. Specifically look at the URL!

## APIs & Python

Since we don't want to manually use the browser anytime we want to retrieve 
data, we now replicate a request in `Python` :fontawesome-brands-python:. 
To send requests we can make use of the appropriately named
[`requests`](https://requests.readthedocs.io/en/latest/) package.

???+ question "Setup"
    
    Within a ==virtual environment== install the `requests` package.
    
    === ":fontawesome-brands-windows: Windows"

        ```bash
        pip install requests
        ```

    === ":fontawesome-brands-apple: MacOS"

        ```bash
        pip3 install requests
        ```

## Rate limits

During the task, you should have noticed that the API provides information 
on rate limits. Rate limits are the number of requests that can be made to
the server in a given time frame. If you as the user exceed the rate limit, 
the server will respond with an error message.
In this specific case, we can make up to 200 requests per minute which is more
than enough for our use case. These rate limits are set by the provider and 
can vary from one API to another. Some APIs may not have any rate limits at 
all.

The below snippet sends a request to the `/assets` endpoint and stores the
response in a variable.

```python
import requests

response = requests.get(url="https://api.coincap.io/v2/assets")
data = response.json()  # assign the response to a variable
```

???+ question "Validate the above quiz question"
    
    What type is returned by the `#!python response.json()` method? 
    Check the `#!python type()` of the `data` variable.

### Methods

In the above code snippet, we applied `requests` `get()` method.
The `get` method solely retrieves data from the server, that is no data is 
changed on the server-side. If you have another look at the CoinCap API docs
you will discover that all endpoints like `/assets`, `/rates`, or `/markets` 
are prefaced by the `GET` method.

Nevertheless, `GET` is not the only method, there are also `POST`, `PUT`,
`DELETE`, and `PATCH`. Following table provides a brief overview:

| Method | Description                         | `requests` method   |
|--------|-------------------------------------|---------------------|
| GET    | Retrieve data from the server       | `requests.get()`    |
| POST   | Create data on the server           | `requests.post()`   |
| PUT    | Update data on the server           | `requests.put()`    |
| DELETE | Delete data on the server           | `requests.delete()` |
| PATCH  | Partially update data on the server | `requests.patch()`  |

Don't worry about these methods too much for now as we will continue solely
with `GET` methods.

<div style="text-align: center;">
    <iframe src="https://giphy.com/embed/XreQmk7ETCak0" width="350" height="280" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/retro-thumbs-up-XreQmk7ETCak0"></a></p>
</div>

???+ info
    
    If you need to revisit the topic of HTTP methods or simply want to dive 
    deeper, [here's](https://restfulapi.net/http-methods/) a great article.

## Endpoints continued...

Let's revisit the code snippet from above and extend it. After requesting the 
`/assets` endpoint we convert the response (the `#!python dict`) into a tabular 
format in order to process the data more easily.

```python hl_lines="6 7"
import requests

response = requests.get(url="https://api.coincap.io/v2/assets")
data = response.json()

print(data.keys())  # print all dictionary keys
print(data["data"]) # closer look at the value of the "data" key
```

```title=">>> Output"
dict_keys(['data', 'timestamp'])
[{'id': 'bitcoin', 'rank': '1', 'symbol': 'BTC', 'name': 'Bitcoin', ....] 
```

A closer look at the response reveals that the `#!python dict` is nested. 
The `data` key is of particular interest, since it contains a list of 
dictionaries containing information on cryptocurrencies. 
We can convert this list to a `pandas` `DataFrame`.

```python
import pandas as pd

data = pd.DataFrame(data["data"])
print(data.head())
```

| id       | rank | symbol | name     | ... |
|----------|------|--------|----------|-----|
| bitcoin  | 1    | BTC    | Bitcoin  | ... |
| ethereum | 2    | ETH    | Ethereum | ... |
| tether   | 3    | USDT   | Tether   | ... |
| solana   | 4    | SOL    | Solana   | ... |
| xrp      | 5    | XRP    | XRP      | ... |

???+ info 

    The content of your `DataFrame` can differ slightly as responses 
    contain the latest data from the server. Since we are dealing with 
    cryptocurrency market data, changes occur rapidly.

    Nevertheless, that's the power of APIs as they allow you to 
    programmatically access up to date information. 🦾

## Query parameters

To continue on our quest to visualize the latest price history of a
cryptocurrency, we need to settle on a single cryptocurrency. The concept 
of query parameters is introduced with another practical example.

For the following examples, we will use an emerging (at the time of writing) 
cryptocurrency called `Pepe-Cash` (more of a meme-coin).

<p align="center">
  <img src="https://tokenscan.io/img/cards/PEPECASH.jpg" alt="Pepe">
</p>

To get access to the price history of `Pepe-Cash`, we need to consult the API 
documentation and find the appropriate endpoint.

<?quiz?>
question: Which endpoint provides the historic market data of a specific cryptocurrency?
answer: /markets
answer-correct: /assets/{{id}}/history
answer: /rates
answer: /assets - The endpoint we used before already contains the information we need.
content:
<p>Exactly, by providing a asset <code>id</code>, we can retrieve 
the price history from the <code>/assets/{{id}}/history</code> endpoint.
</p>
<?/quiz?>

With the endpoint name at hand, we can send another request to the server. 
But first, we need to construct the URL. Expand the code snippet below, if you 
solved the quiz question.

??? info "URL construction"

    ```python
    api_url = "https://api.coincap.io/v2"
    coin_id = "pepe-cash"
    endpoint = f"/assets/{coin_id}/history"
    query_params = "?interval=d1"  # daily interval (if available)
    
    url = f"{api_url}{endpoint}{query_params}"
    ```
    
    Let's walk through the URL construction step by step:
    
    1. `api_url` is the base URL of the API (nothing new here).
    2. `coin_id` :fontawesome-solid-arrow-right: `pepe-cash` is the 
        identifier of the cryptocurrency we want to retrieve data 
        for. We have already requested all cryptocurrency identifiers like 
        `bitcoin` or `ethereum` with the `/assets` endpoint. Have another look 
        at the table [here](#endpoints-continued).
    3. `endpoint` contains the endpoint name we want to access, in this 
        particular case :fontawesome-solid-arrow-right: 
        `/assets/pepe-cash/history`.
    4. `query_params` stands for ==query parameters== which are additional 
        parameters that are passed to the server. Think of a `Python` 
        function with the endpoint being the function name and the query 
        parameters being the function parameters used for fine-grained control.

        Query parameters are separated from the URL by a `?`.
        In this case, we specified `?interval=d1`. `interval` is the 
        parameter name followed by the value `d1` which stands for daily 
        price history intervals. Again, with a `Python` function you can think 
        of `interval=d1` as a named argument.
    
        More detailed explanations on both parameters and values are 
        specified in the API documentation.
    
    Finally, we end up with the URL 
    `#!python "https://api.coincap.io/v2/assets/pepe-cash/history?interval=d1"`
    
    <div style="text-align: center;">
        <iframe src="https://giphy.com/embed/l1Etfpt5pdYl34BuU" width="480" height="360" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/spongebob-spongebob-squarepants-season-5-l1Etfpt5pdYl34BuU"></a></p>
        <figcaption>Quite a complicated URL.</figcaption>
    </div>

### Request

If you've followed the construction of the URL closely, we can easily send 
another request to retrieve market data. This time around it is another `GET`
request, however with a query parameter.

```python
# construct the URL (same as above)
api_url = "https://api.coincap.io/v2"
coin_id = "pepe-cash"
endpoint = f"/assets/{coin_id}/history"
query_params = "?interval=d1"  # daily interval (if available)

url = f"{api_url}{endpoint}{query_params}"

# send the request
response = requests.get(url=url)
```

Again, convert the response to a `DataFrame` and print the first few rows.

```python
pepe_history = response.json()
pepe_history = pd.DataFrame(pepe_history["data"])

print(pepe_history.tail())
```

| priceUsd           | time           | date                      |
|--------------------|----------------|---------------------------|
| 0.0176438251661799 | 1726963200000  | 2024-09-22T00:00:00.000Z  |
| 0.0127411915131318 | 1727827200000  | 2024-10-02T00:00:00.000Z  |
| 0.0127704751708670 | 1727913600000  | 2024-10-03T00:00:00.000Z  |
| 0.0131082066240718 | 1728345600000  | 2024-10-08T00:00:00.000Z  |
| 0.0130405021808657 | 1728432000000  | 2024-10-09T00:00:00.000Z  |

We are now looking at the daily (if available) price history of `Pepe-Cash` in 
USD.

### Detour: Visualizations

As a bonus we can plot the price history and try to recreate the price 
charts seen on various market platforms. This Visualizations section is 
optional and should provide a glimpse into the possibilities of working with
APIs.

<div style="text-align: center;">
    <iframe src="https://giphy.com/embed/BQUITFiYVtNte" width="480" height="293" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/imagination-BQUITFiYVtNte"></a></p>
</div>

Regardless of whether you plot the price chart 
dynamically or statically, two preprocessing steps are necessary.

```python
# convert date and price to their appropriate types
pepe_history["date"] = pd.to_datetime(pepe_history["date"])
pepe_history["priceUsd"] = pepe_history["priceUsd"].astype(float)
```

=== "Option 1: Dynamic plot :fontawesome-solid-arrow-right: `plotly`"

    ```python
    import plotly.express as px
    
    fig = px.area(
        data_frame=pepe_history,
        x="date",
        y="priceUsd",
        title="Pepe Cash - Price History in USD",
        color_discrete_sequence=["#009485"],
    )
    fig.show()
    ```
    
    <div style="text-align: center;">
        <iframe src="/assets/python-extensive/data/api/pepe-plotly.html" width="100%" height="450px">
        </iframe>
    </div>


=== "Option 2: Static plot :fontawesome-solid-arrow-right: `matplotlib`"

    ```python
    import matplotlib.pyplot as plt
    
    # pandas plot method:
    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html
    pepe_history.plot(
        x="date",
        y="priceUsd",
        kind="area",
        title="Pepe Cash - Price History in USD",
        color="#009485",
    )
    plt.show()
    ```

    <div style="text-align: center;">
        <img src="/assets/python-extensive/data/api/pepe-matplotlib.svg" alt="Pepe Cash - Price History in USD">
    </div>

??? tip "Bonus: Styling the plot"

    If you want to style the dynamic plot further (to more closely resemble the
    price charts seen on market platforms) adjust colors, labels and add a 
    logo.

    ```python
    fig = px.area(
        data_frame=pepe_history,
        x="date",
        y="priceUsd",
        title="Pepe Cash - Price History in USD",
        color_discrete_sequence=["#009485"],
        template="plotly_dark"  # dark theme
    )
    # add the logo
    fig.add_layout_image(
        dict(
            source="https://cryptologos.cc/logos/pepe-pepe-logo.png?v=035",
            xref="paper",
            yref="paper",
            x=1,
            y=1.15,
            sizex=0.2,
            sizey=0.2,
            xanchor="right",
            yanchor="top",
        )
    )
    fig.show()
    ```

    <div style="text-align: center;">
        <iframe src="/assets/python-extensive/data/api/pepe-stylish.html" width="100%" height="450px">
        </iframe>
    </div>

???+ question "Rate conversion to :fontawesome-solid-euro-sign:"

    Since the price history is in USD, convert the prices to EUR. Conveniently,
    the API provides an endpoint for current exchange rates. 

    1. Use the appropriate `/rates/{{id}}` endpoint.
    2. Use the identifier (`id`) :fontawesome-solid-arrow-right: `euro` for the 
       endpoint.
    3. Construct the URL and send a `GET` request.
    4. Extract the exchange rate from the response. ==Hint:== 
        This time it is easier to deal with the `#!python dict` and not 
        perform a conversion to a `DataFrame`.
    5. Convert `#!python pepe_history["priceUsd"]` to EUR.
    
    Start with the given code snippet below:

    ```python
    import requests

    # get current Pepe price history in USD
    response = requests.get(url="https://api.coincap.io/v2/assets/pepe-cash/history?interval=d1")
    pepe_history = pd.DataFrame(response.json()["data"])
    pepe_history["priceUsd"] = pepe_history["priceUsd"].astype(float)

    # get exchange rate; your solution ...
    ```

## Conclusion

In this end-to-end example, we have seen how to retrieve data from an API, 
store it in a `DataFrame` and visualize it. With consecutive requests, we 
have pulled a list of cryptocurrencies, the price history of a specific 
coin and even converted the prices to EUR. 

Despite this specific use case, concepts like rate limits, endpoints, request
methods and query parameters were introduced along the way which are 
universal to APIs.

???+ info "Apply your knowledge"
    
    You should be able to apply your knowledge to other APIs as well. Here 
    are just a couple of other APIs[^1]:
    [^1]:
        Some of these APIs require authentication or are paid services.
    
    - [OpenWeatherMap](https://openweathermap.org/api) for weather data
    - [NASA](https://api.nasa.gov/) from astronomy pictures to earth 
        observation data
    - [Google Search](https://developers.google.com/custom-search/v1/overview?hl=de) 
        access search results programmatically
    - [Spotify](https://developer.spotify.com/documentation/web-api) access 
        Spotify's music data
    - [Instagram](https://developers.facebook.com/docs/instagram-platform) 
        access Instagram's data

    The possibilities are endless. 🚀

If you want to dive deeper into APIs, we recommend the following resources:

- [HTTP Status Codes](https://developer.mozilla.org/de/docs/Web/HTTP/Status): 
    Dive deeper into the server responses and their various status codes.
- [FastAPI](https://fastapi.tiangolo.com/): Build an API yourself with Python
