# Classification

## Logistic Regression

While linear regression helps us predict continuous values, many real-world
problems require predicting categorical outcomes: Will a customer subscribe to
a term deposit? Is an email spam? Is a transaction fraudulent? 
Logistic regression addresses these binary classification problems by extending
the concepts we learned in linear regression to predict probabilities between 
0 and 1.

### Theory

???+ info

    The theoretical part is adapted from:

    ^^Daniel Jurafsky and James H. Martin. 2025. Speech and Language 
    Processing: *An Introduction to Natural Language Processing, Computational 
    Linguistics, and Speech Recognition with Language Models*[^1]^^

    [^1]:
        3rd edition. Online manuscript released January 12, 2025.
        [https://web.stanford.edu/~jurafsky/slp3](https://web.stanford.edu/~jurafsky/slp3)

#### Deja vu: Linear regression

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

#### The sigmoid function

Unlike linear regression, which outputs unbounded values, logistic regression
uses the sigmoid (or logistic) function to transform \(z\) into a probability

???+ defi "Sigmoid function"

    \[
    \sigma(z) = \frac{1}{1 + e^{-z}}
    \]

    The sigmoid function takes the real number \(z\) and transforms it to the 
    range (0,1).

<div style="text-align: center;">
    <iframe src="/assets/data-science/algorithms/sigmoid.html" width="600" height="450">
    </iframe>
    <figcaption>
        An illustration of the sigmoid function often referred to as 
        logistic function. Thus, the name logistic regression.
    </figcaption>
</div>

For given input features \(x_1, x_2, ..., x_n\), we can calculate the 
linear combination \(z\) and then apply the sigmoid function to get the 
probability of the outcome.
To compute the probability of the outcome being 1 
:fontawesome-solid-arrow-right: \(P(y=1|x)\), for example 
if an email is spam, we have to set a decision boundary.

???+ defi "Decision boundary"

    If \(\sigma(z) \gt 0.5\), we predict \(y=1\), otherwise \(y=0\).

For instance, if the probability of an email being spam is 0.7, we predict
that the email is spam \((0.7 \gt 0.5)\). With a probability of 0.4, we 
predict that the email is *not* spam \((0.4 \le 0.5)\).

#### The optimization problem

But how do we find the best parameter combination (weights and bias) for our 
logistic regression model?
Unlike linear regression, which uses ordinary least squares, logistic
regression typically uses Maximum Likelihood Estimation (MLE), i.e., the best
parameters (weights and bias) that maximize the likelihood of the observed
data.

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

    Intuitively speaking, the loss function penalizes the model for making 
    wrong predictions. If the model predicts a probability of 0.9 for a 
    spam email, and the email is actually spam (\(y=1\)), the loss is small.
    On the other hand, if the model predicts a probability of 0.1 for a 
    spam email, and the email is spam (\(y=1\)), the loss will be high. 

    The weights are gradually adjusted to minimize the loss.
    Think of it like turning knobs slowly until we get better predictions.
    
    Gradually adjusting these knobs to minimize the loss is referred to as
    gradient descent.

Conveniently, `scikit-learn` provides a logistic regression implementation
that takes care of the optimization for us. Finally, we look at a 
practical example to see logistic regression in action.

## Example

