import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import (
    RandomForestClassifier,
)
from sklearn.feature_selection import VarianceThreshold
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import (
    KBinsDiscretizer,
    OneHotEncoder,
    StandardScaler,
)
from sklearn.svm import SVC


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

pipe = Pipeline(
    [
        ("imputer", DataFrameImputer()),
        ("preprocessor", preprocessor),
        ("variance", VarianceThreshold(threshold=0.0)),
        ("classifier", None),
    ]
)


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

search = GridSearchCV(
    pipe,
    grid,
    n_jobs=-1,
    cv=StratifiedKFold(n_splits=5, shuffle=True, random_state=654),
    scoring=["balanced_accuracy", "roc_auc"],
    refit="balanced_accuracy",
    verbose=2,
)


# load data
data = pd.read_csv("data/bank-merged.csv")
X, y = data.drop(columns="y"), data["y"]

# fit the grid search
search.fit(X, y)

print(
    f"Best score: {search.best_score_}\n"
    f"Best estimator: {search.best_params_}"
)
