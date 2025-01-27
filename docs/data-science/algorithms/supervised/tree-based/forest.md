# Random Forest

# Random Forest

While decision trees are easy to interpret, they have several drawbacks: they
are prone to overfitting and are sensitive to slight changes in the data.

Random Forest is an ensemble method that addresses these drawbacks at the cost
of slightly reduced interpretability. At its core, a random forest is simply a
collection of decision trees. Since we have already extensively discussed the
CART (Classification and Regression Trees) algorithm, we can dive right in.

## Introduction

???+ info

    Random forests were introduced by Leo Breiman in 2001. The following 
    section closely follows the original paper.

    ^^Breiman, L. Random Forests. *Machine Learning 45*, 5–32 (2001).^^
    [https://doi.org/10.1023/A:1010933404324](https://doi.org/10.1023/A:1010933404324)


