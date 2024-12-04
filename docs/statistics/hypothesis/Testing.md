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

### Null Distribution
When comparing samples from the same population the expected difference is **Zero** (no difference under the null hypothesis). But due to sampling variability, the observed differences are small. By repeatedly sampling and calculating differences, we can create a **null distribution** - a distribution of differences expected under the null hypothesis \( H_0 \). The null distribution will center around zero and display the variability expected due to random sampling. 

> In statistical hypothesis testing, the null distribution is the probability distribution of the test statistic when the null hypothesis is true.
>
> -- <cite>Kent W. Staley - An Introduction to the Philosophy of Science</cite>

To build the null distribution:

1. **Repeat Sampling**: Take many pairs of samples from the population.
2. **Calculate Differences**: For each pair, compute the difference in sample means.
3. **Plot the Differences**: Create a histogram of these differences.

So if we stick with our `age` example, and compare samples from the whole population, we will receive a distribution of age differences:

<iframe src="/assets/statistics/prob_testing_nulldist.html" width="100%" height="400px"></iframe>

??? code "Code"
    ``` py
    from ucimlrepo import fetch_ucirepo 
    
    # fetch dataset 
    adult = fetch_ucirepo(id=2) 
    
    # data (as pandas dataframes) 
    data = adult.data.features

    import plotly.express as px
    import random
    import numpy as np
    import pandas as pd

    sample_means_dif = []
    for i in range(10000):
        sample_means_dif.append(np.mean(random.sample(list(data.age), 20))-np.mean(random.sample(list(data.age), 20)))


    fig = px.histogram(x=sample_means_dif)
    fig.update_traces(marker=dict(color='rgba(0, 65, 110, 0.8)'))

    # Add a horizontal line for the population mean
    fig.add_vline(x=0, line_dash="dash", annotation_text="Expected Value: 0", annotation_position="top right", line_color="#E87F2B")

    fig.update_layout(
            barmode='overlay',
            yaxis_title_text='Absolute Frequency',
            xaxis_title_text='Sample Means Difference',
            title=dict(
                text='<b><span style="font-size: 10pt">Null Distribution</span><br><span style="font-size: 8pt">Age vs. Age</span><span style="font-size: 5pt"> Number of Samples: 10.000 | Data: UCIML Repo: Adult; variable: age</span> </b>',
            ),
        )

    fig.show()

    ```
In this case we see, that the distribution looks like we would imagine if the null hypothesis cannot be rejected (is true). 

### Alternative Distribution

The alternative hypothesis posits that there is a genuine difference between groups. Therefore, under the alternative hypothesis, the distribution of differences shifts away from zero. The **alternative distribution** represents the expected differences if the alternative hypothesis is true.

Again we stick with the `age` example and compare the age differences of mutliple samples for `male` and `female` in our dataset:


<iframe src="/assets/statistics/prob_testing_altdist.html" width="100%" height="400px"></iframe>

??? code "Code"
    ``` py
    from ucimlrepo import fetch_ucirepo 
    
    # fetch dataset 
    adult = fetch_ucirepo(id=2) 
    
    # data (as pandas dataframes) 
    data = adult.data.features

    import plotly.express as px
    import random
    import numpy as np
    import pandas as pd

    sample_means_dif = []
    for i in range(10000):
        sample_means_dif.append(np.mean(random.sample(list(data[data['sex']=="Male"].age), 20))-np.mean(random.sample(list(data[data['sex']=="Female"].age), 20)))


    fig = px.histogram(x=sample_means_dif)
    fig.update_traces(marker=dict(color='rgba(0, 65, 110, 0.8)'))

    # Add a horizontal line for the population mean
    fig.add_vline(x=np.mean(sample_means_dif), line_dash="dash", annotation_text="Mean Difference: "+str(np.mean(sample_means_dif)), annotation_position="top right", line_color="#E87F2B")

    fig.update_layout(
            barmode='overlay',
            yaxis_title_text='Absolute Frequency',
            xaxis_title_text='Sample Means Difference',
            title=dict(
                text='<b><span style="font-size: 10pt">Alternative Distribution</span><br><span style="font-size: 8pt">Age (Male) vs. Age (Female) </span><span style="font-size: 5pt"> Number of Samples: 10.000 | Data: UCIML Repo: Adult; variable: age</span> </b>',
            ),
        )

    fig.show()

    ```
What we can see now is, that the peak (mean) of the distribution ist not around zero and therefore the null hypothesis is false and can be rejected against an alternative hypothesis. But is this difference significant?

### Quantifying Differences Between Distributions
To assess whether an observed difference is [significant](../../statistics/hypothesis/Metrics.md#significance), we need to analyze the center of the two peaks of the null distribution and the alternative distribution. However, to make this comparison meaningful, we need to scale or normalize this difference based on the spread (or width) of the distributions. This normalization accounts for the units and ensures that the comparison is independent of the scale. For example, if we're measuring something in centimeters, both the numerator and denominator will be in the same unit, effectively canceling the units out.


<iframe src="/assets/statistics/prob_testing_distComp.html" width="100%" height="400px"></iframe>

??? code "Code"
    ``` py
    import plotly.graph_objects as go
    fig = go.Figure()

    fig.add_trace(go.Histogram(x=sample_means_dif, marker=dict(color='rgba(0, 65, 110, 0.8)'),name='Null Distribution'))

    # Zweite Spur hinzufügen
    fig.add_trace(go.Histogram(x=sample_means_difa, marker=dict(color='rgba(232, 127, 43, 0.8)'),name='Alternative Distribution'))

    # Add a horizontal line for the population mean
    fig.add_vline(x=0, line_dash="dash", annotation_text="H_0 Center", annotation_position="top left", line_color="#00416E")
    fig.add_vline(x=np.mean(sample_means_difa), line_dash="dash", annotation_text="H_a Center", annotation_position="top right", line_color="#E87F2B")


    fig.update_layout(
            barmode='overlay',
            yaxis_title_text='Absolute Frequency',
            xaxis_title_text='Sample Means Difference',
            title=dict(
                text='<b><span style="font-size: 10pt">Differences in Distributions</span><br><span style="font-size: 5pt"> Number of Samples: 10.000 | Data: UCIML Repo: Adult; variable: age</span> </b>',
            ),
        )

    fig.show()

    ```

It’s important to note that different statistical methods may define this "width" differently. So, we shouldn't get too caught up in formal definitions here. The key is to keep things flexible and understand this as a general approach that various statistical tests can adapt in different ways.

In essence, what we’re doing is taking the difference between two central points (which we'll call "signal") and dividing it by some measure of the distribution’s width (which represents "noise"). This idea of comparing signal to noise is at the core of hypothesis testing. Whether we’re dealing with null hypothesis testing or alternative methods, the goal is to quantify how strong the signal is relative to the noise.

\[
\text{Signal-to-Noise Ratio} = \frac{\text{Difference of Means}}{\text{Measure of Variability}}
\]

This concept of comparing signal to noise is the cornerstone of inferential statistics. Regardless of the specific statistical test, the underlying principle is the same:

- **Assess the Effect**: Measure the difference or relationship you're interested in.
- **Account for Variability**: Consider the variability in the data.
- **Determine Significance**: Use the signal-to-noise ratio to infer whether the effect is statistically significant.

Examples of Statistical Tests:

- [t-test](../../statistics/hypothesis/Ttest.md): Compares the means of two groups relative to the variability within the groups.
- [ANOVA](../../statistics/hypothesis/ANOVA.md): Analyzes differences among group means in a sample.
- [Regression Analysis](../../statistics/regression/LinearRegression.md): Assesses the relationship between variables, considering residual variability.

