# Dimensionality Reduction

## Principal Component Analysis (PCA)

In data science and machine learning, we often encounter data sets with 
hundreds or even thousands of features. We speak of high-dimensional data 
sets. While these features may contain valuable information, working with 
such high-dimensional data can be computationally expensive, prone to 
overfitting, and difficult to visualize. This is where another 
unsupervised method, dimensionality reduction comes in — a technique used to 
simplify data sets, while retaining much of the critical information.

One of the most widely used methods for dimensionality reduction is 
Principal Component Analysis (PCA). PCA transforms a high-dimensional (= 
lots of features) data set into a smaller set of features (components). In
practice, PCA can reduce hundreds of features down to just 2 or 3 
features, making PCA an ideal tool for visualization, preprocessing, and 
feature extraction.

In this section, we will explain the inner workings of PCA and apply it to
the semiconductor data set.

### What is PCA?

PCA is a **linear transformation technique** that identifies the directions 
(also called **principal components**) in which the data varies the most. 
These principal components capture as much variance as possible. PCA has a 
variety of applications, such as:

- **Data visualization**: Plot a dimensionality reduced data set on 2D.
- **Preprocessing**: Removing noise or redundant features while retaining the
  essential patterns in data.
- **Feature engineering**: Summarizing high-dimensional data into a smaller set
  of meaningful features.

### How does it work?

PCA follows these essential steps:

1. **Compute the covariance matrix**: PCA captures relationships between
   features by calculating the covariance between them.

    ???+ info
    
        Think of the covariance matrix as the "spread" of the data. PCA looks 
        at the interaction :fontawesome-solid-arrow-right: the correlation of 
        features with each other.

2. **Eigen decomposition**: Identify the eigenvalues and eigenvectors of the
   covariance matrix. The eigenvectors represent the directions of the
   principal components, while the eigenvalues represent the amount of variance
   captured by each component.

    ???+ info
    
        If you want to know more about eigenvalues and eigenvectors, check out
        this [site](https://www.mathsisfun.com/algebra/eigenvalue.html).

3. **Rank components**: Components are ranked by their eigenvalues. The first
   principal component captures the most variance, the second captures the
   next-most, and so on.
4. **Transform the data**: Project the original data onto the top principal
   components to reduce its dimensionality.

### The mathematical objective

Let’s assume we have a data set \(X\) with \(p\) features (dimensions). We
aim to transform \(X\) into a new matrix \(Z\) with \(k\) features such
that \(k < p\), while retaining as much variance as possible.

The transformation (described previously under point 4) is defined as:

???+ defi "PCA transformation"

    \[
    Z = X W
    \]

    Where:
    
    - \(Z\) is the transformed data set in the lower-dimensional space,
    - \(W\) is a matrix whose columns are the top \(k\) eigenvectors of the
        covariance matrix of \(X\).

???+ tip

    Dimensionality reduction helps in combating the *curse of dimensionality*, 
    a phenomenon where the performance of algorithms deteriorates with an 
    increase in the number of features. Algorithms like clustering 
    often struggle to find meaningful patterns when working with a 
    high-dimensional data set.

## Example

It’s time to apply PCA to real-world data. We'll revisit the semiconductor
data set that we used in the previous clustering chapter. The first goal 
is to use PCA to reduce the data set's dimensions and visualize them.

### Prepare the data

First, we load the data set. If you haven’t already downloaded it, you can grab
it below:

<div class="center-button" markdown>
[Download semiconductor data :fontawesome-solid-download:](../../../assets/data-science/algorithms/clustering/semiconductor.csv){ .md-button }
</div>

???+ question "Load the data"

    1. Load the `csv` file and assign it to a variable called `data`.

Before applying PCA, let’s make sure we deal with potential problems such as
missing values.

```python
# fill missing values with the mean
data = data.fillna(data.mean())
```

Next, scale the features to standardize the data set:

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()  # Z-Score
scaled_data = scaler.fit_transform(data)
```

### Apply PCA

We now apply PCA to reduce the dimensions. First, we fit the PCA model on
the `scaled_data`:

```python
from sklearn.decomposition import PCA

pca = PCA(random_state=42)  # (1)!
components = pca.fit_transform(scaled_data)
```

1. Although the above definition of PCA is deterministic, the actual 
   implementation can be stochastic (depending on the solver used). Since
   `svd_solver` is set to `#!python "auto"` by default, the results can 
   vary slightly. Long story short, setting `random_state` ensures 
   reproducibility in all cases.
