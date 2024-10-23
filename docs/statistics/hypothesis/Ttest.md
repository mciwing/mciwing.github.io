# T-Test

## Introduction to T-Tests

The **t-test** is a fundamental statistical method widely used in various fields to compare the means of two groups and determine if they are statistically different from each other. At its core, the t-test evaluates whether the difference between the means of two groups is significant or if it could have occurred by chance due to variability in the data. This is crucial when testing hypotheses in research studies.

???+ example "Example: Math Score"
    
    Suppose you're investigating whether a new tutoring program improves students' math test scores compared to a standard curriculum. Here, the two groups are:

    - **Group A:** Students using the new tutoring program.
    - **Group B:** Students following the standard curriculum.

    Your **alternative hypothesis** is that the mean test score of Group A is different from that of Group B. The **null hypothesis** states that there is no difference in the mean test scores between the two groups.


The t-test formula provides a standardized way to measure the difference between group means relative to the variability in the data:

???+ defi "Definition: T-Test"
    \[
    t_k = \frac{\bar{x}-\bar{y}}{s/\sqrt{n}} = \frac{\text{Difference of Means}}{\text{Standard Deviations}}
    \]

    Where:

    - \(\bar{x}\) = average of group x
    - \(\bar{y}\) = average of group y
    - \(s\) = standard error of the arithmetic mean = \(\sigma\sqrt{n}\)
    - \(n\) = number of samples
    - \(k\) = degree of freedom

This formula essentially calculates how many standard deviations the difference between the two means is away from zero. A larger absolute value of \(t\) indicates a more significant difference between the groups.

### Calculating the p-value

In the following graph you see the probability of a certain t-value occurring given that the null hypothesis is true. This curve is called the *t-distribution* (or sometimes Student's t-distribution).

<iframe src="/assets/statistics/prob_hypo_tdist.html" width="100%" height="400px"></iframe>
??? code "Code"
    ``` py
    import numpy as np
    import pandas as pd
    import plotly.express as px
    from scipy.stats import norm

    # Generate the data for the normal distribution
    x = np.linspace(-4, 4, 1000)
    y = norm.pdf(x, 0, 1)

    # Create DataFrame for Plotly
    df = pd.DataFrame({'x': x, 'y': y})

    # Create the plot
    fig = px.line(df, x='x', y='y')

    # Adjust the plot
    fig.data[0].update(line=dict(color='#00416E', width=2))

    # Add layout modifications
    fig.update_layout(
        xaxis_title_text='t-Value',
        yaxis_title_text='P(t|H0)',
        title=dict(
            text=f'<b><span style="font-size: 10pt">t-Distribution</span></b>',
        ),
        showlegend=False,
    )

    # Show the plot
    fig.show()
    ```

If the null hypothesis is true, we expect the difference between the means to be zero \(\bar{x} - \bar{y} = 0\), resulting in a t-value of zero. This corresponds to the highest probability and the peak of the distribution. However, due to sampling variability and noise, the means will not be exactly equal (even if the null hypothesis is true), leading to t-values around zero and therefore to the t-distribution.

The **p-value** helps determine the statistical significance of your results. It represents the probability of observing a t-value as extreme as the one calculated, assuming the null hypothesis is true.

???+ example "Example: Math Score"

    Let's stick with the example from before. Imagine you conduct the tutoring program study and calculate a t-value of 2.5 with a corresponding probability of 0.02. 

    
    <iframe src="/assets/statistics/prob_hypo_t_tutor.html" width="100%" height="400px"></iframe>

    Since 2.5 is extremer than the common significance level of 0.05 with the corresponding critical t-value of 1.8, the null hypothesis can be rejected and you conclude that the tutoring program has a statistically significant effect on test scores.

    <figure markdown="span">
    ![Tutor](https://memecreator.org/static/images/memes/4321085.jpg){width=70% }
    <figcaption>(Source: <a href="https://www.memecreator.org/meme/need-a-tutor-i-noah-guy/">Memecreator</a>) </figcaption>
    </figure>

### Strategies to Maximize the t-value

To increase the likelihood of detecting a true effect, consider the following approaches:

1. Increase the Difference Between Means (\(\bar{x} - \bar{y}\)):

    - **Action:** Enhance the impact of the treatment or condition.
    - **Example:** If testing a new drug, use a dosage that is expected to produce a noticeable effect compared to the placebo.

2. Decrease the Variability (Reduce \(s\)):

    - **Action:** Control external factors to minimize data dispersion.
    - **Example:** In an agricultural study measuring crop yield, ensure that soil quality, irrigation, and sunlight are consistent across test plots.

3. Increase the Sample Size (\(n\)):

    - **Action:** Collect data from more subjects to reduce the standard error.
    - **Example:** Survey a larger number of participants in a market research study to obtain more reliable results.


## One-Sample T-Test

The **one-sample t-test** is the simplest form of the t-test family and serves as an excellent introduction to understanding t-tests in general. It is used when you have a **single sample** and want to determine whether its mean is significantly different from a known or hypothesized **population mean**. So in this case, we do not have two different samples or groups, but one sample from a population. 

???+ defi "Definition: One-Sample T-Test"
    The formula for calculating the t-value in a one-sample t-test is:

    \[
    t = \frac{\bar{x} - \mu}{\frac{s}{\sqrt{n}}}
    \]

    Where:

    - \(\bar{x}\) = Sample mean
    - \(\mu\) = Hypothesized population mean (the value you're testing against)
    - \(s\) = Sample standard deviation
    - \(n\) = Sample size

    The degrees of freedom (df) for this test are calculated as \(df = n - 1\).

### Applying the Test

0. **Set the Hypothesis**
1. **Collect Data**: Measure the stress levels of the sample employees.
2. **Calculate the Sample Mean (\(\bar{x}\))**: Find the average stress level from your data.
3. **Compute the Sample Standard Deviation (s)**.
4. **Calculate the t-value** using the formula above.
5. **Determine Degrees of Freedom**: \(df = n - 1\).
6. **Find the p-value**: Use the t-distribution table or statistical software.
7. **Make a Decision**: If the p-value is less than your significance level (e.g., 0.05), reject the null hypothesis.

???+ info "Robustness"
    The t-test is relatively robust to violations of normality with larger sample sizes (n > 30).

### Assumptions of the One-Sample t-test

For the test results to be valid, the following assumptions should be met:

1. **Independence**: Observations are independent of one another.
2. **Normality**: The data should be approximately normally distributed, especially important for small sample sizes.
3. **Scale of Measurement**: The data are continuous and measured on an interval or ratio scale.

???+ example "Example: Thickness Testing"
    A factory produces metal sheets that are supposed to have an average thickness of \(2.5 mm\). The quality control team wants to ensure that the production process is meeting this specification. They randomly sample 30 sheets from the production line and measure their thickness.

    They want to determine if the average thickness of the sampled sheets is statistically different from the target mean of \(2.5 mm\).

    Assumptions: 
    - Significance level \( \alpha = 0.05 \)
    - Two-Tailed Tests: There can be positive or negative deviations 

    ---

    - **Set the hypotheses:**
        - **Null hypothesis (H~0~):** The mean thickness of the sheets is \(2.5 mm\) (μ = \(2.5 mm\)).
        - **Alternative hypothesis (H~1~):** The mean thickness of the sheets is not \(2.5 mm\) (μ ≠ \(2.5 mm\)).
    
    ---

    - **Collect sample data** & **Calculate the (\(\bar{x}\)) and (\s))**: 
    Suppose the sample of 30 sheets has an average thickness of \(2.45 mm\) and a standard deviation of \(0.1 mm\).

    ---

    - **Calculate the t-value:**

    \[
    t = \frac{2.45 - 2.5}{\frac{0.1}{\sqrt{30}}} = \frac{-0.05}{\frac{0.1}{5.477}} = \frac{-0.05}{0.01826} ≈ -2.74
    \]

    ---

    - **Determine Degrees of Freedom:**

    \[
    df = n - 1 = 30 - 1 = 29 
    \]

    ---

    - **Find the p-value:**
    0.005

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   

5. **Compare with the critical t-value:**
   - For a significance level of \( \alpha = 0.05 \) and \( df = 29 \), the critical t-value for a two-tailed test is approximately \( \pm 2.045 \).

6. **Make a decision:**
   - The calculated t-statistic is **-2.74**, which is more extreme than the critical value of \( -2.045 \). Therefore, we reject the null hypothesis.

### **Conclusion:**
There is significant evidence at the 5% level to conclude that the average thickness of the metal sheets is not 2.5 mm. The production process may need to be adjusted to ensure the thickness specification is met.


**Example:** Suppose you're a psychologist studying the average stress level of employees in a high-pressure industry. The national average stress level, measured on a standardized scale, is known to be 50. You collect data from a sample of employees in a particular company to see if their average stress level deviates from the national average.
- **Null Hypothesis (\(H_0\))**: The average stress level of employees in the company is equal to 50.
- **Alternative Hypothesis (\(H_1\))**: The average stress level of employees in the company is not equal to 50.





**Key Points to Remember:**

- Use the one-sample t-test when comparing a sample mean to a specific value.
- Ensure that the data meet the test assumptions for valid results.
- Interpret the results in the context of your research question and consider both statistical and practical significance.

By mastering the one-sample t-test, you lay the groundwork for understanding more complex statistical tests and enhancing your data analysis skills.

**Key Takeaways:**

- The t-test compares group means relative to variability and sample size.
- A larger absolute t-value indicates a more significant difference between groups.
- Strategies to maximize the t-value include increasing mean differences, decreasing variability, and increasing sample size.
- Always interpret statistical results within the context of your specific research question and practical significance.

By mastering the t-test, you'll be better equipped to analyze data critically and contribute valuable insights in your field of study.

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx



## Two-Sample T-Test


## Nonparametric T-Tests

### Wilcoxon Signed-Rank

### Mann-Whitney U Test

## Permutation Testing



