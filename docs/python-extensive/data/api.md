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

???+ question "Open a website :open_mouth:"
    
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

To send the same request to the `/comments` endpoint we can use following code
snippet.

```python
import requests

response = requests.get("https://jsonplaceholder.typicode.com/comments")
```

Since `response` does not explicitly return the data we have to access it with

```python
data = response.json()
```

???+ question "Validate the above quiz question"
    
    What type is returned by the `#!python response.json()` method? 
    Check the `#!python type()` of the `data` variable.

We can easily convert the data into a tabular format with `pandas`.

```python
import pandas as pd

data = pd.DataFrame(data)
```

???+ info

    Looking at `data.shape` you'll notice that we retrieved 500 rows of data
    with a single request. With a `pandas.DataFrame` you can utilize all your
    knowledge you gained so far to further handle and plot the data.

???+ question "Send a request with Python"

    Pick one of the 6 available endpoints. Write code to

    1. Send a request
    2. Access the data

### Methods

In the above code snippet, we applied `requests` `get()` method.
The `get` method solely retrieves data from the server, that is no data is 
sent to or modified on the server. In fact, all endpoints of {JSON} Placeholder 
can be accessed using the `GET` method.

Nevertheless, `GET` is not the only method, there are also `POST`, `PUT`,
`DELETE`, and `PATCH`. Following table provides a brief overview:

| Method | Description                         | `requests` method   |
|--------|-------------------------------------|---------------------|
| GET    | Retrieve data from the server       | `requests.get()`    |
| POST   | Create data on the server           | `requests.post()`   |
| PUT    | Update data on the server           | `requests.put()`    |
| DELETE | Delete data on the server           | `requests.delete()` |
| PATCH  | Partially update data on the server | `requests.patch()`  |

We will continue solely with `GET` methods.

<div style="text-align: center;">
    <iframe src="https://giphy.com/embed/XreQmk7ETCak0" width="373" height="280" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/retro-thumbs-up-XreQmk7ETCak0"></a></p>
</div>

???+ info
    
    If you need to revisit the topic of HTTP methods or simply want to dive 
    deeper, [here's](https://restfulapi.net/http-methods/) a great article.

## GitHub API

Since APIs serve different purposes, we switch to another real world example,
the GitHub API.

???+ info

    <div style="text-align: center">
        <img src="/assets/python-extensive/data/api/github-mark-white.png" 
        alt="GitHub Logo" width="75"/>
    </div>

    GitHub (github.com) is a popular web-based platform that serves as:
    
    - A hosting service for software development and version control
    - A place where developers store, share, and collaborate on code projects
    
    Think of GitHub as a social network for programmers - like a combination of 
    Google Drive, LinkedIn, and Instagram, but for code. Developers can:
    
    - Store their code in "repositories" (like folders)
    - Track changes to their code over time
    - Collaborate with others on projects
    - Share their work with the global developer community

Besides browsing GitHub on the web, we can also access information 
programmatically using their API. You can find more information 
[here](https://docs.github.com/de/rest/about-the-rest-api/about-the-rest-api?apiVersion=2022-11-28).

---

The base URL of the Github API is

```plaintext
https://api.github.com/
```

For example, we can retrieve the information of a specific user with the 
`/users` endpoint (official [documentation](https://docs.github.com/de/rest/users/users?apiVersion=2022-11-28#get-a-user)).

```plaintext
https://api.github.com/users/{username}
```

Using the above URL as is won't work, as we need to specify the specific 
user we are looking for. Thus, we have to replace `{username}` with the actual
user. This concept is known as a path parameter.

```python
username = "mciwing"
url = f"https://api.github.com/users/{username}"

response = requests.get(url)
data = response.json()
```

???+ tip

    With an f-string you can easily set the path parameter using a variable.

You accessed some public information on the `mciwing` user who manages the code
for this website and content you're currently reading.

???+ question "Not found"

    Use the same endpoint, this time around you intentionally have to look for 
    a non-existent username. Use this nonsensical one:

    ```python
    username = "iwo2jöiojfnvjlkhsnkjdvn"
    ```

    What's the response?

### HTTP Status Codes

When making requests to an API, the server responds with a status code 
indicating how the request was handled. Common status codes include:

| Code | Meaning               | Description                                |
|------|-----------------------|--------------------------------------------|
| 200  | OK                    | Request succeeded                          |
| 404  | Not Found             | Requested resource doesn't exist           |
| 403  | Forbidden             | Server understood but refuses to authorize |
| 429  | Too Many Requests     | You've exceeded the rate limit             |
| 500  | Internal Server Error | Something went wrong on the server         |

You can access the status code of any response using the `status_code` 
attribute.
Let's look at another example. With the

```plaintext
https://api.github.com/repos/{owner}/{repo}/contributors
```

endpoint, we can retrieve all contributors of a specific project. We access
information of this site's project (repository):

```python hl_lines="7"
owner = "mciwing"
repo = "mciwing.github.io"

url = f"https://api.github.com/repos/{owner}/{repo}/contributors"

response = requests.get(url)
print(response.status_code)  # (1)!
```

1. If everything went smoothly the status code is `#!python 200`

We can now easily sum up the contributions of all authors.

```python
n_contributions = 0
for contributor in response.json():
    n_contributions = n_contributions + contributor["contributions"]  # (1)!
print(n_contributions)
```

1. Remember, we are dealing with a `#!python dict` hence, we can easily access the number of contributions using the corresponding key `#!python "contributions"`.

At the time of writing `#!python 605` contributions were made by all authors 
to build this site. If you execute the code, the number has changed 
as we are continually working on the site. 

???+ tip

    That's the power of APIs, you're able to access the up-to date information.
    :mechanical_arm:
    If you want to have the latest data, all you have to do is execute your 
    code again.

## Limits

Although we have not encountered any limitations so far, most APIs come with 
various limitations to ensure fair usage:

<div class="grid cards" markdown>

-   :fontawesome-solid-clock: __Rate Limits__

    Rate limits restrict the number of requests you can make within a specific time
    frame. For example:

    - 200 requests per minute
    - 1000 requests per day
    - 5 requests per second

    If you exceed these limits, the server typically responds with a 
    `429 Too Many Requests` status code.

-   :fontawesome-solid-key: __Authentication__

    Many APIs require authentication for:

    - Tracking usage
    - Controlling access
    - Billing purposes

</div>

Depending on the API, you may experience rate limits or have to authenticate
your requests or simply have to pay for the service. Either way, the specific
API documentation will guide you through the process.

<!-- NASA example to conclude -->

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
