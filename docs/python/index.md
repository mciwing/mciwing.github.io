# Why Python?

This crash course on

<div style="text-align: center;">
  <img src="https://www.python.org/static/img/python-logo.png" alt="Python Logo">
</div>

will teach you the basics of the Python programming language.

## Motivation

<div class="grid cards" markdown>

-   :fontawesome-brands-python: __Ease of use__

    ---

    `Python` with its syntax is easy to learn and yet very powerful.

-   :fontawesome-solid-robot: __Flexible__

    ---

    `Python` is a versatile language that can be used for web development, 
    data analysis, artificial intelligence, and many more.

</div>

---

The below section should give you an impression of what you can do with 
`Python`. This is not an extensive list by all means. I might sound 
trashy but if you can imagine something you probably can build it in 
`Python`.

Don't worry about the code snippets too much, after finishing the 
course you'll have a better understanding of them and will be able to run 
and modify code yourself. For now, the snippets illustrate the capabilities 
of the language and what complex things you can achieve with little code.

---

### Examples

#### :fontawesome-solid-chart-pie: Visualizations

You can create stunning and interactive visualizations[^1].
[^1]:
    [Plotly](https://plotly.com/python/) is a Python graphing library that 
    lets you create interactive, publication-quality graphs.

```py
# Source: https://plotly.com/python/tile-county-choropleth/
import plotly.express as px

df = px.data.election()
geojson = px.data.election_geojson()

fig = px.choropleth_map(
    df,
    geojson=geojson,
    color="Bergeron",
    locations="district",
    featureidkey="properties.district",
    center={"lat": 45.5517, "lon": -73.7073},
    map_style="carto-positron",
    zoom=9,
)
```

<div style="text-align: center;">
    <iframe src="/assets/python/index/plot.html" width="100%" height="400px">
    </iframe>
</div>

---

#### :fontawesome-solid-robot: Machine Learning/AI

... or you can easily train your own machine learning models. In this 
example, with just a few lines of code, a decision tree is fit and 
visualized[^2].
[^2]:
    [Scikit-learn](https://scikit-learn.org/stable/) is a Python library 
    for machine learning.

```py
# Source: https://scikit-learn.org/stable/auto_examples/tree/plot_unveil_tree_structure.html#train-tree-classifier
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree

iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

clf = DecisionTreeClassifier(max_leaf_nodes=3, random_state=0)
clf.fit(X_train, y_train)

plot_tree(clf)
plt.savefig("tree.svg")
```

<div style="text-align: center;">
  <img src="/assets/python/index/tree.svg" alt="Decision Tree" style="height:300px;">
</div>

---

#### :fontawesome-solid-wand-sparkles: Automation

... or automate tasks that you would have otherwise done manually.
This code snippet fetches some data (from an online service) and writes it to a
file[^3].
[^3]:
    [HTTPX](https://www.python-httpx.org/) is a Python library to interact 
    with APIs.

```py
import json
from pathlib import Path

import httpx

url = "https://pokeapi.co/api/v2/pokemon/charmander"

response = httpx.get(url)

with Path("charmander.json").open("w") as file:
    json.dump(response.json(), file, indent=4)

```

---

#### :fontawesome-solid-globe: Web Development

You can create websites, **just like this one**. In fact, all the 
heavy lifting of this site is done by `Python` and tools developed by its 
community.
