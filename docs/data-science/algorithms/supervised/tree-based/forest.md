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
case of classification, the majority vote is taken. 

It was observed that introducing randomness in the tree-growing process
improves the model performance.

???+ info

    Contrary to the classic CART, random forests do not constrain the tree 
    growth. I.e., trees are fully grown and not pruned.
