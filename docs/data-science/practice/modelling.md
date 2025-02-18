## Introduction

In this chapter, we start our modelling efforts. Let's dive right in.

Create a new notebook or script. Your project should now look like this:

```plaintext hl_lines="6"
📁 bank_model/
├── 📁 .venv/
├── 📁 data/
├───── 📄 bank-merged.csv
├── 📄 preparation.ipynb
├── 📄 modelling.ipynb
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

    By default `train_test_split` shuffles the data before splitting which
    is a good practice. It helps to avoid any bias that might be present in the
    order of the data.

    However, if you are ever working with data that is dependent on the order
    (time series data), you should not shuffle the data. In that case, set 
    `#!python shuffle=False`.

Now apply the preprocessing steps (from the previous chapter) to the training 
and test sets:

```python
# impute missing values
impute.fit(X_train)
X_train = impute.transform(X_train)
X_test = impute.transform(X_test)

# convert back to DataFrame
X_train = pd.DataFrame(X_train, columns=X.columns)  # (1)!
X_test = pd.DataFrame(X_test, columns=X.columns)

# apply preprocessing (OneHotEncoder, KBinsDiscretizer & StandardScaler)
preprocessor.fit(X_train)
X_train = preprocessor.transform(X_train)
X_test = preprocessor.transform(X_test)
```

1. Since, `preprocessor` requires the column names of our data, we need to 
   convert the array back to a `DataFrame`. Else the `preprocessor` will not
   work!

> The general rule is to never call `fit` on the test data.
> 
> [`scikit-learn`: Common pitfalls and recommended practices](https://scikit-learn.org/stable/common_pitfalls.html#data-leakage)


???+ info

    For example, when `impute.fit(X_train)` is called, the `SimpleImputer`
    calculates the mode solely from the training data - `X_train`. When
    `impute.transform(X_test)` is called, the `SimpleImputer` uses the mode
    calculated from `X_train` to fill in missing values in `X_test`. So we 
    never use the test set to calculate the mode.
    
    The same applies to the `preprocessor` and thus we can prevent information
    leakage.

## Train a model

For starters, we will train a simple decision tree. First, we need to encode
our target `#!python "y"` as we are still dealing with `#!python str` 
labels (`#!python "yes"` or `#!python "no"`). For this purpose, we can use
the [`LabelEncoder`](../data/preprocessing.md#label-encoding).

```python
from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
y_train = encoder.fit_transform(y_train)
y_test = encoder.transform(y_test)
```

Now, we fit the first model. We set the parameters `max_depth` and 
`min_samples_leaf` to prune the tree.

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

The accuracy is a good metric to evaluate the performance of a model. However,
in classification it is not always the best metric. Here's why:

```python
print(y.value_counts(normalize=True))
```

```title=">>> Output"
y
no     0.89002
yes    0.10998
```

The target variable `#!python "y"` is imbalanced. The class `#!python "no"`
occurs in nearly 90% of the cases. This means that a model that constantly 
predicts `#!python "no"` for every observation would achieve an accuracy of 
90%.

Thus, our model is not as good as it seems, and we need to consider other 
metrics to evaluate its performance. For our task, we pick the balanced 
accuracy score.

#### Confusion matrix

To understand the balanced accuracy score, we first need to understand the
confusion matrix. Let's calculate it and explain it step by step.

```python
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

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

    The labels in red were added by the author and their creation is not 
    part of the code block. They are simply used to facilitate the explanation.

Put simply, the confusion matrix compares the actual values with the predicted
values (of our test set). The matrix is divided into four quadrants:

- **True Positives (TP)**: The model correctly predicted the positive class 
  (yes - client subscribed to a term deposit). We have `#!python 20` true 
  positive cases.
- **True Negatives (TN)**: The model correctly predicted the negative class 
  (no - client did not subscribe to a term deposit). In our instance, 
  `#!python 683` true negative cases.

With the first diagonal covered, we move on to the instances that were 
incorrectly predicted:

- **False Positives (FP)**: The model predicted the positive class, but the 
  actual class was negative. `#!python 16` to be specific.
- **False Negatives (FN)**: The model predicted the negative class, but the 
  actual class was positive. `#!python 67` to be exact.

???+ tip

    A perfect model would have 0 false positives and 0 false negatives.
    Hence, we want to minimize the false positives and false negatives.

    Generally, the confusion matrix is a great tool to understand the
    performance of a model. It is especially useful when dealing with
    imbalanced classes.

Regarding our first model, we can simply conclude that there is still a lot of
room for improvement. With an understanding of the confusion matrix, we can
extend our knowledge to the balanced accuracy score.
