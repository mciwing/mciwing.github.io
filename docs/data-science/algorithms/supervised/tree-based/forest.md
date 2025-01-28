# Random Forest

While decision trees are easy to interpret, they have several drawbacks: they
are prone to overfitting and are sensitive to slight changes in the data.

Random Forest is an ensemble method that addresses these drawbacks at the cost
of slightly reduced interpretability. At its core, a random forest is simply a
collection of decision trees. Since we have already extensively discussed the
CART (Classification and Regression Trees) algorithm, we can dive right in.

## The basics

???+ info

    Random forests were introduced by Leo Breiman in 2001. The following 
    section closely follows the original paper.

    ^^Breiman, L. Random Forests. *Machine Learning 45*, 5–32 (2001).^^
    [https://doi.org/10.1023/A:1010933404324](https://doi.org/10.1023/A:1010933404324)

A random forest combines multiple decision trees to create an ensemble model.
The idea is to grow multiple trees and average their predictions. Thus, 
resulting in a more robust model that improves generalization and reduces
overfitting.

The randomness in a random forest stems from two techniques:

1. Bootstrap sampling
2. Random feature selection

### Bootstrap sampling

The first technique is known as **bootstrap sampling**. Given a
training set of size $N$, we draw $N$ samples ==with replacement==. This means 
that some samples may be repeated, while others may not be included at all. 
This results in a new training set of the same size as the original, but with 
some samples missing and others duplicated.

Each tree is fit on a different bootstrap sample. Intuitively speaking, this 
means that each tree sees a slightly different "version" of the training data.

### Random feature selection

The second technique is **random feature selection**. 
Remember, that a CART is grown by selecting the best split at each node.
This is done by considering all features. Contrary when growing trees for a 
random forest, we only consider a random subset of features at each split. 

---

### Putting it all together

Each tree in a random forest is fit on a bootstrap sample and uses a random
subset of features at each split.
In case of regression, the predictions of all trees are simply averaged. In 
case of classification, the majority vote is taken. 

It was observed that introducing randomness in the tree-growing process
improves the model performance.

???+ info

    Contrary to the classic CART, random forests do not constrain the tree 
    growth. I.e., trees are fully grown and not pruned.

## Examples

With a basic understanding of random forests we take a look at some 
examples. As always, we'll use our favorite machine learning package (at 
least that of the author :wink:) `scikit-learn`.

In order to focus on the random forest implementation and its parameters, we'll
reuse the California housing data (for regression) and the breast cancer data
(for classification). Both were utilized in the decision tree examples.

### Regression

Let's start with building a random forest to predict California housing prices.

#### Load data

As usual, we load the data and split it into a training and test set in 
order to evaluate the model later on.

```python
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split

X, y = fetch_california_housing(return_X_y=True, as_frame=True)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, shuffle=True
)
```

#### Fit the model

Just like with decision trees, `scikit-learn` provides two separate classes 
for regression and classification, namely `RandomForestRegressor` and 
`RandomForestClassifier`. Both are part of the `ensemble` module.

```python
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(random_state=784)  # (1)!
model.fit(X_train, y_train)
```

1. As a random forest is well random :sweat_smile:, we set the 
   `random_state` to ensure the reproducibility of our results.

Depending on your setup, the fitting process might take a couple of seconds.

#### Evaluate the model

```python
score = model.score(X_test, y_test)
print(f"Model performance (R²): {round(score, 2)}")
```

```title=">>> Output"
Model performance (R²): 0.81
```

???+ info

    Remember, that the `score()` method of a decision tree regressor 
    (`DecisionTreeRegressor`) returned the coefficient of determination 
    \(R^2\). The same applies to random forests.

Compared to a single tree with an \(R^2\) of 0.61, the random forest performs
considerably better with an \(R^2\) of 0.81. You can re-visit the according 
section [here](cart.md#fit-and-evaluate-the-model).

???+ question "How many trees are in the forest?"
    
    Consult the `scikit-learn` docs to find out how many trees are in the 
    forest by default. Use following question for self-assessment.

<?quiz?>
question: How many trees form a forest by default?
answer: None, you have to pass it as argument.
answer: 1000
answer: 1, the forest defaults to a single decision tree.
answer-correct: 100
content:
<p>Correct, the parameter <code>n_estimators</code> defaults to 100 trees.</p>
<?/quiz?>

???+ info

    If you want to get closer to the original definition of a random forest 
    regressor by Breiman, you have to set the `max_features` parameter. 
    Specifically, with \(m\) features, the number of features considered at 
    each split should be \(\frac{m}{3}\) for regression.

    ```python hl_lines="2"
    RandomForestRegressor(
        max_features=len(X_train.columns) // 3,
        random_state=784
    )
    ```

    By default, `scikit-learn` considers \(m\) features for each split.

???+ tip

    If you're unsure how to set parameters of a model (such as `max_features`),
    stick to the defaults. `scikit-learn` provides sensible defaults 
    that work well. Later on, we will explore methods to automatically tune 
    these hyperparameters.

### Classification

Next, we switch to a classification task.

???+ question

    Load the breast cancer data, fit and evaluate a random forest.
    
    1. Load the data and split it into a training and test set.
    2. Load the appropriate random forest class.
    3. Fit the model.
    4. Evaluate the model on the test set.

    Hint: This and the previous chapter should provide all necessary
    information, to solve the tasks.

#### Inspecting the forest

We can even inspect all individual trees of our ensemble forest. Simply access
the attribute `estimators_` of your fitted model.

```python
print(model.estimators_)  # (1)!
```

1. Assuming, you named the forest from the above task `model`.

```title=">>> Output"
[
    DecisionTreeClassifier(max_features=1.0, random_state=1877362837), 
    DecisionTreeClassifier(max_features=1.0, random_state=1395144809)
    ...
]
```

`estimators_` is a list of individual tree instances. If you're dealing with a
`RandomForestRegressor`, `estimators_` is a list of `DecisionTreeRegressor`.
