# Where to get data?

In this section, we will explore different ways to retrieve data.
We will start with tabular data, move on to APIs, and finish with some tips.

## API

An application programming interface (API) is a set of rules and protocols
that allows one software application to interact with another.
In other words, it is a way to communicate with a server. Some of these
servers are openly available and host data that can be accessed by anyone.
Others require authentication and are therefore paid services.

To illustrate the practical interaction with APIs, we will retrieve
cryptocurrency data from the [CoinCap API](https://docs.coincap.io/).

We will pull the latest price history of a specific 
cryptocurrency, perform a conversion from USD to EUR, and plot a 
line chart to visualize the data.

???+ info "Disclaimer"
    
    This section merely demonstrates APIs on the example of cryptocurrency 
    market data.

    Cryptocurrencies involve significant financial risk. 
    Investors should conduct thorough research and consult financial professionals 
    before making investment decisions. The code examples presented herein are 
    for illustrative purposes only and do not constitute financial advice 
    nor do we endorse any companies mentioned.


???+ question "Reading the documentation"
    
    Open the CoinCap API documentation ([here](https://docs.coincap.io/)) and 
    browse through the site for a minute or two.

### Rate limits

During the task, you should have noticed that the API provides information 
on rate limits. Rate limits are the number of requests that can be made to
the server in a given time frame. If you exceed the rate limit, the server
will respond with an error message. In this specific case, we can make up to
200 requests per minute which is more than enough for our use case.
These rate limits are set by the provider and can vary from one API to another.

But how can we request data from the server to retrieve a price history? To 
answer this question, the concept of endpoints is introduced.

### Endpoints

An endpoint is a specific URL that the API uses to perform a specific action.
For example, the endpoint `/assets` returns a list of all cryptocurrencies.
To send a request to the server, we need to specify the endpoint in the URL.
The server will then respond with the requested data (if everything went 
smoothly).

To request all cryptocurrencies, we can use the following URL:
```
https://api.coincap.io/v2/assets
```

`https://api.coincap.io/v2` is simply the URL of the API and `/assets` is 
the endpoint of our interest.

???+ question "Send your first request"

    Open the URL `https://api.coincap.io/v2/assets` in your browser and 
    observe the response.

<?quiz?>
question: Which Python type does the output of your request most closely resemble?
answer: A <code>pandas</code> <code>DataFrame</code>
answer: A simple <code>list</code>
answer-correct: A simple <code>dictionary</code>
content:
<p>Correct! The server response you got was actually in the form of a 
<code>JSON</code> file. 
This is a common format for APIs to return data. We can easily read the 
<code>JSON</code> with <code>Python</code>.
</p>
<?/quiz?>

Since we don't want to manually use the browser anytime we want to retrieve 
data, we now replicate the request in `Python` :fontawesome-brands-python:. 
To send requests we can make use of the appropriately named
[`requests`](https://requests.readthedocs.io/en/latest/) package.

???+ question "Setup"
    
    Create a new virtual environment and install the `requests` package.
    
    ```bash
    pip install requests
    ```

The below snippet sends a request to the `/assets` endpoint and stores the
response in a variable.

```python
import requests

response = requests.get(url="https://api.coincap.io/v2/assets")
data = response.json()  # assign the response (JSON) to a variable
```

???+ question "Validate the above quiz question"
    
    What type is returned by the `#!python response.json()` method? 
    Check the `#!python type()` of the `data` variable.

#### Detour: Methods

In the above code snippet, we used `requests` `get()` method to send a
`GET` request to the server. `GET` is solely to retrieve data from the 
server no data is changed on the server-side. If you have another look at the 
CoinCap API docs you will discover that all endpoints like `/assets`, `/rates`,
or `/markets` are prefaced by the `GET` method.

Nevertheless, there `GET` is not the only method, there are also `POST`, `PUT`,
`DELETE`, and `PATCH`. Following table provides a brief overview, but don't 
worry about these methods too much for now as we will continue solely with 
`GET` methods.

| Method | Description                         | `requests` method   |
|--------|-------------------------------------|---------------------|
| GET    | Retrieve data from the server       | `requests.get()`    |
| POST   | Create data on the server           | `requests.post()`   |
| PUT    | Update data on the server           | `requests.put()`    |
| DELETE | Delete data on the server           | `requests.delete()` |
| PATCH  | Partially update data on the server | `requests.patch()`  |


???+ info
    
    If you need to revisit the topic of HTTP methods or simply want to dive 
    deeper, [here's](https://restfulapi.net/http-methods/) a great article.

**Validate a response etc**

![](https://tokenscan.io/img/cards/PEPECASH.jpg)
