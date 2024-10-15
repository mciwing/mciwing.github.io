# Central Limit Theorem

In this section, we'll explore the **Central Limit Theorem (CLT)**, a cornerstone of probability and statistics that works hand in hand with the **Law of Large Numbers (LLN)** you've previously learned about. The CLT is fascinating because it explains why normal (Gaussian) distributions are so prevalent in statistics, even when the underlying data doesn't seem to fit that mold. 

<figure markdown="span">
  ![Correlation Types](https://i.pinimg.com/enabled/564x/2c/67/ac/2c67acc310967612e3cbac8bc636d960.jpg){width=50% }
  <figcaption>(Source: <a href="https://at.pinterest.com/pin/663999538798585356/">Pinterest</a>) </figcaption>
</figure>

## Definition & Interpretation

???+ defi "Interpretation: Central Limit Theorem"
    The distribution of sample means approaches a normal distribution as the number of samples becomes large, regardless of the shape of the population distribution.

But what does this mean?

- **Population Distribution**: This could be any distribution—uniform, skewed, bimodal, or even a highly irregular distribution.

    <iframe src="/assets/statistics/prob_clt_agedist.html" width="100%" height="400px"></iframe>
    ??? code "Code"
        ``` py
        import plotly.express as px

        fig = px.histogram(data, x="age")
        fig.update_traces(marker=dict(color='rgba(0, 65, 110, 0.8)'))

        fig.update_layout(
                barmode='overlay',
                yaxis_title_text='Absolute Frequency',
                xaxis_title_text='Age',
                title=dict(
                    text='<b><span style="font-size: 10pt">Age Distribution</span><br> <span style="font-size:5">Data: UCIML Repo: Adult; variable: age</span></b>',
                ),
            )

        fig.show()
        ```

- **Sample Means**: If you take multiple samples from this population and calculate their means, those means will form their own distribution.
    ```py
    sample_mean = np.mean(random.sample(list(data.age), 20))
    ```

    <iframe src="/assets/statistics/prob_clt_agemeandist.html" width="100%" height="400px"></iframe>

    ??? code "Code"
        ``` py
        sample_means = []
        for i in range(100):
            sample_means.append(np.mean(random.sample(list(data.age), 20)))

        fig = px.histogram(x=sample_means)
        fig.update_traces(marker=dict(color='rgba(0, 65, 110, 0.8)'))

        fig.update_layout(
                barmode='overlay',
                yaxis_title_text='Absolute Frequency',
                xaxis_title_text='Sample Mean',
                title=dict(
                    text='<b><span style="font-size: 10pt">Sample Mean Distribution</span><br><span style="font-size: 8pt">Sample Size: 20 | Number of Samples: 100</span> <span style="font-size:5">Data: UCIML Repo: Adult; variable: age</span></b>',
        
                ),
            )
        fig.show()
        ```

- **Result**: As the number of samples increases, the distribution of these sample means will tend toward a normal distribution.
    <iframe src="/assets/statistics/prob_clt_agemeandist_large.html" width="100%" height="400px"></iframe>

    ??? code "Code"
        ``` py
        sample_means = []
        for i in range(100000):
            sample_means.append(np.mean(random.sample(list(data.age), 20)))

        fig = px.histogram(x=sample_means)
        fig.update_traces(marker=dict(color='rgba(0, 65, 110, 0.8)'))

        fig.update_layout(
                barmode='overlay',
                yaxis_title_text='Absolute Frequency',
                xaxis_title_text='Sample Mean',
                title=dict(
                    text='<b><span style="font-size: 10pt">Sample Mean Distribution</span><br><span style="font-size: 8pt">Sample Size: 20 | Number of Samples: 100000</span> <span style="font-size:5">Data: UCIML Repo: Adult; variable: age</span></b>',
        
                ),
            )
        fig.show()
        ```

This demonstrates that **even if the original data is not normally distributed**, the distribution of the sample means will be approximately normal if the sample size is large enough.

## Relation to the Law of Large Numbers

The **Law of Large Numbers** states that as the size of a sample increases, the sample mean will get closer to the population mean. When combined with the CLT, we understand not only that the sample mean converges to the population mean but also that the distribution of those sample means becomes normal.

## Why Is the Central Limit Theorem Important?

**Simplifies Statistical Analysis**

- **Normality Assumption**: Many statistical tests assume normality. Thanks to the CLT, we can often safely make this assumption for sample means or sums.
- **Parameterization**: Normal distributions are fully described by their mean and variance, making them easy to work with.

    <figure markdown="span">
    <div style="background-color: white; display: flex; justify-content: center;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/7/74/Normal_Distribution_PDF.svg" style="width: 70%;">
    </div>
    <figcaption style="text-align: center;">(Source: <a href="https://en.wikipedia.org/wiki/Normal_distribution">Wikipedia</a>) </figcaption>
    </figure>


**Practical Applications**

- **Confidence Intervals**: The CLT allows us to construct confidence intervals around sample means.
    <figure markdown="span">
    <div style="background-color: white; display: flex; justify-content: center;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/8/8c/Standard_deviation_diagram.svg" style="width: 100%;">
    </div>
    <figcaption style="text-align: center;">(Source: Ainali on <a href="https://commons.wikimedia.org/wiki/File:Standard_deviation_diagram_micro.svg">Wikipedia</a>) </figcaption>
    </figure>

- **Hypothesis Testing**: Facilitates hypothesis testing by enabling the use of z-scores and t-scores.
- **Quality Control**: In manufacturing, the CLT helps in monitoring process variations.



## Recap

The Central Limit Theorem is a powerful reminder that, regardless of the original data distribution, the process of sampling and aggregation tends to produce a normal distribution. This universality is why we often say, **"All roads lead to Gauss."** Understanding the CLT not only deepens your grasp of statistical principles but also equips you with the tools to make accurate inferences from data in a wide array of fields.

# Tasks
???+ question "Task: Central Limit Theorem"
    We use the biased die example from before: 

    ``` py
    die_biased = [1, 2, 4, 5, 6, 6]
    ```

    Work on the following tasks: 
    
    1. Calculate the expected value of the biased die (mean).
    2. Visualize the probability of each side in a histrogram.
    3. Now we perform some experiments:
        - Choose one random side (`#!python sample_size = 1`) of the biased die. Repeat this `100.000` times and visualize the frequency in a histogram. 
        - Compare the result with the visualization of the the probability. 
        - Now increase the `sample_size` and inspect the change in histogram. 
        - Does the calculated expected value match with the mean value of the normal distribution? 
