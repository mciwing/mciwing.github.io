# Introduction

With extensive data preparation knowledge, we can tackle the next
big part of the course: algorithms. An algorithm is a

> a set of mathematical instructions or rules that, especially if given to a
> computer, will help to calculate an answer to a problem.
> 
> [Cambridge Dictionary](https://dictionary.cambridge.org/de/worterbuch/englisch/algorithm)

In data science/machine learning, algorithms are used to solve problems 
such as modelling data to make prediction for unseen data or clustering data 
to find patterns.

The following chapters will introduce you to the most common algorithms, like 
linear and logistic regression, decision trees, and k-means clustering. We will
explore the theory as well as practical examples.
First, we establish two main categories of algorithms: supervised and 
unsupervised learning.

## Supervised Learning

Supervised learning is a type of machine learning where algorithms learn from 
^^labeled^^ training data to make predictions on new, unseen data. The term 
"supervised" comes from the idea that the algorithm is guided by a 
"supervisor" (the labeled data) that provides the correct answers during
training.

In supervised learning, each training example consists of:

- Input features (\(X\)): The characteristics or attributes we use to make 
    predictions
- Target variable (\(y\)): The correct output we want to predict

The algorithm learns the relationship between inputs (\(X\)) and outputs 
(\(y\)), creating a model that can then (hopefully!) generalize to new data.

### Example

Assume we want to predict apartment prices :fontawesome-solid-arrow-right: 
\(y\) based on their size plus the number of rooms 
:fontawesome-solid-arrow-right: \(X\):

```python hl_lines="16 17"
from sklearn.linear_model import LinearRegression

# apartment data [m², rooms]
X = [
    [75, 3],
    [120, 4],
    [50, 2],
]
y = [500_000, 675_000, 425_000]  # apartment prices

# use linear regression to predict apartment prices
model = LinearRegression()
model.fit(X, y)

# predict price for a new apartment with 150m² and 5 rooms
new_house = [[150, 5]]
predicted_price = model.predict(new_house)
```

For each new observation, we can use the trained model to predict the price.

---

### Classification vs. Regression

Supervised learning encapsulates both classification and regression tasks.

``` mermaid
graph LR
  A[Supervised Learning] --> B[Regression];
  A --> C[Classification];
```

---

#### Classification

Classification problems involve predicting discrete categories or labels. The
output is always one of a fixed set of classes. For instance, in binary
classification, the model decides between two possibilities. 

For example, the Portuguese retail bank data can be used to predict 
whether a customer would subscribe to a term deposit. The target variable is 
binary: yes or no.

On the other hand, multiclass classification handles three or more categories 
(like classifying animals in photos :fontawesome-solid-arrow-right: dog, 
cat, dolphin, tiger, elephant, etc.).

---

#### Regression

Regression problems, on the other hand, predict continuous numerical values.
Instead of categorizing inputs into classes, regression models estimate a
numerical value along a continuous spectrum. These models work by finding
patterns in the data to estimate a mathematical function that best describes
the relationship between inputs and the target variable.

---

#### Examples

<div class="grid cards" markdown>

-   __Classification__

    ---
    Predicting a ^^categorical^^ target variable:

    - Spam or not spam
    - Fraudulent or legitimate transaction
    - Medical diagnosis (disease or no disease)
    - Sentiment analysis of text (positive, negative, neutral)
    - Image classification (cat, dog, dolphin, etc.)
    - ...

-   __Regression__

    ---
    Predicting a ^^continuous^^ target variable:
  
    - Apartment prices (like in the toy example above)
    - Temperature
    - Sales revenue
    - ...

</div>

???+ info
  
    No matter if you're dealing with a classification or regression task, the 
    key to successful supervised learning lies in having high-quality labeled
    data and selecting appropriate features that have predictive power for the 
    target variable.

## Unsupervised Learning

Contrary, unsupervised learning deals with ^^unlabeled^^ data to discover 
hidden patterns and structures. Unlike supervised learning, there is no 
"supervisor" providing correct answers - the algorithm must find
meaningful patterns on its own.

In unsupervised learning, we solely have:

- Input features (\(X\)): The characteristics or attributes of the data

The algorithm's task is to find groupings, reduce complexity, or reveal
underlying structures in the data.

### Example

Let's say we want to segment customers based on their shopping behavior:

```python hl_lines="13 14"
from sklearn.cluster import KMeans

# customer data [annual_spending, avg_basket_size]
X = [
    [1200, 50],
    [5000, 150],
    [800, 30],
    [4500, 140],
    [1000, 45]
]

# use k-means to find customer segments
model = KMeans(n_clusters=2)
segments = model.fit_predict(X)
```

The algorithm will group similar customers together without being told what
these groups should be - it discovers the patterns naturally from the data.

---

### Clustering & Dimensionality Reduction

Unsupervised learning can be further divided into two main categories:

``` mermaid
graph LR
  A[Unsupervised Learning] --> B[Clustering];
  A --> C[Dimensionality Reduction];
```

---

#### Clustering

Clustering algorithms group similar data points together based on their
features. The goal is to find cluster/groups in the data without any 
prior knowledge of the groups.

---

#### Dimensionality Reduction

Dimensionality reduction techniques aim to reduce the number of input features
while preserving the most important information. This can help to simplify
complex data, speed up algorithms, and improve model performance.

---

### Examples

<div class="grid cards" markdown>

-   __Clustering__

    ---
    Clustering/grouping of similar data points:

    - Customer segmentation in marketing
    - Anomaly detection
    - Finding similar products in recommendations
    - ...

-   __Dimensionality Reduction__

    ---
    Reducing the complexity of data:
  
    - Feature extraction from high-dimensional data
    - Visualization of complex datasets
    - Noise reduction in signals
    - ...

</div>

???+ info

    While unsupervised learning offers powerful ways to explore and understand
    data, its results can be harder to evaluate since there are no "correct"
    answers to compare against. The value of the results often depends on how
    meaningful the discovered patterns are for the specific application.

---
