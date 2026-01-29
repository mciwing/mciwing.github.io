# Random Forest

While decision trees are easy to interpret, they have several drawbacks: they
are prone to overfitting and are sensitive to slight changes in the data.

Random forest is an ensemble method that addresses these drawbacks at the cost
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
case of classification, the majority vote is taken. The majority vote in a 
random forest classification means that the class predicted most frequently by
the individual trees is selected as the final prediction.

No matter the task, classification or regression: it was observed that 
introducing randomness in the tree-growing process improves the model 
performance.

???+ info

    Contrary to the classic CART, random forests do not constrain the tree 
    growth. I.e., trees are fully grown and not pruned.

## Examples

With a basic understanding of random forests we take a look at some 
examples. As always, we'll use our favorite machine learning package 
`scikit-learn` (at least that of the author :wink:).

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
    \(R^2\). The same applies to random forests regressors.

Compared to a single tree with an \(R^2\) of 0.61, the random forest performs
considerably better with an \(R^2\) of 0.81. You can re-visit the according 
section [here](cart.md#fit-and-evaluate-the-model).

???+ question "How many trees are in the forest?"
    
    Consult the `scikit-learn` docs to find out how many trees are in the 
    forest by default. Use the following question for self-assessment.

<quiz>
How many trees form a forest by default?
- [ ] None, you have to pass it as argument.
- [ ] 1000
- [ ] 1, the forest defaults to a single decision tree.
- [x] 100

The parameter `n_estimators` defaults to 100 trees.
</quiz>

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
    that work well. In later chapters, we will explore methods to 
    automatically tune these hyperparameters.

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

In most cases, you won't need to inspect the individual trees. Nevertheless,
we can utilize this information to solidify our understanding of random 
forests.

---

### Stronger together

We fit a random forest classifier on a synthetic data set to 
==literally== illustrate the different trees. First, we generate the data.

```python
from sklearn.datasets import make_classification

X, y = make_classification(
    random_state=42,
    n_clusters_per_class=1
)
```

Next, we initialize and fit a random forest classifier.

```python
classifier = RandomForestClassifier(
    random_state=42, n_estimators=4, max_depth=3
)
classifier.fit(X, y)
```

Note, that we set the number of trees to `#!python 4`. We keep the number 
small as we visualize them later on. The `max_depth` parameter limits the 
depth of each tree to `#!python 3`. This is done to perform pruning and thus 
keep the trees simple and easier to plot.

Finally, we visualize all trees. We access the trees via the `estimators_`
attribute and plot them using the familiar `plot_tree()` function. Everything 
else is just plot customization.

```python hl_lines="5 7"
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

fig = plt.figure(figsize=(20, 12))
for index, tree in enumerate(classifier.estimators_, 1):
    plt.subplot(2, 2, index)
    plot_tree(
        tree,
        label="root",
        class_names=True,
        filled=True,
        fontsize=14,
    )
    plt.title(f"Decision Tree {index}", fontsize=25)

plt.tight_layout()
plt.show()
```

<figure markdown="span">
    ![Individual trees visualized](../../../../assets/data-science/algorithms/tree-based/individual-trees.png)
    <figcaption>All four individual trees of this particular forest.
    </figcaption>
</figure>

Although there is a lot of information cramped inside one figure, at first 
glance it is obvious that all four trees are different. Each of them differs
in splits (feature and threshold), number of nodes and predictions.

Each one of these trees on their own might not generalize well, hence they are
often referred to as weak learners. However, when combined, they form a 
"strong" model. That's the essence of an ensemble method!

### Feature importance

One of the most powerful attribute of random forests is their ability to 
assess feature importance: measuring how much each input variable contributes 
to predicting the target variable.

Remember that trees are fitted on a [bootstrap](forest.md#bootstrap-sampling) 
training set. Since some samples are left out during this process, we can use 
these to measure the importance of each feature. These unused observations are 
called "out-of-bag" (OOB) samples. For each feature, the OOB samples are 
randomly permuted (shuffled) and the increase in prediction error is measured. 
Features that lead to larger increases in error when permuted are considered 
more important.

Let's examine feature importance using the breast cancer dataset:

```python hl_lines="6"
X, y = load_breast_cancer(return_X_y=True, as_frame=True)

rf = RandomForestClassifier(random_state=42)
rf.fit(X, y)

print(rf.feature_importances_)
```

```title=">>> Output"
[0.03484323 0.01522515 0.06799034 0.06046164 0.00795845 0.01159704
 ...]
```

???+ info

    To keep the example concise, we did not perform a train test split.

Feature importance values are a `#!python list` of `#!python float`s. 
Each value corresponds to a feature in the order they were passed to the
model. The values are normalized and sum to `#!python 1.0`. 
A higher value indicates that the feature contributes more to making correct 
predictions.

Feature importance can help with:

1. Feature selection: Identifying which features are most relevant for
   predictions
2. Model interpretation: Understanding which features drive the model's
   decisions
3. Data collection: Guiding future data collection efforts by highlighting
   important measurements

???+ question "Visualize the feature importance"

    Generate a bar plot to visualize the feature importance.
    Use any package of your choice. For convenience, you can use the 
    following code snippet to get started.
    
    ```python
    import pandas as pd

    feature_importance = pd.DataFrame(
        {"feature": X.columns, "importance": rf.feature_importances_}
    )
    ```

    Don't worry about styling the plot!

A possible solution is provided below.

<div style="text-align: center;">
    <iframe src="/assets/data-science/algorithms/feature-importance.html" 
        width="100%" 
        height="650px">
    </iframe>
</div>

## Recap

Random forests improve upon single decision trees by combining multiple trees
into an ensemble model. Through bootstrap sampling and random feature
selection, they address the main drawbacks of decision trees - overfitting and
sensitivity to data changes. While slightly less interpretable than single
trees, random forests provide better generalization, more robust predictions,
and useful insights through feature importance measures.

With `scikit-learn`, you are now able to build a random forest for regression 
and classification tasks. You have also learned how to inspect individual trees
and assess feature importance.
