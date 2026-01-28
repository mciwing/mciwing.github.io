# Regression

In machine learning, we often face the challenge of making predictions based on
patterns in our data. Linear regression, a supervised method addresses 
this by providing a straightforward approach to modeling the relationship 
between variables, allowing us to both explain existing data and make 
predictions with new observations.

This chapter introduces linear regression through a practical example, starting
with a simple housing prices model. We'll explore the mathematics behind 
linear regression and how to evaluate model performance (with the coefficient 
of determination \( R^2 \)), These are concepts that will accompany us 
throughout the next few chapters.

## Example

`scikit-learn` provides a couple of data sets for download. To fit a linear 
regression on a real-world example, we load the California housing data set.
More information about the California Housing data set can be found 
[here](https://scikit-learn.org/stable/datasets/real_world.html#california-housing-dataset).

???+ info

    Data reference:

    ^^Pace, R. Kelley and Ronald Barry, Sparse Spatial Autoregressions, 
    Statistics and Probability Letters, 33:291-297, 1997^^

Our objective is to model the
target variable \(y\) using input variables \(X\). In this case, \(y\) corresponds to 
the median house value, expressed in hundreds of thousands of dollars ($100,000).
Below figure shows all houses colored by their median value \(y\).

<figure markdown="span">
    <img 
        src="/assets/data-science/algorithms/regression/california.png"
        width=75%
    >
    <figcaption>
        California median house values (in $100,000): Higher values are 
        concentrated along the coast and in major urban centers such as 
        San Francisco and Los Angeles.
    </figcaption>
</figure>

For \(X\) a couple of variables are available, such as house age (HouseAge) and
average bedrooms (AveBedrms). We start by modelling \(y\) with a single input 
variable \(X\) as it allows us to easily visualize and interpret the results.

Start by loading the data:

```python hl_lines="3"
from sklearn.datasets import fetch_california_housing

X, y = fetch_california_housing(return_X_y=True, as_frame=True)
print(X.head())
```

Conveniently, by setting `#!python return_X_y=True`, the function splits the 
input variables \(X\) and the target \(y\).

???+ question

    The data frame `X` contains the variables `#!python "Latitude"` and 
    `#!python "Longitude"`, since we won't need them, remove them from the data
    frame. Tip: Consult the pandas [documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html).
