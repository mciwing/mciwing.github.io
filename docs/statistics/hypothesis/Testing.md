# Testing Principals

Before diving into hypothesis testing, let's briefly revisit the [central limit theorem (CLT)](../../statistics/probability/CentralLimitTheorem.md). The CLT states that the [sampling distribution](../../statistics/probability/Sampling.md#sample-distribution) of the sample mean will approximate a normal distribution as the sample size becomes large, regardless of the population's distribution. Because measuring the entire population is often impractical, we rely on samples. Each sample provides an estimate, and repeated sampling yields a distribution of these estimates.

???+ example "Examples: Are Apples as Heavy as Apples" 

    Consider a seemingly nonsensical question:

    *"Are apples as heavy as apples?"*
   
    At first glance, this question doesn't make sense. We're comparing apples to apples! However, this example illustrates sampling variability under the null hypothesis.

    <figure markdown="span">
    ![Image title](../../assets/statistics/apple.jpg){width=50% }
    </figure>

    Imagine you have a large bucket of apples, and you want to test whether one group of apples is heavier than another group from the same bucket. Here's how you might proceed:

    1. **Sample Group A**: Randomly select 10 apples and measure their weights.
    2. **Sample Group B**: Randomly select another 10 apples and measure their weights.
    3. **Calculate the Mean Weights**: Compute the average weight for each group.
    4. **Compute the Difference**: Find the difference between the two average weights.

    Under the **null hypothesis** (no difference in weights), we expect the difference in mean weights to be zero. However, due to sampling variability, the difference is unlikely to be exactly zero. You might find that Group A has a mean weight of 150 grams, while Group B has a mean weight of 152 grams - a difference of 2 grams.

    Does this mean that apples in Group B are inherently heavier? Probably not. The observed difference is likely due to random variation.

## Null & Alternative Distribution

When comparing samples from the same population the expected difference is **Zero** (no difference under the null hypothesis). But due to sampling variability, the observed differences are small. By repeatedly sampling and calculating differences, we can create a **null distribution** - a distribution of differences expected under the null hypothesis \( H_0 \). The null distribution will center around zero and display the variability expected due to random sampling. 

> In statistical hypothesis testing, the null distribution is the probability distribution of the test statistic when the null hypothesis is true.
>
> -- <cite>Kent W. Staley - An Introduction to the Philosophy of Science</cite>

To build the null distribution:

1. **Repeat Sampling**: Take many pairs of samples from the population.
2. **Calculate Differences**: For each pair, compute the difference in sample means.
3. **Plot the Differences**: Create a histogram of these differences.

The alternative hypothesis posits that there is a genuine difference between groups. Therefore, under the alternative hypothesis, the distribution of differences shifts away from zero. The **alternative distribution** represents the expected differences if the alternative hypothesis is true.

The goal now is, to calculate the probability that those two distributions (Null and Alternative) are different from each other.

### Quantifying Differences Between Distributions
To assess whether an observed difference is [significant](../../statistics/hypothesis/Metrics.md#significance), we need to consider both the **difference of means** and the **variability** in the data.
The difference of means (DOM) - sometimes called signal - can be calculated by using:

\[
\text{DOM} = \text{Mean of Group 1} - \text{Mean of Group 2}
\]

On the other hand, there are two different kind of variability - or noise - in the data: 

- **Standard Deviation** (StD): Measures the spread of data within each group.
- **Standard Error** (SE): Estimates the variability of the sample mean.

To quantify the differences between the distributions, the **signal-to-noise ratio** can be calculated: 

\[
\text{Signal-to-Noise Ratio} = \frac{\text{Difference of Means}}{\text{Measure of Variability}}
\]

A higher ratio suggests that the observed effect is more likely to be real (not due to chance).

## The Foundation of Inferential Statistics

This concept of comparing signal to noise is the cornerstone of inferential statistics. Regardless of the specific statistical test, the underlying principle is the same:

- **Assess the Effect**: Measure the difference or relationship you're interested in.
- **Account for Variability**: Consider the variability in the data.
- **Determine Significance**: Use the signal-to-noise ratio to infer whether the effect is statistically significant.

Examples of Statistical Tests:

- [t-test](../../statistics/hypothesis/Ttest.md): Compares the means of two groups relative to the variability within the groups.
- [ANOVA](../../statistics/hypothesis/ANOVA.md): Analyzes differences among group means in a sample.
- [Regression Analysis](../../statistics/regression/General.md): Assesses the relationship between variables, considering residual variability.

