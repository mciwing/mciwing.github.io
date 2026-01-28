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

???+ info

    This chapter adapts and expands upon:

    ^^scikit-learn: *Ordinary Least Squares and Ridge Regression*[^1]^^

    ^^scikit-learn: *Linear Models*[^2]^^ 

    [^1]:
        [https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols_ridge.html](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols_ridge.html)
    [^2]:
        [https://scikit-learn.org/stable/modules/linear_model.html](https://scikit-learn.org/stable/modules/linear_model.html)

## Theory

Linear regression, also known as Ordinary Least Squares (OLS), models the 
relationship between a target variable \(y\) and one or more input variables 
\(X\). The goal is to find the best linear function that predicts \(\hat{y}\) 
from \(X\).

???+ defi "Linear combination"

    \[
    \hat{y} = w_0 + w_1 \cdot x_1 + w_2 \cdot x_2 + ... + w_n \cdot x_n
    \]

    where:
    
    - \(w_0\) is the **intercept** (bias term)
    - \(w_1, w_2, ..., w_n\) are the **coefficients** (weights)
    - \(x_1, x_2, ..., x_n\) are the input features

The term "Ordinary Least Squares" refers to the optimization objective, 
finding the weights \(w_0, w_1, ..., w_n\) that minimize the sum of squared 
differences called residuals between the actual values \(y\) and predicted 
values \(\hat{y}\).

???+ defi "Cost function"

    \[
    \text{min} \quad \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
    \]

    where \(n\) is the number of observations.

This minimization ensures that our model makes the smallest possible errors 
on average when predicting the training data. Let's look at an example.

## Example

`scikit-learn` provides a couple of data sets for download. To fit a linear 
regression on a real-world example, we choose the California housing data set.
More information about the California Housing data set can be found 
[here](https://scikit-learn.org/stable/datasets/real_world.html#california-housing-dataset).

???+ info

    Data reference:

    ^^Pace, R. Kelley and Ronald Barry, Sparse Spatial Autoregressions, 
    Statistics and Probability Letters, 33:291-297, 1997^^

Our objective is to model the target variable \(y\) using input variables 
\(X\). In this case, \(y\) corresponds to the median house value, expressed in 
hundreds of thousands of dollars ($100,000).
Below figure shows all houses in California colored by their median value 
\(y\).

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

### Load the data

Start by loading the data:

```python hl_lines="3"
from sklearn.datasets import fetch_california_housing

X, y = fetch_california_housing(return_X_y=True, as_frame=True)
print(X.head())
```

Conveniently, by setting `#!python return_X_y=True`, the function splits the 
input variables \(X\) and the target \(y\). Note, \(X\) contains multiple input
variables such as such as house age *HouseAge* and average bedrooms *AveBedrms*.
However, some are not needed.

???+ question

    The data frame `X` contains the variables `#!python "Latitude"` and 
    `#!python "Longitude"`, remove them from the data frame. Tip: Consult the 
    pandas [documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html).

### Split the data

Before training our OLS model, we need to split our data into two distinct sets:

- **Training set**: Used to fit the model and learn the optimal weights 
    (80% of data)
- **Test set**: Used to evaluate the model's performance on unseen data 
    (20% of data)

Think of this like preparing for an exam: you study from practice problems 
(training set) and then test your knowledge with new questions (test set). 
This separation allows us to assess whether our model can accurately predict 
house prices it hasn't seen before, rather than just memorizing the training 
data.

???+ info

    The 80/20 split is a common convention, but not a strict rule. Depending on
    the data set size, other split ratios might be a better fit.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, shuffle=True
)
```

Let's break the code snippet down:

1. `train_test_split()` takes the complete data set (`X` and `y`) as input
2. Splits off 20% for testing (`#!python test_size=0.2`)
3. Uses a fixed seed (`#!python random_state=42`) which ensures the same
    outcome every time the code snippet is executed.
4. Randomly shuffles the data (`#!python shuffle=True`) to remove any inherent
    ordering

???+ info "Why shuffle?"
    
    Some data sets may have inherent order (e.g., the houses could be sorted by
    location). Shuffling ensures that both training and test sets are 
    representative of the entire data distribution.

After splitting, we put our test data (`X_test` and `y_test`) aside and only
use it at the very end.

### Intuition

For the first OLS model, we use a single input variable \(X\) as it allows us 
to easily visualize and interpret the results. The choice falls on the median 
income at the house location, referred to as *MedInc*. 
Visualize the target and input variable in a scatter plot:

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.scatter(X_train["MedInc"], y_train, color="#009485")
ax.set(
    xlabel="Input Variable (MedInc)",
    ylabel="Target (House Value)",
    title="Train set",
)
plt.show()
```

<div class="grid cards" markdown>

-   __Scatter Plot__ 

    --- 
    
    Looking at the scatter plot, you might intuitively imagine drawing a straight 
    line through the points that best captures the trend. This intuition is 
    exactly what OLS does mathematically, it finds the optimal line that minimizes 
    the distance between the line and all data points. :point_down:

-   <figure markdown="span">
        <img 
            src="/assets/data-science/algorithms/regression/scatter-dark.png#only-dark"
        >
        <img 
            src="/assets/data-science/algorithms/regression/scatter-light.png#only-light"
        >
    </figure>

-   <figure markdown="span">
        <img 
            src="/assets/data-science/algorithms/regression/regression-dark.png#only-dark"
        >
        <img 
            src="/assets/data-science/algorithms/regression/regression-light.png#only-light"
        >
    </figure>

-   __Best-Fit Line__

    ---

    The OLS model finds the line that minimizes the sum of squared residuals,
    the vertical distances between each point and the line. Recall from the 
    theory section that this is exactly what the cost function measures:
    
    \[
    \text{min} \quad \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
    \]

</div>

### Train the model

Our next step is to train an OLS model to automatically find this "best-fit" 
line. Remember, since we have one input variable, the linear combination 
simplifies to:

\[
\hat{y} = w_0 + w_1 \cdot x_1
\]

where:

- \(\hat{y}\) is the predicted house price
- \(w_0\) is the intercept (baseline house price)
- \(w_1\) is the coefficient for the input variable *MedInc* (\(x_1\))

Start by importing the linear regression model from the package.

```python
from sklearn.linear_model import LinearRegression

# create an instance
model = LinearRegression()
```

At this point, the model is not trained, however that can be easily done
using the `fit()` method. Remember, to use the training set 

```python
model.fit(X=X_train[["MedInc"]], y=y_train)
```

#### Intercept and coefficient

After training, we can inspect the model's learned parameters. The intercept 
and coefficient that define the best-fit line:

```python
print(f"Intercept (w₀): {round(model.intercept_, 4)}")
print(f"Coefficient (w₁): {round(model.coef_[0], 4)}")
```

```title=">>> Output"
Intercept (w₀): 0.4446
Coefficient (w₁): 0.4193
```

These values tell us that our linear model is:

\[
\hat{y} = 0.4446 + 0.4193 \cdot x_1
\]

**Interpretation:**

- **Intercept (0.4446)**: The baseline house value when *MedInc* is zero 
    (approximately $44,460)
- **Coefficient (0.4193)**: For each unit increase in *MedInc*, the house value
    increases by ~ $41,930

### Predictions

Now that the model is trained, we can predict house prices for new observations. 
Let's predict the price \(\hat{y}\) for a house in an area where 
*MedInc* is `#!python 3.5`:

```python
import pandas as pd

new_house = pd.DataFrame({"MedInc": [3.5]})
new_price = model.predict(new_house)
print(round(new_price, 4))
```

```title=">>> Output"
1.9123
```

The model predicts a house value of approximately **$191,230**.

#### Manual validation

We can verify this prediction using our linear equation. Substituting \(x_1 = 3.5\):

\[
\begin{align}
\hat{y} &= 0.4446 + 0.4193 \cdot 3.5 \\
&= 1.9122
\end{align}
\]

This matches our model's prediction!

???+ question "Practice: Make your own prediction"

    Calculate the predicted house price for an area where *MedInc* is 
    `#!python 5.0`.
    
    1. Use `#!python model.predict()` to get the prediction.
    2. Validate it by hand using the linear equation.
    3. Do the results match?
