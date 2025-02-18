# Motivation

![header](../assets/header/pcc.png)

This course will teach you the basics of the 
**:fontawesome-brands-python: Python** programming language.

---

<div style="text-align: center;">
    <img 
        src="/assets/python/index/lattenspitze-top.gif" alt="lattenspitze code" 
        style="height: 400px; border-radius:10px;"
    >
</div>
<div style="text-align: center;">
    <img 
        src="/assets/python/index/lattenspitze-bottom.gif" alt="lattenspitze plotly" 
        style="height: 400px; border-radius:10px;"
    >
</div>
<figcaption style="text-align: center;">
    Creation of a 3D surface plot of the Lattenspitze. 🏔️<br>
    That's the power of Python - ease of use paired with a wide range of 
    functionalities stemming from a large developer community! 🦾
</figcaption>

## Why :fontawesome-brands-python: Python?

<div class="grid cards" markdown>

-   :fontawesome-brands-python: __Ease of use__

    ---

    `Python` with its syntax is easy to learn and yet very powerful.

-   :fontawesome-solid-robot: __Flexible__

    ---

    `Python` is a versatile language that can be used for data analysis, 
    automation, artificial intelligence, and many more applications.

</div>

---

The below section should give you an impression of what you can do with 
`Python`. This is not an extensive list by all means. It might sound 
trashy but if you can imagine something you probably can build it in 
`Python`.

???+ info

    Don't worry about the code snippets too much, after finishing the 
    course you'll have a better understanding and will be able to run 
    and modify code yourself. For now, the following snippets illustrate the
    capabilities of the language and what complex things you can achieve with
    little code. There is no need to execute it - Just take a look!

---

## Examples

???+ info "Just the beginning..."

    All of the following examples are from one of the courses featured on our
    website. If you stick around and explore subsequent `Python` courses you 
    will be able to easily implement all examples yourself! :rocket:

### :fontawesome-solid-robot: Machine Learning

With `Python` you can easily train your own machine learning models. In this 
example, with just a few lines of code, one such model (a decision tree) is 
fit and visualized[^1].
[^1]:
    [Scikit-learn](https://scikit-learn.org/stable/) is a Python package 
    for machine learning.

```py linenums="1"
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.tree import DecisionTreeRegressor, plot_tree

# load data
X, y = fetch_california_housing(return_X_y=True, as_frame=True)

# fit a decision tree
tree = DecisionTreeRegressor(
    random_state=784, max_depth=2, min_samples_leaf=15
)
tree.fit(X, y)

# visualize the tree
plot_tree(tree, filled=True, feature_names=X.columns, proportion=True)
plt.show()
```

<div style="text-align: center;">
  <img src="/assets/python/index/tree.svg" alt="Decision Tree">
  <figcaption>A decision tree visualized.</figcaption>
</div>

---

### Computer Vision/AI

Or how about state-of-the-art computer vision with YOLO[^2]?
[^2]:
    [YOLO](https://docs.ultralytics.com/) is an advanced real-time object detection
    model known for its speed and accuracy, enabling efficient identification and
    localization of objects within images and videos.

```py linenums="1"
from ultralytics import YOLO

# Load a pretrained YOLO11n model
model = YOLO("yolo11n.pt")

# Run inference on the source
results = model("https://ultralytics.com/images/bus.jpg")
results[0].show()
```

<div style="text-align: center;">
  <img src="/assets/python/index/yolo-pred.jpg" alt="Computer Vision" 
    style="width: 400px;">
  <figcaption>Object detection with YOLO.</figcaption>
</div>

---

### :fontawesome-solid-wand-sparkles: Automation

But it's not just machine learning and AI, you can also automate mundane tasks.
This code snippet fetches some data (from an online service) and writes an 
Excel file[^3].
[^3]:
    [requests](https://requests.readthedocs.io/en/latest/) is a Python package
    to interact with APIs.

```py linenums="1"
import pandas as pd
import requests

url = "https://api.coincap.io/v2/assets/pepe-cash/history?interval=d1"
response = requests.get(url)

data = pd.DataFrame(response.json()["data"])
data.to_excel("price-history.xlsx", index=False)
```

### :fontawesome-solid-chart-pie: Visualizations

You can create stunning and interactive visualizations[^4]. Let's visualize 
the above written Excel file.
[^4]:
    [Plotly](https://plotly.com/python/) is a Python graphing package that 
    lets you create interactive, publication-quality graphs.

```py linenums="1"
import pandas as pd
import plotly.express as px

data = pd.read_excel("price-history.xlsx")
fig = px.area(
    data_frame=data,
    x="date",
    y="priceUsd",
    title="Price History in USD",
    color_discrete_sequence=["#009485"],
)
fig.show()
```

<div style="text-align: center;">
    <iframe src="/assets/python/index/price-history.html" width="100%" height="400px">
    </iframe>
</div>

---

### :fontawesome-solid-globe: Web Development

You can create websites, **just like this one**. In fact, all the 
heavy lifting of this site is done by `Python` and tools developed by its 
community.

The most important package used to build this site was 
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/),
a widely used and customizable static site generator. :heart:

---

## Getting Started...

In the next sections, we will install `Python` including the code editor 
`Visual Studio Code`.

???+ tip

    Both Python and Visual Studio Code are already pre-installed on PCs in
    the MCI computer rooms. If you are working with your own computer, 
    please proceed to the next page.
