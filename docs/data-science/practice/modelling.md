## Introduction

In this chapter, we start our modelling efforts. Let's dive right in.

Create a new notebook or script. Your project should now look like this:

```plaintext hl_lines="6"
📁 bank_model/
├── 📁 .venv/
├── 📁 data/
├───── 📄 bank-merged.csv
├── 🐍 preparation.py
├── 🐍 modelling.py
├── ...
```

Copy the code block from the previous recap section to get started.
[:octicons-link-external-16:](data-preparation.md#code-recap)

## Apply preprocessing

Now it is time to actually apply all preprocessing steps. To prevent
information leakage, we will split the data into training and test sets first.

```python
from sklearn.model_selection import train_test_split

# remove the target from data and assign it to y
y = data.pop("y")
X = data

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

???+ tip

    By default `train_test_split()` shuffles the data before splitting which is a
    good practice. It helps to avoid any bias that might be present in the order of
    the data.

    However, if you are ever working with data that is dependent on the order (time
    series data), you should not shuffle the data. In that case, set
    `#!python shuffle=False`.

Now apply the preprocessing steps (from the previous chapter) to the training
and test sets:

```python
# impute missing values
impute.fit(X_train)
X_train = impute.transform(X_train)
X_test = impute.transform(X_test)

# convert back to DataFrame
X_train = pd.DataFrame(X_train, columns=X.columns)
X_test = pd.DataFrame(X_test, columns=X.columns)

# apply preprocessing (OneHotEncoder, KBinsDiscretizer & StandardScaler)
preprocessor.fit(X_train)
X_train = preprocessor.transform(X_train)
X_test = preprocessor.transform(X_test)
```

???+ info

    The `impute.transform()` method returns an array. Since the `preprocessor`
    requires the column names of our data, we need to convert the array back to a
    `DataFrame`. Else the `preprocessor` will not work!

______________________________________________________________________

> The general rule is to never call `fit` on the test data.
>
> [`scikit-learn`: Common pitfalls and recommended practices](https://scikit-learn.org/stable/common_pitfalls.html#data-leakage)

???+ info

    For example, when `impute.fit(X_train)` is called, the `SimpleImputer`
    calculates the mode solely from the training data - `X_train`. When
    `impute.transform(X_test)` is called, the `SimpleImputer` uses the mode
    calculated from `X_train` to fill in missing values in `X_test`. So we never
    use the test set to calculate the mode.

    The same principles apply to the `preprocessor` and thus we can prevent
    information leakage.

______________________________________________________________________

## Train a model

For starters, we will train a simple decision tree. First, we need to encode
our target `#!python "y"` as we are still dealing with `#!python str` labels
(`#!python "yes"` or `#!python "no"`). For this purpose, we can use the
[`LabelEncoder`](../data/preprocessing.md#label-encoding).

```python
from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
encoder.fit(y_train)
y_train = encoder.transform(y_train)
y_test = encoder.transform(y_test)
```

Now, we fit the first model. We set the parameters `max_depth` and
`min_samples_leaf` to
[prune](../algorithms/supervised/tree-based/cart.md#to-fix) the tree.

```python
from sklearn.tree import DecisionTreeClassifier

tree = DecisionTreeClassifier(
    random_state=42, max_depth=15, min_samples_leaf=10
)
tree.fit(X_train, y_train)
score = tree.score(X_test, y_test)
print(f"Accuracy: {round(score, 2)}")
```

```title=">>> Output"
Accuracy: 0.89
```

89 % accuracy seems like a perfect start! But don't get too excited yet, we
overlooked a small yet crucial detail.

### Detour: Class imbalance

In classification, the accuracy is a good metric to evaluate the performance of
a model. However, it is not always the most appropriate one. Here's why:

```python
print(y.value_counts(normalize=True))
```

```title=">>> Output"
y
no     0.89002
yes    0.10998
```

The target variable `#!python "y"` is imbalanced. The class `#!python "no"`
occurs in 89% of the cases, while `#!python "yes"` accounts for roughly 11%.
This means that a model that constantly predicts `#!python "no"` for every
observation would achieve an accuracy of 89%.

Thus, our decision tree is not as good as it seems, and we need to consider
other metrics to evaluate its performance. For our task, we pick the balanced
accuracy score.

#### Confusion matrix

To understand the balanced accuracy score, we first need to understand the
confusion matrix. Let's calculate it and explain it step by step.

```python
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix

y_pred = tree.predict(X_test)
# calculate the matrix
conf_matrix = confusion_matrix(y_true=y_test, y_pred=y_pred)
# plot it
disp = ConfusionMatrixDisplay(
    confusion_matrix=conf_matrix, display_labels=["no", "yes"]
)
disp.plot()
plt.show()
```

<div style="text-align: center;">
    <img src="/assets/data-science/practical/confusion-matrix.svg" alt="Confusion matrix">
    <figcaption>Confusion matrix calculated using the test set.</figcaption>
</div>

???+ info

    The labels in red were added by the author and their creation is not part of
    the code block. They are simply used to facilitate the following explanation.

Put simply, the confusion matrix compares the actual values with the predicted
values (of our test set). The matrix is divided into four quadrants:

- **True Positives (TP)**: The model correctly predicted the positive class
    (yes - client subscribed to a term deposit). We have `#!python 20` true
    positive cases.
- **True Negatives (TN)**: The model correctly predicted the negative class (no
    \- client did not subscribe to a term deposit). In our instance,
    `#!python 683` true negative cases.

With the first diagonal covered, we move on to the instances that were
incorrectly predicted:

- **False Positives (FP)**: The model predicted the positive class, but the
    actual class was negative. `#!python 16` to be specific.
- **False Negatives (FN)**: The model predicted the negative class, but the
    actual class was positive. `#!python 67` to be exact.

???+ tip

    A perfect model would have 0 false positives and 0 false negatives. Hence, we
    want to minimize the false positives and false negatives.

    Generally, the confusion matrix is a great tool to understand the performance
    of a model. It is especially useful when dealing with imbalanced classes.

Regarding our first model, we can simply conclude that there is still a lot of
room for improvement. With an understanding of the confusion matrix, we can
extend our knowledge to the balanced accuracy score.

#### Balanced accuracy

The balanced accuracy score is defined as:

???+ defi "Balanced accuracy score"

    \[
    \text{Balanced accuracy} = \frac{1}{2} \left( \frac{TP}{TP + FN} + \frac{TN}{TN + FP} \right)
    \]

> In the binary case, balanced accuracy is equal to the arithmetic mean of
> sensitivity (true positive rate) and specificity (true negative rate)
>
> [`scikit-learn`: Balanced accuracy score](https://scikit-learn.org/stable/modules/model_evaluation.html#balanced-accuracy-score)

The balanced accuracy score ranges from 0 to 1. A score of 1 indicates a
perfect model.

???+ question "Manual calculation"

    Calculate the balanced accuracy score for the decision tree model.

    Use the results from the above confusion matrix and the formula for the
    balanced accuracy score. You can perform the calculation on a piece of paper or
    use simple arithmetic in Python.

Let's compare your result with the one calculated by `scikit-learn`.

```python
from sklearn.metrics import balanced_accuracy_score

balanced_accuracy = balanced_accuracy_score(y_test, y_pred)
print(f"Balanced accuracy: {round(balanced_accuracy, 4)}")
```

```title=">>> Output"
Balanced accuracy: 0.6035
```

Hopefully, your result matches the one calculated by `scikit-learn`.

Compared to the accuracy of 89%, the balanced accuracy score of 60% gives a
more realistic view of the model's performance. In turn, this means we have to
improve our model.

???+ tip

    If you want to know more about different metrics and scoring, check out this
    excellent guide. It not only covers classification metrics, but also multiple
    ways to score regression models (apart from the \(R^2\)).

    [`scikit-learn`: Metrics and scoring: quantifying the quality of predictions](https://scikit-learn.org/stable/modules/model_evaluation.html)

## Detour: Reproducibility

Since, we are already on detours, let's take another one. Up until now, we have
always set the `random_state` parameter (if available). As we have covered
multiple times, this ensures the reproducibility of our results. We set it when
splitting the data, when initializing a model, etc.

But what happens if you forget to set the `random_state` parameter? To
demonstrate the outcome, we generate a data set. In a loop we split the data,
train a tree and calculate the balanced accuracy score. We repeat this process
10 times:

```python linenums="1" hl_lines="7 17 20"
from sklearn.datasets import make_classification

X_synthetic, y_synthetic = make_classification(
    n_samples=1000,
    n_features=20,
    n_classes=2,
    random_state=None,
)

for i in range(10):
    (
        X_train_synthetic,
        X_test_synthetic,
        y_train_synthetic,
        y_test_synthetic,
    ) = train_test_split(
        X_synthetic, y_synthetic, test_size=0.2, random_state=None
    )
    tree = DecisionTreeClassifier(
        random_state=None, max_depth=15, min_samples_leaf=10
    )
    tree.fit(X_train_synthetic, y_train_synthetic)
    y_pred = tree.predict(X_test_synthetic)
    score = balanced_accuracy_score(y_test_synthetic, y_pred)
    print(f"Iteration {i + 1}: {round(score, 4)}")
```

Here are my results, yours look drastically different:

```title=">>> Output"
Iteration 1: 0.8853
Iteration 2: 0.9457
Iteration 3: 0.8997
Iteration 4: 0.8947
Iteration 5: 0.9407
Iteration 6: 0.9097
Iteration 7: 0.9004
Iteration 8: 0.9451
Iteration 9: 0.919
Iteration 10: 0.8886
```

As you can see the model's performance varies greatly!

???+ danger

    The code block illustrates the importance of the `random_state` parameter.
    Without it, you won't be able to reproduce your own results and others won't be
    able to reproduce your results either.

    Specifically, in a science setting and real-world applications, reproducibility
    is crucial to validate findings and conclusions. So ensure reproducibility!

## More modelling

Let's get back on track and try out more models. We will compare their
performance with the balanced accuracy score.

### Random forest

Naturally, since we started with a CART (decision tree), we try a random
forest.

```python
from sklearn.ensemble import RandomForestClassifier

forest = RandomForestClassifier(
    n_estimators=100,
    max_depth=15,
    min_samples_leaf=10,
    random_state=42,  # (1)!
)
forest.fit(X_train, y_train)

y_pred = forest.predict(X_test)
score_forest = balanced_accuracy_score(y_test, y_pred)

print(f"Forest balanced accuracy: {round(score_forest, 4)}")
```

1. We adopt the values for `max_depth` and `min_samples_leaf` from the decision
    tree.

```title=">>> Output"
Forest balanced accuracy: 0.5927
```

Compared to the decision tree (balanced accuracy of 60.35%), the random forest
has a balanced accuracy of 59.27%. Somehow, the performance got even worse!

#### `class_weight` parameter

We can try to improve the performance by setting the `class_weight` parameter
to `#!python balanced`. This takes the class imbalance into consideration.

```python hl_lines="6"
forest = RandomForestClassifier(
    n_estimators=100,
    max_depth=15,
    min_samples_leaf=10,
    random_state=42,
    class_weight="balanced",
)
forest.fit(X_train, y_train)

y_pred = forest.predict(X_test)
balanced_forest = balanced_accuracy_score(y_test, y_pred)

print(f"Forest balanced accuracy: {round(balanced_forest, 4)}")
```

```title=">>> Output"
Forest balanced accuracy: 0.7337
```

Now we were able to improve the performance significantly, namely to 73.37%.

### Logistic regression

???+ question "Logistic regression"

    What about a logistic regression model? How does it perform?

    1. Initialize and fit a `LogisticRegression` model with
        `#!python   class_weight="balanced"`. Don't forget to set the
        `random_state`.
    1. Calculate the balanced accuracy score for the test set.
    1. Compare the results to the decision tree and random forest.

??? info

    Depending on the parameter settings, the logistic regression model achieves
    similar performance to the random forest.

As you can see, with a preprocessed data set, we can now easily compare
different models.

These are our results so far:

- Decision tree: 60.35%
- Random forest: 73.37%
- Logistic regression: ? (your result)

## Hyperparameter tuning

So far, we've used arbitrary values for our model parameters
(`#!python max_depth=15, min_samples_leaf=10`, etc.). However, these might not
be optimal for our specific problem. Therefore, we apply hyperparameter tuning.
Hyperparameter tuning is the process of finding the best combination of model
parameters to maximize performance.

For starters, we will perform a manual hyperparameter tuning for the maximum
depth (`max_depth`) parameter. We will test the values
`#!python [5, 10, 15, 20, 25]`.

```python hl_lines="1 6"
max_depth = [5, 10, 15, 20, 25]

for n in max_depth:
    forest = RandomForestClassifier(
        n_estimators=100,
        max_depth=n,
        min_samples_leaf=10,
        random_state=42,
        class_weight="balanced",
    )
    forest.fit(X_train, y_train)
    y_pred = forest.predict(X_test)
    score = balanced_accuracy_score(y_test, y_pred)
    print(f"max_depth={n}: {round(score, 4)}")
```

```title=">>> Output"
max_depth=5: 0.7352
max_depth=10: 0.7445
max_depth=15: 0.7337
max_depth=20: 0.733
max_depth=25: 0.733
```

The best performance is achieved with a `max_depth` of `#!python 10`. So the
initial value of `#!python 15` was not optimal. Next, we could try to optimize
the number of trees (`n_estimators`), the minimum number of samples required to
be at a leaf node (`min_samples_leaf`), etc. You get the point ...

???+ tip

    However, this manual tuning is time-consuming and not always feasible. In the
    last (advanced) chapter of this course, we will introduce you to automated
    hyperparameter tuning.

???+ info

    You can spend hours tuning hyperparameters. So, don't get lost in the
    hyperparameter tuning process.

    :warning: *Spoiler alert* :warning:: With this specific data set and
    hyperparameter tuning, you won't significantly surpass the results we have
    achieved so far.

## The result

We conclude that a

______________________________________________________________________

```python
RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    min_samples_leaf=10,
    random_state=42,
    class_weight="balanced",
)
```

is the best model we have found for our task. It achieves a balanced accuracy
of 74.45%.

______________________________________________________________________

<div style="text-align: center;">
    <h4>Here is the main takeaway:</h4>
</div>

???+ tip

    Unfortunately, with real world data sets you won't always achieve astounding
    results. But that's okay! :blush:

    If the performance does not meet your expectations, you can try following
    things:

    - Feature engineering: Create new features or modify existing ones.
    - Preprocessing: Try different preprocessing steps.
    - Model selection: Try different models.

    But sometimes, it is also a possibility that the features can't describe the
    target variable well enough or you simply need more data.

## Recap

We tried different models and evaluated their performance using the balanced
accuracy score. Ultimately, we concluded that a random forest model performed
best.

Along the way, we introduced class imbalance, confusion matrix, balanced
accuracy and hyperparameter tuning. Another example illustrated the importance
of reproducibility.

Next, we distill our findings in an end-to-end example and save the final model
to disk.
