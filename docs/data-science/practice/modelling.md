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
    calculated from `X_train` to fill in missing values in `X_test`.
    
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
it is not always the best metric. Here's why:
