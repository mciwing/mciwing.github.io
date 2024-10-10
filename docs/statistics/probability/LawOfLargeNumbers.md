# Law of Large Numbers

## Sample Distribution
In this explanation, we'll talk about creating sample distributions, an essential topic in inferential statistics. This is important for generating confidence intervals and making inferences about a population from a sample, which is a core goal of inferential statistics.

???+ code "Code"
    For the upcoming example, the following data will be used: 
        ``` py
        from ucimlrepo import fetch_ucirepo 
        
        adult = fetch_ucirepo(id=2) # fetch dataset 
        data = adult.data.features # data (as pandas dataframes) 
        ```

### Creating a Data Distribution
Let’s say we’re interested in finding out the average **age** of people. While we know there is a wide range of ages, we want to get a more precise understanding. Statistically, this means determining the **population parameter** for the age of people. However, it’s not feasible to find out the age of every person in the world. Why? There are simply too many people, living in different regions, and new individuals are born while others pass away. Additionally, we might accidentally include the same person more than once, making the task more complicated.

Instead of measuring the entire population, we can take a **random sample** of people. For example, we could collect the ages of 100 individuals. 

```py
sample = random.sample(list(data.age), 100)
```

One person might be 25 years old, another might be 42 years old, and so on. After gathering the data, we can create a **distribution** of these ages, often visualized as a histogram, and calculate the **sample mean** (the average age of the people in our sample).

```py
sample_mean = np.mean(sample)
```

<iframe src="/assets/statistics/prob_sample1.html" width="100%" height="400px"></iframe>

??? code "Code"
    ``` py
    # Pick a random sample of 100 from the data and calculate the mean
    sample = random.sample(list(data.age), 100)
    sample_mean = np.mean(sample)

    # Count the frequency of each age in the sample
    pd.DataFrame(sample)
    s_counts = pd.DataFrame(sample).value_counts().sort_index()
    s_counts = s_counts.to_frame().reset_index()

    # Plot the sample data
    fig = px.bar(x = s_counts[0], y=s_counts['count'])
    fig.update_traces(marker=dict(color='rgba(0, 65, 110, 0.8)'))

    # Add a vertical line for the population mean
    fig.add_vline(x=sample_mean, line_dash="dash", annotation_text="Mean: "+str(sample_mean), annotation_position="top right", line_color="#E87F2B")

    # Adjust the layout
    fig.update_layout(
        barmode='overlay',
        xaxis_title_text='Age',
        yaxis_title_text='Frequency',
        title=dict(
                text='<b><span style="font-size: 10pt">Age Distribution - Sample 4 (Mean: '+str(sample_mean)+')</span> <br> <span style="font-size:5">Data: UCIML Repo: Adult; variable: age</span></b>',
            ),
    )

    fig.show()
    ```

Now, the **sample mean** we calculate from our 100 people is just one estimate of the population's average age.

???+ info "Outlook"

    How does this sample mean realate to the actual population mean? 
    And how confident are we, that this sample mean is really close to the population mean? 
    Those are questions we will learn to answer in the upcomming sections about confidence intervals and hypothesis testing.
 

However, it’s important to understand that this is just **one estimate**. If we take another random sample of 100 people, we might get a slightly different average because not all individuals are the same age. So, what can we do? 

<div class="tenor-gif-embed" data-postid="25159664" data-share-method="host" data-aspect-ratio="1.33333" data-width="40%"><a href="https://tenor.com/view/stewie-repetition-gif-25159664">Stewie Repetition GIF</a>from <a href="https://tenor.com/search/stewie+repetition-gifs">Stewie Repetition GIFs</a></div> <script type="text/javascript" async src="https://tenor.com/embed.js"></script>

Right, we repeat the experiment! We measure another sample of 100 people and calculate a new sample mean.
Note, that there can be an overlap between those two samples (one person was part of the first and the second sample). This is called **sampling with replacement**. 

We notice that the results are similar to the first sample, but not exactly the same. 

<iframe src="/assets/statistics/prob_sample2.html" width="100%" height="400px"></iframe>

This difference is known as **sampling variability** - the natural variation that occurs when taking different samples from the same population. More about this topic will be covered in the  [Sampling Variability](#sampling-varibility) section. 

???+ question "Task: Data Distribution"
    Use the following dataset:
    ``` py
    from ucimlrepo import fetch_ucirepo 
  
    # fetch dataset 
    adult = fetch_ucirepo(id=2)
    # https://archive.ics.uci.edu/dataset/2/adult
    
    # data (as pandas dataframes) 
    data = adult.data.features 

    # Show the first 5 rows
    data.head()
    ```
    Work on the following task: 

    1. Pick a random sample of 100 values from the `hours-per-week` attribute
    2. Calculate the mean of this sample
    3. Plot the sample distribution as a `plotly.express` bar chart. Add vertical line (`fig.add_vline`) to indicate the sample mean
    4. Calculate the mean of the population (all the entries in the dataset) and compare it with the sample


### Creating a Sample Distribution of Means

We can repeat this **sampling process** multiple times. Let’s say we take **N samples**. Each sample gives us a new **sample mean**, and these means will vary slightly due to the natural differences in people's ages. Now, instead of focusing on individual ages (data distribution), we can create a **distribution of sample means** - a new distribution that shows how the sample estimates themselves vary.


<iframe src="/assets/statistics/prob_distSampMean.html" width="100%" height="400px"></iframe>

This distribution of **sample means** gives us valuable insights about the population. For example, if most of the sample means are very close to each other, we can be more confident that our sample estimates are close to the **true population mean**. However, if the sample means are widely spread out, it indicates that we might need larger or more representative samples to get a more accurate estimate of the population's true average age.

<iframe src="/assets/statistics/prob_lawoflarge1.html" width="100%" height="400px"></iframe>

???+ info "Different Types of Sample Distribution"
    While we have been using the **mean** as an example, the same approach can be applied to other statistics as well. For instance, you could look at the **variance**. If you're interested in knowing how much **age varies** across a population, you could calculate the **variance** or **standard deviation** for each sample.

    By repeating the process with multiple samples, you can then create a sample distribution of these variance estimates. This allows you to find the **average variance** across all the samples, giving you a better understanding of how much variability exists in the ages of the overall population.
    
???+ question "Task: Distribution of Means"

### Sample Distribution of Differences
Let's shift the focus of our example and explore sample estimate differences instead of just looking at one parameter.  The question we want to explore is: are widowed individuals generally older than people who have never been married? While it seems obvious that widowed individuals are likely to be older, since people tend to marry before becoming widowed, let’s frame this question statistically to better understand the process.

We start by imagining two populations: one of widowed individuals and one of never-married individuals. 

```py
data_widowed = data[data['marital-status'] == 'Widowed'].age
data_never_married = data[data['marital-status'] == 'Never-married'].age
```

Since it’s not practical to measure the age of every person in both groups, we take a random sample from each. For example, we could sample 100 widowed individuals and 100 people who have never been married, 

```py
sample_widowed = random.sample(list(data_widowed), 100)
sample_never_married = random.sample(list(data_never_married), 100)
```

and then calculate the average age for each group.

```py
sample_widowed_mean = np.mean(sample_widowed)
sample_never_married_mean = np.mean(sample_never_married)
```

Let’s say, in the first sample, the average age of the widowed group is 70 years, and the average age of the never-married group is 45 years. The difference between these averages is 25 years. However, this is just one sample, and the difference might vary slightly if we take another random sample. So, we repeat the process with a second random sample and find that the difference this time is 24 years.

<iframe src="/assets/statistics/prob_diffSampMean.html" width="100%" height="400px"></iframe>

By repeating this process across many samples, we can build a distribution of the differences in average age between the widowed and never-married groups. This distribution allows us to see how consistent the differences are across various samples. If the differences are relatively consistent, we can be confident that widowed individuals tend to be older than those who have never been married. If the differences vary widely, we may need larger or more representative samples to draw a reliable conclusion.

<iframe src="/assets/statistics/prob_diffSampdiff.html" width="100%" height="400px"></iframe>

???+ info "Sign of the Estimator"

    It’s also important to note that, just like in other statistical comparisons, the sign of the difference (positive or negative) doesn’t affect the actual result. For instance, if we subtract the average age of the never-married individuals from that of the widowed group, we’ll get a positive difference. But if we subtract the widowed individuals' ages from the never-married individuals' ages, the result will be negative. Statistically, both results show the same difference; it’s just a matter of interpretation.

### Random & Representative Sampling
To give another example, suppose we wanted to compare the ages of people from different regions, say those living in urban areas versus rural areas. Even if there’s no significant age difference between the two groups, each sample might show slight variations due to natural differences in the sample. By taking many samples, we could build a distribution of differences and better understand whether any observed difference is consistent.

This also emphasizes the importance of random and representative sampling. If we don’t carefully select our samples, we might get misleading results. For instance, imagine comparing life expectancy in two countries, but we only sample older people in one country and younger people in the other. The resulting data would falsely suggest a significant difference in life expectancy between the countries, when in reality, the sampling was biased. To avoid this, we need to ensure that our samples fairly represent the populations we’re studying.

## Sampling Varibility

Variability is a crucial concept in statistics and probability and plays a significant role in scientific research. It’s also one of the main sources of frustration for researchers because it can make results less predictable and more complex. Let’s dive into the idea of **sampling variability**, where this variability comes from, and why understanding it is so important.

Imagine you have a research question: **What is the average age of workers in a factory?** To answer this, you decide to measure the age of a few workers. Let's say you randomly select one worker who is 45 years old. Is this the average age of all workers in the factory? Most likely not. So, you keep asking more workers and get different ages like 50, 34, 60, etc. This difference in ages between the workers is an example of **sampling variability** - the natural differences that occur when taking samples from a population.

Even though the overall population (all workers in the factory) has a true average age, you will get slightly different values from each sample you take. This is why relying on just one sample to represent an entire population can lead to inaccurate results. The goal is to reduce this variability by taking more samples and averaging them to get a more reliable estimate of the population’s average age like we did before.

???+ defi "Definition: Sampling Variability"
    Using the

    - same measurement (e.g. mean) on 
    - different samples (e.g. age of 100 people) from the 
    - same population (e.g. age of all people in the world) can lead to 
    - different values (e.g. 47 or 52,...)

### Sources of Sampling Variability

1. **Natural Variation**: In many fields, especially biology and sociology, natural variation occurs. In our factory example, workers come from different backgrounds and generations, which naturally causes variability in their ages.
   
2. **Measurement Noise**: In some cases, the tools or methods used to gather data may introduce variability. For instance, if you’re using a tool with low precision, like a scale that only measures in whole kilograms when you need to measure in grams, you introduce errors in your measurements.

3. **Complex Systems**: Variability can also come from the complexity of the system being studied. In the factory example, factors like different hiring policies, regional differences, or workforce changes can add to the variation in workers’ ages.

4. **Uncontrollable Factors**: Some sources of variability, like random or unpredictable events, are outside of the researcher's control. For example, economic conditions might affect the hiring or retirement age of workers, adding unpredictability.

### Dealing with Sampling Variability

To reduce the impact of sampling variability, one of the most effective strategies is to **take multiple samples**. Instead of measuring just a few workers' ages, you would gather information from a larger sample, maybe 100 or more workers, and calculate the average age. The more samples you take, the closer you get to the true average age of the entire population. This is based on the [**law of large numbers**](#law-of-large-numbers_1), which states that as you increase the number of samples, the average of those samples will get closer to the population mean.

Additionally, **statistical tools** like confidence intervals can help you understand how close your sample estimate is to the actual population parameter. Confidence intervals provide a range within which the true average age of the factory workers is likely to fall, giving a better sense of the precision of your estimate.


???+ question "Task: Sampling Variability"

    In a production environment, suppose you want to determine the **average lifetime of machines** in a factory. Machines vary in quality, maintenance schedules, and usage, so there will naturally be variability in how long they last. Instead of measuring just one machine’s lifetime, you collect data from several machines and calculate the average lifespan. However, if you only sample a few machines, the result might not accurately reflect the factory's overall performance. By sampling a larger number of machines and using statistical tools like confidence intervals, you get a more reliable estimate of the machines' average lifespan.

    In summary, understanding and managing **sampling variability** is key to making reliable and accurate conclusions in research. By taking multiple samples and applying statistical analysis, we can reduce the impact of variability and make better-informed decisions. Whether you are studying the age of workers, the lifespan of machines, or any other parameter, knowing how to handle variability is essential.

    Use the following dataset:
    ``` py
    from ucimlrepo import fetch_ucirepo 
    
    # fetch dataset 
    cars = fetch_ucirepo(id=9) 
    # https://archive.ics.uci.edu/dataset/9/auto+mpg
    
    # data (as pandas dataframes) 
    data = cars.data.features

    # Show the first 5 rows
    data.head()
    ```
    Work on the following task: 

    1. Analyze the correlation between the variables `horsepower` and `cylinders`. Therefore calculate the covariance, pearson correlation coefficient and spearman correlation coefficient. Interpret the results.
    2. Generate a scatter plot for the variabels `horsepower` and `cylinders`. Compare the before result with the calculated measures. 
    3. Take a closer look on the different variables and the corresponding attribute type. Is there a variable, where the calculation of the correlation makes no sense? 


XXXXXXXXXXXXXXXXXX


## Law of Large Numbers 

???+ example "Example: Coin Toss"

    For a random variable \( \bar{X} \), which represents the **arithmetic mean** after tossing a coin once, where heads is assigned a value of 1 and tails a value of 0, the result can be visualized in a histogram. Similarly, after five coin tosses, we can calculate the probability of various outcomes, such as:

    <iframe src="/assets/statistics/random_coin1.html" width="100%" height="400px"></iframe>

    ??? code "Code"
        ``` py
        import numpy as np
        import plotly.express as px
        import pandas as pd

        x = [0,1]

        df = pd.DataFrame(x, columns=['fair'])

        fig = px.histogram(df, x='fair', histnorm='probability density')

        # Adjust the plot
        fig.update_layout(
            title=dict(
                    text='<b><span style="font-size: 10pt">Flip a Coin</span></b>',
                ),
            xaxis_title_text='Arithmetic Mean',
            yaxis_title_text='Probability',
            bargap=0.1,
        )

        # Scale the axis
        fig.update_layout(yaxis_range=[0,0.5])

        # Show the plot
        fig.show()
        ```

    In the context of random variables, let's consider a situation where we toss a coin five times and examine the outcomes. The random variable \( \bar{X} \) represents the arithmetic mean after five coin tosses. We want to determine the probability of certain outcomes based on how many times heads or tails appear. For instance, the probability of getting no tails at all (meaning all heads, with an arithmetic mean of 0) after five tosses is:

    \[
    P(\bar{X} = 0) = P(00000) = \left(\frac{1}{2}\right)^5 = \frac{1}{32} = 0.03125
    \]

    Similarly, the probability of getting exactly one tail (and thus an arithmetic mean of 0.2) is:

    \[
    P(\bar{X} = 0.2) = 5 \cdot \frac{1}{32} = 0.15625
    \]

    The detailed breakdown of this calculation considers each specific sequence of outcomes where one tail appears, and each of these sequences has a probability of \( \frac{1}{32} \). Thus, the total probability is multiplied by the number of favorable outcomes, in this case, 5.

    Now, we can extend this example to calculate the probabilities for other outcomes. What is the probability of obtaining exactly 1, 2, 3, 4, or 5 tails, corresponding to arithmetic means of 0.2, 0.4, 0.6, 0.8, and 1, respectively?

    - The probability of no tails (mean = 0) is \( P(\bar{X} = 0) = \frac{1}{32} = 0.03125 \).
    - The probability of one tail (mean = 0.2) is \( P(\bar{X} = 0.2) = 5 \cdot \frac{1}{32} = 0.15625 \).
    - The probability of two tails (mean = 0.4) is \( P(\bar{X} = 0.4) = 10 \cdot \frac{1}{32} = 0.3125 \).
    - The probability of three tails (mean = 0.6) is \( P(\bar{X} = 0.6) = 10 \cdot \frac{1}{32} = 0.3125 \).
    - The probability of four tails (mean = 0.8) is \( P(\bar{X} = 0.8) = 5 \cdot \frac{1}{32} = 0.15625 \).
    - The probability of all tails (mean = 1) is \( P(\bar{X} = 1) = \frac{1}{32} = 0.03125 \).

    As the number of coin tosses increases, the distribution of outcomes starts to resemble a **binomial distribution**, which predicts the likelihood of each possible outcome over a large number of trials. For example, as the number of coin tosses grows, the shape of the probability distribution becomes smoother and more predictable.


    
xxxxxxxxxxxxxxx

As we increase the number of experiments, the distribution gradually transitions from a rough pattern to a smooth curve resembling the binomial distribution. This is illustrated through histograms showing how the distribution evolves as the number of coin tosses increases from one to 50,000. Initially, the distribution appears discrete, but with more trials, it takes the form of a continuous curve, following the binomial distribution closely.

By observing such patterns, we gain a deeper understanding of how random variables behave in large samples and how their probability distributions develop over time. This knowledge is fundamental to making accurate predictions in statistics and understanding the nature of random processes.

<div class="grid cards" markdown>
-    

    <iframe src="/assets/statistics/random_coin_1.html" width="100%" height="400px"></iframe>

-    

    <iframe src="/assets/statistics/random_coin_5.html" width="100%" height="400px"></iframe>

-    

    <iframe src="/assets/statistics/random_coin_50.html" width="100%" height="400px"></iframe>

-    

    <iframe src="/assets/statistics/random_coin_500.html" width="100%" height="400px"></iframe>

-    

    <iframe src="/assets/statistics/random_coin_5000.html" width="100%" height="400px"></iframe>

-    

    <iframe src="/assets/statistics/random_coin_50000.html" width="100%" height="400px"></iframe>

</div>

??? code "Code"
    ``` py 
    import numpy as np
    import matplotlib.pyplot as plt
    import plotly.express as px
    import pandas as pd


    def coin_flip_experiment(throws, repetitions):
        # List to store the mean values of each repetition
        mean_values = []
        
        for _ in range(repetitions):
            # Simulate coin flips (0 = heads, 1 = tails)
            flips = np.random.randint(0, 2, throws)
            # Calculate the mean value of the flips
            mean_value = np.mean(flips)
            # Store the mean value
            mean_values.append(mean_value)
        
        return mean_values

    # Parameters for the experiment
    throws = 50000  # Number of coin flips per repetition
    repetitions = 50000  # Number of times the experiment is repeated

    # Run the experiment and adjust format
    mean_values = coin_flip_experiment(throws, repetitions)
    mean_values = pd.DataFrame(mean_values, columns=['mean'])
    probs = mean_values.value_counts().reset_index(),
    probs = pd.DataFrame(probs[0])
    probs['count'] = probs['count']/repetitions

    # HISTOGRAM Large Number of Values
    # Generate Histogram
    fig = px.bar(
        probs,
        x='mean',
        y='count',
        )

    # Adjust the plot
    fig.update_layout(
        xaxis_title_text='Arithmethic Mean',
        yaxis_title_text='Probability',
        title=dict(
                text=f'<b><span style="font-size: 10pt">Probability: {throws} Coins </span><br> <span style="font-size:5">50.000 Flips</span></b>',
            ),
        #bargap=0.1,
        xaxis_range=[-0.5,1.5],
        showlegend=False,
    )
    fig.update_traces(marker=dict(color='#00416E', line=dict(color='#00416E', width=1)))

    # Show the plot
    fig.show()
    ```

# Recap

- Random variables are quantities that can take on different values.
- They assign numbers to each outcome of a random process.
- There is a distinction between discrete and continuous random variables.
- Each event has a certain probability associated with it.
- The representation of these probabilities is called a probability distribution.
- As the number of experiments increases, the distribution approaches a binomial distribution.


# Tasks
???+ question "Task"
    Consider a defective die with the following sides: \( [1, 1, 2, 3, 5, 6] \).
    Work on the following task: 

    1. Display the probabilities of each face of the die in a histogram.
    2. Conduct an experiment by rolling the die once using the `randint` function and plot the outcome in a histogram. How does the histogram change when you roll the die 10 times or 10,000 times? Interpret the results. Can you identify a binomial distribution?
    3. Now, introduce an average value. Roll the die 10 times and calculate the average number. Repeat this process 10,000 times and display the averages in a histogram.
    4. Increase the sample size from 10 to 1010 in increments of 100. Overlay the results in a histogram. Interpret the findings. Can you now identify a binomial distribution? 