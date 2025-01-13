# Classification

## Logistic Regression

While linear regression helps us predict continuous values, many real-world
problems require predicting categorical outcomes: Will a customer churn? Is an
email spam? Is a tumor malignant? Logistic regression addresses these binary
classification problems by extending the concepts we learned in linear
regression to predict probabilities between 0 and 1.

### Theory

???+ info

    The theoretical part is adapted from:

    ^^Daniel Jurafsky and James H. Martin. 2025. Speech and Language 
    Processing: *An Introduction to Natural Language Processing, Computational 
    Linguistics, and Speech Recognition with Language Models*[^1]^^

    [^1]:
        3rd edition. Online manuscript released January 12, 2025.
        [https://web.stanford.edu/~jurafsky/slp3](https://web.stanford.edu/~jurafsky/slp3)

### Deja vu: Linear regression

Just like in linear regression, we have a set of features \(x_1, x_2, ..., x_n\)
describing an outcome \(y\). But instead of predicting a continuous value, \(y\)
is binary: 0 or 1.

Similar to linear regression, logistic regression uses a linear combination of
the features to predict the outcome. I.e., each feature is assigned a 
**weight**, and a **bias term** is added at the end.

???+ defi "Linear combination"

    \[
    z = b_1 \cdot x_1 + b_2 \cdot x_2 + ... + b_n \cdot x_n + a
    \]

with \(a\) being the bias term and \(b_1, b_2, ..., b_n\) the weights. 
"The resulting single number \(z\) expresses the weighted sum
of the evidence for the class." (Jurafsky & Martin, 2025 p. 79)
Bias, weights and the intercept are all real numbers.

So far, logistic regression is the same as linear regression with the sole 
difference that in [linear regression](regression.md#linear-regression) we 
referred to the bias \(a\) as the intercept, and the 
weights \(b_1, b_2, ..., b_n\) as coefficients or slope.

However, \(z\) is not the final prediction, since it can take real values 
and in fact ranges from \(-\infty\) to \(+\infty\). Thus, \(z\) needs to be 
transformed to a probability between 0 and 1. This is where the sigmoid
function comes into play.

### The sigmoid function

Unlike linear regression, which outputs unbounded values, logistic regression
uses the sigmoid (or logistic) function to transform \(z\) into a probability

???+ defi "Sigmoid function"

    \[
    \sigma(z) = \frac{1}{1 + e^{-z}}
    \]

    The sigmoid function takes the real number \(z\) and squashes it to the 
    range (0,1).
