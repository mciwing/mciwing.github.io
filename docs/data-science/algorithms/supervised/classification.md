# Classification

## Logistic Regression

While linear regression helps us predict continuous values, other real-world
problems require predicting categorical outcomes: Will a customer subscribe to
a term deposit? Is an email spam? Is a transaction fraudulent? Logistic
regression addresses these binary classification problems by extending the
concepts we learned in linear regression to predict probabilities between 0 and
1\.

We will cover the theory and apply logistic regression to the breast cancer
dataset to predict whether a tumor is malignant or benign.

### Theory

???+ info

    The theoretical part is adapted from:

    ^^Daniel Jurafsky and James H. Martin. 2025. Speech and Language Processing:
    *An Introduction to Natural Language Processing, Computational Linguistics, and
    Speech Recognition with Language Models*[^1]^^

    [^1]: 3rd edition. Online manuscript released January 12, 2025.
    [https://web.stanford.edu/~jurafsky/slp3](https://web.stanford.edu/~jurafsky/slp3)

#### Deja vu: Linear regression

Just like in linear regression, we have a set of features
\(x_1, x_2, ..., x_n\) describing an outcome \(y\). But instead of predicting a
continuous value, \(y\) is binary: 0 or 1.

Similar to linear regression, logistic regression uses a linear combination of
the features to predict the outcome. I.e., each feature is assigned a
**weight**, and a **bias term** is added at the end.

???+ defi "Linear combination"

    \[
    z = b_1 \cdot x_1 + b_2 \cdot x_2 + ... + b_n \cdot x_n + a
    \]

with \(a\) being the bias term and \(b_1, b_2, ..., b_n\) the weights. "The
resulting single number \(z\) expresses the weighted sum of the evidence for
the class." (Jurafsky & Martin, 2025 p. 79) Bias, weights and the intercept are
all real numbers.

So far, logistic regression is the same as linear regression with the sole
difference that in [linear regression](regression.md#linear-regression) we
referred to the bias \(a\) as the intercept, and the weights
\(b_1, b_2, ..., b_n\) as coefficients or slope.

However, \(z\) is not the final prediction, since it can take real values and
in fact ranges from \(-\infty\) to \(+\infty\). Thus, \(z\) needs to be
transformed to a probability between 0 and 1. This is where the sigmoid
function comes into play.

#### The sigmoid function

Unlike linear regression, which outputs unbounded values, logistic regression
uses the sigmoid (or logistic) function to transform \(z\) into a probability

???+ defi "Sigmoid function"

    \[
    \sigma(z) = \frac{1}{1 + e^{-z}}
    \]

    The sigmoid function takes the real number \(z\) and transforms it to the range
    (0,1).

<div style="text-align: center;">
    <iframe src="/assets/data-science/algorithms/classification/sigmoid.html" width="600" height="450">
    </iframe>
    <figcaption>
        An illustration of the sigmoid function often referred to as 
        logistic function. Thus, the name logistic regression.
    </figcaption>
</div>

For given input features \(x_1, x_2, ..., x_n\), we can calculate the linear
combination \(z\) and then apply the sigmoid function to get the probability of
the outcome. To compute the probability of the outcome being 1
:fontawesome-solid-arrow-right: \(P(y=1|x)\), for example if an email is spam,
we have to set a decision boundary.

???+ defi "Decision boundary"

    If \(\sigma(z) \gt 0.5\), we predict \(y=1\), otherwise \(y=0\).

For instance, if the probability of an email being spam is 0.7, we predict that
the email is spam \((0.7 \gt 0.5)\). With a probability of 0.4, we predict that
the email is *not* spam \((0.4 \le 0.5)\).

#### The optimization problem

But how do we find the best parameter combination (weights and bias) for our
logistic regression model? Unlike linear regression, which uses ordinary least
squares, logistic regression typically uses Maximum Likelihood Estimation
(MLE), i.e., the best parameters (weights and bias) that maximize the
likelihood of the observed data.

<div style="text-align: center;">
    <iframe src="https://giphy.com/embed/3ohs7KViF6rA4aan5u" width="480" height="355" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
    <figcaption>Lo and behold, even more math...</figcaption>
</div>

For optimization purposes we use the negative log-likelihood as our loss
function:

???+ defi "Negative log-likelihood"

    \[
    J(\theta) = -\frac{1}{m}\sum_{i=1}^m [y_i\log(\sigma(z_i)) + (1-y_i)\log(1-\sigma(z_i))]
    \]

    with:

    - \(m\) as the number of training examples
    - \(y_i\) being the the actual class (0 or 1)
    - \(\sigma(z_i)\) is the predicted probability using the sigmoid function
    - \(\theta\) represents all parameters (weights and bias)

???+ tip

    Intuitively speaking, the loss function penalizes the model for making wrong
    predictions. If the model predicts a probability of 0.9 for a spam email, and
    the email is actually spam (\(y=1\)), the loss is small. On the other hand, if
    the model predicts a probability of 0.1 for a spam email, and the email is spam
    (\(y=1\)), the loss will be high.

    The weights are gradually adjusted to minimize the loss. Think of it like
    turning knobs slowly until we get better predictions.

    Gradually adjusting these knobs to minimize the loss is referred to as gradient
    descent.

Conveniently, `scikit-learn` provides a logistic regression implementation that
takes care of the optimization for us. Finally, we look at a practical example
to see logistic regression in action.

## Example

Let's apply logistic regression to the breast cancer dataset, a classic binary
classification problem where we need to predict whether a tumor is *malignant
or benign* based on various features.

With class labels \(y\) being 0 (malignant) or 1 (benign), we can use logistic
regression to predict the probability of a tumor being benign. The features
were calculated from digitized images of a breast mass.

???+ info

    See the [UCI Machine Learning Repository](https://doi.org/10.24432/C5DW2B) for
    more information on the data set.[^2]

    [^2]: Wolberg, W., Mangasarian, O., Street, N., & Street, W. (1993). Breast
    Cancer Wisconsin (Diagnostic) [Dataset]. UCI Machine Learning Repository.
    [https://doi.org/10.24432/C5DW2B](https://doi.org/10.24432/C5DW2B).

### Load the data

Conveniently, `scikit-learn` provides a couple of data sets for both regression
and classification tasks. One of them is the breast cancer dataset.

```python hl_lines="3"
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True, as_frame=True)

# count the number of malignant and benign tumors
print(y.value_counts())
```

```title=">>> Output"
target
1    357
0    212
```

In total, the data contains 569 samples with 357 benign and 212 malignant
tumors.

???+ tip

    Just like in the previous chapter, the data is divided into `X`, containing the
    attributes and `y` holding the corresponding labels. Having attributes and
    labels separated, makes life a bit easier when training and testing the model.

???+ question "Number of features"

    Investigate the `DataFrame` `X` to answer the below quiz question.

<quiz>
How many features (attributes) does the breast cancer dataset have?
- [x] 30
- [ ] 29
- [ ] 32

`X.shape` reveals that we are dealing with 30 features.

</p>
</quiz>

### Split the data

Before training our model, we want to split our data into two parts. Just like
in the previous chapter, we perform a 80/20 split, i.e., we use 80% to train
the model and evaluate it on the remaining 20%.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, shuffle=True
)
```

???+ tip

    If you need a refresh on the parameters used in `train_test_split()` revisit,
    the [Split the data](regression.md#split-the-data) section from the previous
    chapter.

### Train the model

Now that we have our training data, we can train the logistic regression model.

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(random_state=42, max_iter=5_000)  # (1)!
model.fit(X_train, y_train)
```

1. The `random_state` parameter ensures reproducibility, while `max_iter`
    specifies the maximum number of iterations taken for the solver to
    converge (i.e., solving the optimization problem to find the best
    parameter combination).

`#!python model=LogisticRegression(...)` creates an instance of the logistic
regression model. Only after calling the `fit()` method, the `model` is
actually trained. Since we separated attributes and labels into `X_train` and
`y_train` respectively, we can directly call the method without any further
data handling.

#### Weights and bias

With a trained model at hand, we can look at the weights \((b_1, b_2, ...,
b_n)\) and bias \((a)\).

```python
print(f"Model weights: {model.coef_}")
```

```title=">>> Output"
Model weights: [[ 0.98208299  0.22519686 -0.36688444  0.0262268 ... ]]
```

The `coef_` attribute contains the weight for each feature.
[As discussed](#deja-vu-linear-regression), the weights are real numbers.

???+ warning "You might not have the exact same results"

    Your model weights might differ slightly from the ones shown above. This is
    completely normal and happens because:

    **Numerical precision**: The default optimization solver (`#!python "lbfgs"`)
    behind `LogisticRegression` encounters tiny hardware-specific variations. The
    underlying libraries handle floating-point arithmetic differently across
    hardware platforms. During the iterative optimization, these tiny rounding
    differences accumulate, causing the solver to converge to slightly different
    solutions.

    :fontawesome-solid-lightbulb: These small differences don't affect your model's
    predictions or accuracy.

Now, it's your turn to look at the bias.

???+ question "Model bias"

    1. Open the `scikit-learn` docs on the
        [`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)
        class.
    1. Find out how to access the bias term of the model.
    1. Simply print the bias term of the model.

    :fontawesome-solid-lightbulb: Remember, the bias is often referred to as
    intercept.

### Predictions

Since, the main purpose of a machine learning model is to make predictions, we
will do just that.

Predicting, is as simple as using the `predict()` method. We will use the
patient measurements of the test set - `X_test`.

```python
y_pred = model.predict(X_test)

# first 5 predictions
print(y_pred[:5])
```

```title=">>> Output"
[1 0 0 1 1]
```

Congratulations, you just build a machine learning model to predict breast
cancer. But how good is the model? To conclude the chapter, we will briefly
evaluate the model's performance.

### Evaluate the model

Surely, we could just manually compare the predictions (`y_pred`) with the
actual labels (`y_test`) and evaluate how often the model was correct. Or
instead, we can leverage another method called `score()`.

```python
score = model.score(X_test, y_test)
```

First, the `score()` method takes `X_test` and makes the corresponding
predictions and programmatically compares the predictions with the actual
labels `y_test`. `score()` returns the accuracy :fontawesome-solid-arrow-right:
the proportion of correctly classified instances.

```python
print(f"Model accuracy: {round(score, 4)}")
```

```title=">>> Output"
Model accuracy: 0.9561
```

In our case, the model correctly classified 95.61% of the test set. In other
words, in 95.61% of instances, the model was able to correctly predict if a
tumor is malignant or benign.

???+ tip

    As the test set (both attributes and labels) were never used to train the
    model, the accuracy is a good indicator of how well the model generalizes to
    unseen data.

## Recap

We covered logistic regression, a popular algorithm for binary classification.

Upon discussing the theory, we discovered similarities to linear regression in
regard to the linear combination of features. With the help of the sigmoid
function, we transformed the linear combination into probabilities between 0
and 1.

Subsequently, we trained a logistic regression model on the breast cancer data
to predict whether a tumor is malignant or benign. To evaluate the model we
split the data and finally calculated the accuracy.

???+ info

    In subsequent chapters we will explore more sophisticated ways to split data
    and evaluate models.

Next up, we will dive into algorithms, like decision trees and random forest,
that can handle both regression and classification problems.
