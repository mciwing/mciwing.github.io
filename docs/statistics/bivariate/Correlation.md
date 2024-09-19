# Measures of Correlation

This chapter covers the measures of linear relationships, specifically covariance and correlation. These measures help in characterizing the linear relationship between two variables, if such a relationship exists.

## Covariance

In the previous univariate parts, the metrics focused only on a single variable. Covariance allows us to determine the **relationship between two variables**. 

???+ defi "Definition"

    \[
    \text{cov}(X, Y) = \frac{\sum_{i=1}^{N}(x_i - \bar{x}) \cdot (y_i - \bar{y})}{N}
    \]

    where \(X\) and \(Y\) are variables consisting of \(N\) values, and \( \bar{x} \) and \( \bar{y} \) are their respective means.  

The name suggests that it is a type of 'variance,' as \( \text{cov}(X, X) = \sigma^2(X) \).

XXX Example XXX

**Interpretation of Covariance:**  

- Covariance indicates the **direction of the relationship**:
    - \(>0\): Positive relationship (if \(X\) increases, \(Y\) increases)
    - \(=0\): No relationship
    - \(<0\): Negative relationship (if \(X\) increases, \(Y\) decreases)
- Covariance does not provide information about the **strength** of the relationship since it is not dimensionless.
- To quantify the strength, we use a normalized measure called the correlation coefficient.  

## Correlation Coefficient

### Pearson

The Pearson correlation coefficient expresses both the **direction and strength** of the linear relationship between two variables. It is a normalized form of covariance and is **symmetric**: \( \rho_{X,Y} = \rho_{Y,X} \).

???+ defi "Definition"

    \[
    \rho = \frac{\text{cov}(X, Y)}{\sigma_x \cdot \sigma_y}
    \]

    where \(X\) and \(Y\) are metric variables, \( \sigma_x \) and \( \sigma_y \) are their standard deviations, and \( \text{cov}(X, Y) \) is the covariance. 

XXX Example XXX

**Interpretation of the Pearson Correlation Coefficient :**  

- The Pearson correlation coefficient has no dimesion.
- Its value ranges between \([-1 \dots 1]\) (according to the standard terminology by Jacob Cohen, 1988):
    - \(0\): No correlation
    - \(> \pm 0.1\): Weak correlation
    - \(> \pm 0.3\): Moderate correlation
    - \(> \pm 0.5\): Strong correlation
    - \(\pm 1\): Perfect positive/negative correlation (one variable can be derived from the other)

### Spearman

Covariance and the Pearson correlation coefficient require variables to be at least metric. When one of the variables is **ordinal**, the rank correlation should be calculated, with Spearman's method being a common choice. The interpretation of Spearman's rank correlation is similar to Pearson's.

???+ defi "Definition"

    \[
    \rho_s = 1 - \frac{6 \cdot \sum_{i=1}^{N} d_i^2}{N^3 - N} \quad \text{where } d_i = R(x_i) - R(y_i)
    \]

    with \(X\) and \(Y\) as variables consisting of \(N\) values and ranks \(R(x_i)\) and \(R(y_i)\).  

**Rank Formation**

- The rank corresponds to the position a value holds when all values are arranged in order.

    ???+ example 
    
        | \(x_i\)   | 2.17 | 8.00 | 1.09 | 2.01 |
        |-----------|------|------|------|------|
        | \(R(x_i)\)| 3    | 4    | 1    | 2    |

- For identical values, the average rank (mean of the relevant ranks) is used.

    ???+ example 
        | \(x_i\) | 1.09 | 2.17 | 2.17 | 2.17 | 3.02 | 4.50 |
        |---------|----|----|----|----|----|----|
        | \(R(x_i)\)| 1    | 3    | 3    | 3    | 5    | 6    |

        with \( (2+3+4)/3 = 3 \)



XX  Example XX

## Scatter Plot

A scatter plot provides a **graphical representation** of the relationship between two metric variables on a Cartesian coordinate system. Each **data pair** is treated as a **coordinate** and is represented by a point on the plot. This allows for identifying relationships, patterns, or trends between the variables.

<figure markdown="span">
  ![Firewall message](https://media.geeksforgeeks.org/wp-content/uploads/Correl.png){ width="400" }
  <figcaption>Different Types of Correlation (Source: https://www.geeksforgeeks.org/what-is-correlation-analysis/) </figcaption>
</figure>

## Recap

- Measures of linear relationships describe the relationship between two variables.
- Covariance identifies the direction of the relationship between two metrically scaled variables but not the strength.
- The Pearson correlation coefficient measures both the direction and strength of the relationship between two metrically scaled variables.
- If at least one variable is ordinal, the Spearman correlation coefficient is used.
- A scatter plot can visually represent the relationship between two metric variables.  

## Tasks