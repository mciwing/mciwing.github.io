## Introduction

This bonus chapter demonstrates the usage of a pipeline in conjunction with a
grid search to automate the modelling process. Again, we are utilizing the bank
marketing data. However, this time around we streamline the following:

- Data preprocessing
- Model evaluation
- Hyperparameter tuning
- Model selection
- Re-training the model on the entire dataset

... basically every step we had taken in "Data Science in Practice" block.
Moreover, with a pipeline and grid search, we can easily evaluate additional
model types and apply a more sophisticated way to evaluate their performance.

???+ tip

    This chapter serves as an additional outlook for further topics you could
    explore, targeting your curiosity. Some concepts and techniques used in this
    chapter were not covered in this course. We won't explain them in much detail
    here, as they are beyond the scope of this course. Nonetheless, they could
    prove valuable for your future machine learning journey.

If you're still around, great! Let's get started with some code. :rocket:

______________________________________________________________________

## Quickstart

If you just need a blueprint for your next project, here's the whole thing.

??? code

    ```python linenums="1"
    {% include "../../assets/data-science/practical/bonus.py" %}
    ```

1. Open the `bank_model` project (from the Data Science in Practice block).
1. Copy and execute the code.
1. Done!

If you want to know more about the individual parts, keep reading.

______________________________________________________________________

## Plan of attack

We start by defining a bunch of things:

1. Custom transformer, for data imputation and returning a `DataFrame`
1. `ColumnTransformer` for preprocessing the data
1. Pipeline to combine all steps
1. Grid defining all models and parameters to be evaluated
1. Grid search to find the best model

Then we simply need to apply the pipeline and grid search to the data. Finally,
we save the best model.

## Implementation

### 1. Custom transformer

We start by defining a custom transformer that imputes missing values in a
`DataFrame`.

```python
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.impute import SimpleImputer


class DataFrameImputer(BaseEstimator, TransformerMixin):
    def __init__(self, strategy="most_frequent"):
        self.strategy = strategy
        self.imputer = SimpleImputer(
            strategy=strategy, missing_values="unknown"
        )

    def fit(self, X, y=None):
        self.imputer.fit(X)
        return self

    def transform(self, X):
        return pd.DataFrame(
            self.imputer.transform(X), columns=X.columns, index=X.index
        )
```

The custom transformer has implement the `fit()` and `transform()` methods.
Since we are not passing the target variable `y` to the `fit` method, we
"ignore" it by defining it as `#!python y=None`.

If you want to know more about custom transformers or even custom estimators
(models), check out these resources:

- Custom transformer from a function
    [:octicons-link-external-16:](https://scikit-learn.org/stable/modules/preprocessing.html#custom-transformers)
- `TransformerMixin`
    [:octicons-link-external-16:](https://scikit-learn.org/stable/modules/generated/sklearn.base.TransformerMixin.html)
- Custom estimator
    [:octicons-link-external-16:](https://scikit-learn.org/stable/developers/develop.html#rolling-your-own-estimator)

???+ tip

    `DataFrameImputer` returns a `pandas` `DataFrame` which allows us to easily
    chain the imputation step together with our trusted `ColumnTransformer` within
    a pipeline. In this case, that's the whole purpose of the custom transformer.

### 2. `ColumnTransformer`

Speaking of the `ColumnTransformer`, it simply stays the same as before.

```python
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import (
    KBinsDiscretizer,
    OneHotEncoder,
    StandardScaler,
)

preprocessor = ColumnTransformer(
    transformers=[
        (
            "nominal",
            OneHotEncoder(handle_unknown="ignore"),
            [
                "default",
                "housing",
                "loan",
                "contact",
                "poutcome",
                "job",
                "marital",
            ],
        ),
        (
            "ordinal",
            OneHotEncoder(handle_unknown="ignore"),
            ["month", "day_of_week", "education"],
        ),
        (
            "binning",
            KBinsDiscretizer(n_bins=5, strategy="uniform", encode="onehot"),
            ["age", "campaign", "pdays", "previous"],
        ),
        (
            "zscore",
            StandardScaler(),
            [
                "emp.var.rate",
                "cons.price.idx",
                "cons.conf.idx",
                "euribor3m",
                "nr.employed",
            ],
        ),
    ]
)
```

### 3. Pipeline

A pipeline is a sequence of steps where each step is a tuple containing a name
and a transformer/estimator.

```python
from sklearn.feature_selection import VarianceThreshold
from sklearn.pipeline import Pipeline

pipe = Pipeline(
    [
        ("imputer", DataFrameImputer()),
        ("preprocessor", preprocessor),
        ("variance", VarianceThreshold(threshold=0.0)),
        ("classifier", None),
    ]
)
```

Our pipeline consists of the following sequential steps:

1. `#!python "imputer"` - Impute missing values
1. `#!python "preprocessor"` - Apply all further preprocessing steps
1. `#!python "variance"` - Remove features with zero variance (removes all
    constant features)
1. `#!python "classifier"` - Apply a classifier (to be defined later)

???+ tip

    You can modify pipelines to your liking. For example you could add another
    feature selection step. Or what about applying a PCA and then a classifier? The
    possibilities are endless!

### 4. Grid

Next, we define a grid with all models and hyperparameters to be evaluated.

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC

grid = [
    {
        "classifier": [
            RandomForestClassifier(random_state=42, class_weight="balanced")
        ],
        "classifier__n_estimators": [100, 200],
        "classifier__max_depth": [5, 10],
        "classifier__min_samples_leaf": [1, 2],
    },
    {
        "classifier": [SVC(random_state=42, class_weight="balanced")],
        "classifier__C": [0.1, 1, 10],
    },
    {"classifier": [LogisticRegression(class_weight="balanced")]},
    {
        "classifier": [MLPClassifier(random_state=42, max_iter=1_000)],
    },
]
```

The grid contains four different models:

1. Random Forest
1. Support Vector Machine (not discussed in this course)
1. Logistic Regression
1. Multi-layer Perceptron (Neural Network - not discussed in this course)

We will evaluate all these models and each hyperparameter combination.

???+ info

    Names in the grid dictionary must match the names in the pipeline
    (`#!python "classifier"`). The double underscore `#!python "__"` is used to
    indicate that the parameter belongs to the classifier in the pipeline.

### 5. Grid search

Finally, we define the grid search, that's where we put everything together.

```python
from sklearn.model_selection import GridSearchCV, StratifiedKFold

search = GridSearchCV(
    pipe,
    grid,
    n_jobs=-1,  # (1)!
    cv=StratifiedKFold(n_splits=5, shuffle=True, random_state=654),  # (2)!
    scoring=["balanced_accuracy", "roc_auc"],
    refit="balanced_accuracy",
    verbose=2,
)
```

1. Use all available CPU cores (`#!python n_jobs=-1`). This speeds up the
    process significantly.
1. We use a stratified k-fold cross-validation with 5 splits. Each fold
    preserves the percentage of samples for each class.

Basically, we are evaluating all models and hyperparameters using a
(stratified) k-fold cross-validation (read more about cross-validation
[here](https://scikit-learn.org/stable/modules/cross_validation.html#k-fold)).
The `StratifiedKFold` thus replaces our simple `train_test_split()`.

To evaluate the models, we are calculating two performance metrics: balanced
accuracy and ROC AUC (`#!python scoring=["balanced_accuracy", "roc_auc"]`). The
best model is selected based on the balanced accuracy
(`#!python  refit="balanced_accuracy"`) and then ==retrained on the entire
dataset==!

???+ info

    The grid search eliminates the need to compare models manually, it performs
    hyperparameter tuning, and it selects the best model for us. Lastly, we won't
    even have to re-train it on the entire dataset, as the grid search already does
    that for us! :exploding_head:

## Application

With all things defined, we simply need to apply the grid search to the data.

```python
# load data
data = pd.read_csv("data/bank-merged.csv")
X, y = data.drop(columns="y"), data["y"]

# fit the grid search
search.fit(X, y)

print(
    f"Best score: {search.best_score_}\n"
    f"Best estimator: {search.best_params_}"
)
```

```title=">>> Output"
Best score: 0.7407486855434444
Best estimator: {
    'classifier': RandomForestClassifier(class_weight='balanced', random_state=42),
    'classifier__max_depth': 5, 'classifier__min_samples_leaf': 1, 'classifier__n_estimators': 200
}
```

Again, a random forest is the best model.

To predict new data, use following method:

```python
search.best_estimator_.predict()
```

That's it! You've automated the whole modelling process. :tada:

______________________________________________________________________

<div style="text-align: center">

<h2>
    If you can surpass the performance of this pipeline's estimator, 
    please let us know. We are curious to hear from you! 😊
</h2>

</div>

______________________________________________________________________
