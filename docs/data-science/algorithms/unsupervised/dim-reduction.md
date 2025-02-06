# Dimensionality Reduction

## Principal Component Analysis (PCA)

In data science and machine learning, we often encounter data sets with 
hundreds or even thousands of features. We speak of high-dimensional data 
sets. While these features may contain valuable information, working with 
such high-dimensional data can be computationally expensive, prone to 
overfitting, and difficult to visualize. This is where another 
unsupervised method, dimensionality reduction comes in — a technique used to 
simplify data sets, while retaining much of the critical information.

One of the most widely used methods for dimensionality reduction is 
Principal Component Analysis (PCA). PCA transforms a high-dimensional (= 
lots of features) data set into a smaller set of features (components). In
practice, PCA can reduce hundreds of features down to just 2 or 3 
features, making PCA an ideal tool for visualization, preprocessing, and 
feature extraction.

In this section, we will explain the inner workings of PCA and apply it to
the semiconductor data set.

### What is PCA?

PCA is a **linear transformation technique** that identifies the directions 
(also called **principal components**) in which the data varies the most. 
These principal components capture as much variance as possible. PCA has a 
variety of applications, such as:

- **Data visualization**: Plot a dimensionality reduced data set on 2D.
- **Preprocessing**: Removing noise or redundant features while retaining the
  essential patterns in data.
- **Feature engineering**: Summarizing high-dimensional data into a smaller set
  of meaningful features.
