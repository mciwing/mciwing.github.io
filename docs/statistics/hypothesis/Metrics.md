# Metrics

## P-Values
P-values are a central measure of modern inferential statistics, often mentioned in research studies and statistical analyses. You might frequently hear statements like "The p-value is less than 0.05," highlighting their importance in determining statistical significance.

<figure markdown="span">
  ![Correlation Types](https://imgs.xkcd.com/comics/p_values.png){width=100% }
  <figcaption>(Source: <a href="https://xkcd.com/1478/">xkcd</a>) </figcaption>
</figure>

### Definition

A p-value is a probability metric that helps us determine the significance of our results. 

???+ defi "Definition: P-Value"
    The p-Value quantifies the likelihood of obtaining a test statistic at least as extreme as the one observed, assuming the null hypothesis is true. 
    
In simpler terms, it answers the question: *If there is no real effect or difference, what is the probability of observing the data we have collected?*

???+ info "Reminder"
    - **Null Hypothesis (H~0~)**: This is the default assumption that there is no effect or no difference. For example, when testing a new medication, the null hypothesis might state that the medication has no effect on patients compared to a placebo.

    - **Alternative Hypothesis (H~1~ or H~A~)**: This hypothesis suggests that there is an effect or a difference. In the medication example, the alternative hypothesis would state that the medication does have an effect on patients.

    In statistical testing, we often visualize these hypotheses using distributions:

    - **Null Hypothesis Distribution**: This represents the expected distribution of the test statistic if the null hypothesis is true. It is typically derived from theoretical probability distributions (like the normal distribution) and calculated using statistical formulas based on assumptions and degrees of freedom.

    - **Alternative Hypothesis Distribution**: This represents the distribution if the alternative hypothesis is true. However, in practice, we usually don't have a theoretical distribution for the alternative hypothesis because it's based on the actual effect we're trying to detect, which is unknown.Therefore, we collect data from experiments or studies, resulting in an observed test statistic (like a sample mean or proportion).



### Interpretation

The method for calculating a p-value depends on the statistical test being used (e.g., t-test, chi-squared test, ANOVA). While the computational approaches vary, the interpretation of the p-value remains consistent: the p-value answers the  fundamental question about the probability of observing the data under the null hypothesis.

- **Low P-Value (e.g., p < 0.05)**: Indicates that the observed data is unlikely under the null hypothesis. This leads us to consider rejecting the null hypothesis in favor of the alternative hypothesis.

- **High P-Value (e.g., p > 0.05)**: Suggests that the observed data is consistent with the null hypothesis. We do not have enough evidence to reject the null hypothesis.

???+ info "Note"
    A low p-value does not prove that the alternative hypothesis is true; it merely indicates that the null hypothesis may not fully explain the observed data.

???+ failure "Limitations"

    - **Cannot Prove Hypotheses**: P-values do not provide proof but rather evidence against the null hypothesis.

    - **Dependence on Sample Size**: Large samples can produce small p-values for trivial effects, while small samples might not detect significant effects.

    - **Not Measures of Effect Size**: A p-value does not indicate the magnitude of an effect.

### One-Tailed vs. Two-Tailed Tests

**One-Tailed Test**: Used when the research hypothesis predicts the direction of the effect (e.g., a new drug is expected to lower blood pressure). The critical region for rejecting the null hypothesis is entirely on one side of the distribution.

- *Example*: Testing if a new study technique increases test scores. The null hypothesis states there is no improvement, and the alternative hypothesis states there is an improvement. Only high test scores (one tail) are considered evidence against the null hypothesis.
- In a **one-tailed test** with an alpha level of 0.05, the entire 5% significance level is in one tail.

**Two-Tailed Test**: Used when the research hypothesis does not predict the direction (e.g., the drug affects blood pressure but could either raise or lower it). The critical regions are on both ends of the distribution.

- *Example*: Testing if a new fertilizer affects plant growth. The null hypothesis states it has no effect, while the alternative hypothesis states it has an effect (could be an increase or decrease). Both unusually high and low plant growth measurements (both tails) are evidence against the null hypothesis.
- In a **two-tailed test** with the same alpha level, the 5% is split between both tails (2.5% in each).


### Common Misconceptions

Understanding what p-values do **not** represent is crucial to avoid misinterpretations.

1. **Misconception**: A p-value of 0.02 means there's a 2% chance the effect is present in the population.

    - **Correction**: A p-value of 0.02 means there's a 2% probability of observing the test statistic (or something more extreme) assuming the null hypothesis is true. It does not indicate the proportion of the population exhibiting the effect.

2. **Misconception**: A p-value of 0.02 means there's a 98% chance that the sample statistic equals the population parameter.

    - **Correction**: The p-value does not provide the probability that the sample statistic equals the population parameter. It only assesses the likelihood of the observed data under the null hypothesis.

3. **Misconception**: A p-value smaller than the threshold confirms the effect is real.

    - **Correction**: A small p-value suggests that the observed data is unlikely under the null hypothesis, but it does not prove the effect is real. Other factors like sample size, data quality, and experimental design also play significant roles.

4. **Misconception**: A large p-value means the null hypothesis is true.

    - **Correction**: A large p-value indicates that the data is consistent with the null hypothesis, but it doesn't prove that the null hypothesis is true. It might also be due to insufficient sample size or variability in the data.



xxxx
xxxxx
xxxxxxxxxxxxxx




 **Collecting Data and Observing Test Statistics**


For instance, 
Suppose we're testing whether a coin is fair. 
The null hypothesis states:
    
that the coin has an equal chance of landing heads or tails. We flip the coin 100 times (our sample data) and observe that it lands on heads 60 times. Our test statistic is the observed number of heads.

---

 **Calculating the P-Value**

The p-value helps us understand how likely it is to observe our test statistic under the null hypothesis. We ask:

- *What is the probability of getting 60 or more heads in 100 coin flips if the coin is fair?*

Using the null hypothesis distribution (in this case, a binomial distribution with p = 0.5), we calculate this probability. If the p-value is low (commonly below 0.05), it suggests that such an extreme result is unlikely under the null hypothesis.

**Example**:

- In a **t-test** comparing the means of two groups, the p-value assesses the likelihood of observing a difference as large as the one found if the group means are actually equal in the population.

xxxx
xxxxx
xxxxxxxxxxxxxx




107 p-z- pairs (confidence)


## Significance
112
114


### DOF
108

### Errors
109

## Tests
### Parametric vs Non-Parametric
110
ev. 111