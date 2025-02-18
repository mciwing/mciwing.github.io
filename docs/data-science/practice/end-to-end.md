## Introduction

We distill all relevant code blocks from the previous two chapters into
one cohesive notebook. This notebook will be an end-to-end example on fitting
a machine learning model on the bank marketing data set. Lastly, we will
save the model to disk.

???+ tip

    The notebook we will create, can serve as a reference point for your 
    further data science projects.

So start by creating yet another notebook.

```plaintext hl_lines="7"
📁 bank_model/
├── 📁 .venv/
├── 📁 data/
├───── 📄 bank-merged.csv
├── 📄 preparation.ipynb
├── 📄 modelling.ipynb
├── 📄 end-to-end.ipynb
```

## Previously...

In the previous chapters, we:

1. Loaded the data
2. Defined techniques to impute (`SimpleImputer`) and preprocess the data
   (`ColumnTransformer`)
3. Fit and transformed the data
4. Split the data into train and test sets
5. Evaluated different model types and concluded that a 
   `RandomForestClassifier` is the best model (we found) for this task
6. Fit and evaluated the random forest

Here are the bullet points distilled in one code block:

```python linenums="1"
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import balanced_accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import (
    KBinsDiscretizer,
    LabelEncoder,
    OneHotEncoder,
    StandardScaler,
)

data = pd.read_csv("data/bank-merged.csv")
data = data.replace("unknown", None)

impute = SimpleImputer(strategy="most_frequent", missing_values=None)

preprocessor = ColumnTransformer(
    transformers=[
        ("nominal", OneHotEncoder(),
         ["default", "housing", "loan", "contact", "poutcome", "job", "marital"]),

        ("ordinal", OneHotEncoder(),
         ["month", "day_of_week", "education"]),

        ("binning", KBinsDiscretizer(n_bins=5, strategy="uniform", encode="onehot"),
         ["age", "campaign", "pdays", "previous"]),

        ("zscore", StandardScaler(),
         ["emp.var.rate", "cons.price.idx", "cons.conf.idx", "euribor3m", "nr.employed"]),
    ]
)

# remove the target from data and assign it to y
y = data.pop("y")
X = data

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

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

# encode target
encoder = LabelEncoder()
y_train = encoder.fit_transform(y_train)
y_test = encoder.transform(y_test)

# fit on train set
forest = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    min_samples_leaf=10,
    random_state=42,
    class_weight="balanced"
)
forest.fit(X_train, y_train)

# evaluate on test set
y_pred = forest.predict(X_test)
score = balanced_accuracy_score(y_test, y_pred)
print(f"Balanced accuracy: {round(score, 4)}")
```

```title=">>> Output"
Balanced accuracy: 0.7445
```

???+ question "Copy and execute the block"

    Since the code block is nothing new, simply copy and execute it.
    If everything went smoothly, you should see the balanced accuracy score 
    printed.

## Re-fit on whole data set

Previously, we split our data into train and test sets. Using the test set 
we were able to estimate the performance of our model. That's the whole 
purpose of the test set.

Now, our goal is to save the model for future use. Therefore, in practice, we 
want to leverage the power of the whole data set. Thus, we re-fit the model on 
the whole data set to make use of all available data.

```python
# preprocess the whole data set
X = impute.transform(X)
X = pd.DataFrame(X, columns=data.columns)
X = preprocessor.transform(X)

# encode target
y = encoder.transform(y)
```

To preprocess the whole data set, we can reuse the `impute` and `preprocessor`
objects. We only need to transform the data and encode the target. Lastly,
we fit the model on the whole data set. It's as simple as:

```python
forest.fit(X, y)
```

???+ info

    Note, we can simply call `fit()` again, this will "overwrite" the previous 
    model and use the whole data set to fit the model.

`forest` is now fitted on the whole data set. That's it! We have our final 
model which we will save to disk. :party_popper: