# Probability  

In this section we trasit from the exploration of descriptive statistics to the domain of inferential statistics. Inferential statistics plays an important role in interpreting data, making predictions, and drawing conclusions about broader populations based on sample data. At the heart of inferential statistics lies the concept of probability—an essential tool for calculating, interpreting, and applying likelihoods to real-world situations. This section delves into the fundamental principles of probability, providing a foundation for understanding the processes behind statistical inference and its practical applications.

## What is Probability? 

We'll begin by defining probability and exploring some common misconceptions. For now, let's start with a basic definition.

> Probability is the level of possibility of something happening or being true
>
> -- <cite>[Cambridge Dictionary][1]</cite>

[1]: https://dictionary.cambridge.org/us/dictionary/english/probability

The probability values range from 0 to 1, where 

- 0 indicates impossibility and 
- 1 represents certainty. 

A key point to note is that the sum of all probabilities for a set of outcomes must equal 1. In other words, the total likelihood of all possible outcomes must add up to certainty.

???+ example "Example: Rolling a Die"
    Imagine you are rolling a standard six-sided die. The die has six possible outcomes: 
    
    
    \[
    1, 2, 3, 4, 5, 6
    \]

    Each of these outcomes has an equal probability of occurring. The probability of rolling any specific number, say a 1, is 1 out of 6, or 
    
    \[
    P(X = 1) = 1/6.
    \]

    Now, if we sum the probabilities of all possible outcomes (rolling a 1, 2, 3, 4, 5, or 6), we get:

    \[
    P(X = 1) + P(X = 2) + \text{...} + P(X = 6) = \frac{1}{6} + \frac{1}{6} + \frac{1}{6} + \frac{1}{6} + \frac{1}{6} + \frac{1}{6} = 1
    \]

    This shows that the total probability of all possible outcomes equals 1, meaning that one of the six outcomes is certain to occur when you roll the die.


Let's make this concept more tangible by looking at an example from a common smartphone weather app. Imagine the app shows 

<figure markdown="span">
  ![Image title](/assets/statistics/rain.jpg){width=50% }
</figure>


"On Tuesday there is a 30% chance of rain." This statement can be interpreted in different ways:
Does it mean that it will rain for 30 percent of the day? Or that it will rain over 30 percent of the area at a given location? Or is there a 3 in 10 chance it will rain? 

The correct interpretation, however, is that there is a 3 in 10 chance of rain at any given point during the day. This aligns with how probability works - it's not about how long it will rain or the confidence level in the prediction, but the likelihood of rain occurring at all. We'll explore more examples like this to clarify these ideas as we move forward.

Why is probability so important? Probability plays a central role in fields like weather forecasting, actuarial science, and medical research. In medicine, for instance, probability is used to evaluate the effectiveness of treatments and to model the spread of diseases. It's also essential in physics, chemistry, biology, and even machine learning and artificial intelligence, where it helps make predictions based on data.

<figure markdown="span">
  ![Correlation Types](/assets/statistics/statisticsAI.png){width=50% }
  <figcaption>(Source: <a href="https://www.instagram.com/sandserifcomics">sandserifcomics</a>) </figcaption>
</figure>

We rely on probability whenever uncertainty (e.g. randomness) exists about the outcome of an event. For example, determining whether men are generally taller than women requires probability because it isn't universally true that all men are taller than all women. Similarly, probability helps assess the accuracy of medical tests, as even highly reliable tests can produce false positives. In contrast, for questions with known answers, such as the speed of light versus the speed of sound, probability isn't needed.

## Random Variables

A **random variable** differs slightly from traditional mathematical variables. In mathematics, variables can:

1. Represent values that may vary.
2. Act as unknowns to be solved.

For random variables, the first property holds, but the second does not. Random variables allow us to perform **calculations** with the outcomes of a **random experiment**, making it possible to model and work with uncertainty. They are typically represented by capital letters, and their specific values are denoted by lowercase letters.

???+ defi "Definition: Random Variable"
    A random variable is a function that assigns numbers to the outcomes of a random process (mapping).


For example, consider the result of rolling a die:

\[
X = \text{The number shown when a fair die is rolled}
\]

Or the result of flipping a coin:

\[
X = 
\begin{cases}
1, & \text{if heads} \\
0, & \text{if tails}
\end{cases}
\]

In both cases, the random variable maps the outcome of a random process to a numerical value. In the context of a coin flip:

- The **random process** is the coin flip itself.
- Each **experiment** refers to an individual flip.
- An **event** is the outcome, such as getting heads or tails.
- The **sample space** is the set of all possible outcomes (heads or tails).
- The **random variable** assigns a numerical value (e.g., 1 for heads, 0 for tails) to each event.

Thus, random variables enable us to quantify the outcomes of random processes, allowing for further analysis and interpretation.

???+ question "Task"
    Now it's your turn to create a random variable. There are several packages in Python that we can use for this purpose. Use the `random` package we already used in the package [management section](../../python/packages.md#standard-library). 

    <figure markdown="span">
    ![Correlation Types](../../assets/statistics/meme_dice.jpg){width=50% }
    <figcaption>(Source: <a href="https://imgflip.com/i/9599pd">imgflip</a>) </figcaption>
    </figure>

    1. Now generate your own random number. Use the commands `randint`, `random` and `choices`. A good documentation can be found [here](https://www.w3schools.com/python/module_random.asp)
    2. Are those numbers really random? Do some research about the `random.seed` command
    3. Now create the following experiments: 
        - **Fair Die**: Perform a virtual 'rolling of the die' for a fair (normal) die by using the `choices` command
            ```py
            die_fair = [1, 2, 3, 4, 5, 6]
            ```
        - **Biased Die**: Now use a biased die with no 3 but two times the side 6
            ```py
            die_biased = [1, 2, 4, 5, 6, 6]
            ```


## Probability vs. Proportion

Two concepts that students frequently mix up in statistics are **probability** and **proportion**.
Here’s the key distinction:

- **Probability** refers to the likelihood of an event occurring and is based on theoretical outcomes.
- **Proportion** reflects how often an event has actually occurred, relying on observed data.

In simpler terms, **probability** is typically used to discuss the likelihood of future events, while **proportion** is used to describe the frequency of events that have already happened. The following examples highlight the differences between these two concepts in various situations.

???+ example "Example: Flip a Coin"

    When flipping a fair coin, the **probability** of it landing on heads is 0.5, or 50%, which is based on theory. However, if we flip the coin 20 times, we can calculate the **proportion** of times it actually lands on heads. For instance, it might land on tails 40% of the time in those 20 flips. In this case, probability is a theoretical expectation, while proportion is based on real, observable outcomes that we can count.

    <iframe src="/assets/statistics/probability_proportion.html" width="100%" height="400px"></iframe>
    ??? code "Code"
        ``` py
        import random
        import plotly.express as px

        mylist = ["Heads", "Tails"]
        random.seed(23) # Set seed for reproducibility
        flips = random.choices(mylist, k=20)

        # Create a histogram
        fig = px.histogram(x=flips, nbins=2)

        # Change bar mode
        fig.update_traces(marker=dict(color='#00416E', line=dict(color='#00416E', width=0.5)))

        # Set overlay mode
        fig.update_layout(
            xaxis_title_text='Result',
            yaxis_title_text='Count',
            title=dict(
                    text=f'<b><span style="font-size: 10pt">Experiment: Flipping 20 Coins </span></b>',
                ),
            bargap=0.1,
            showlegend=False,)

        fig.show()
        ```

    

???+ tip "Fun Fact: A Coin Toss is not 50/50"
    The term "coin toss" is often used as a symbol of randomness, but mathematicians have long suspected that even a fair coin has a slight tendency to land more often on one side. To investigate this bias, Ph.D. candidate František Bartoš gathered 47 volunteers who flipped coins over multiple weekends, eventually conducting 350,757 tosses. Their findings showed that coins landed with the same side facing upward as before the toss 50.8% of the time, confirming a small but significant bias in coin flips. (<cite>[Arxiv][2], [derStandard][3]</cite>)

[2]: https://arxiv.org/abs/2310.04153
[3]: https://www.derstandard.de/story/3000000191831/beim-muenzwurf-liegen-die-chancen-doch-nicht-genau-bei-50-zu-50


???+ question "Task"
    Let's stick with the example from before and perform further experiments. We use a fair die and a biased die and perform the following task:  

    1. Roll each die 
        - 5 
        - 50  
        - 500 times. 
    2. Visualize the results in histogram (one for the fair die, one for the biased die). 

## Calculation of Probability

### Prerequisites

Before we start calculating probability, it's important to note that certain types (scales) of data (see section [Attribute Types](../../databasics/DataBasics.md#attribute-types)), such as **nominal** and **ordinal** are suitable for probability calculations, while interval and ratio scaled data are not directly valid for such computations. Interval and ratio data must first be converted into a **discrete scale** (like creating bins in a histogram) before probability can be applied, as their values have infinite precision, making them unsuitable for exact probability calculations.

???+ example "Example: Length of Wooden Beams"
    An example involving the length of wooden beams can illustrate this point. Asking for the probability of a beam being exactly a certain length, down to a microscopic precision, is not a practical question. Instead, engineers or builders focus on the probability of a beam’s length falling within a certain range, such as between 3.0 and 3.5 meters, or even within more precise intervals like 3.2 to 3.25 meters. This approach allows for meaningful analysis while accounting for slight variations in manufacturing or cutting processes.

Another key requirement for valid probability calculations is that the data categories must be mutually exclusive. For instance, when flipping a coin, the events "heads" and "tails" are mutually exclusive since both cannot happen at the same time. Similarly, if a wooden beam is measured to be between 3.5 and 4 m in length, it cannot also be between 4 and 4.5 m.

<figure markdown="span">
  ![Correlation Types](/assets/statistics/meme_mutually.jpg){width=50% }
  <figcaption>(Source: <a href="https://makeameme.org/meme/one-does-not-55c7e12c14">MakeAMeme</a>) </figcaption>
</figure>

However, some situations, like getting news from multiple sources, do not have mutually exclusive categories (a person can receive news from both TV and the internet). In such cases, probability cannot be computed unless the question is reformulated with exclusive categories.

### Calculation

For discrete random variables, each outcome of an experiment can be assigned a **probability**. The probability of a specific outcome \(X = x\) is calculated using the formula:

???+ defi "Definition: Probability"
    Probability of a specific outcome

    \[
    P(X = x) = \frac{\text{Number of favorable outcomes}}{\text{Total number of possible outcomes}}
    \]

The **probability distribution** of a discrete random variable shows the likelihood of various outcomes occurring. While this distribution helps us understand the chances of different events, it doesn’t allow us to predict the result of any single experiment. However, if the experiment is repeated many times, the overall pattern becomes clearer, following predictable rules.

???+ example "Example: Flip a Coin"

    <iframe src="/assets/statistics/probability_propprob.html" width="100%" height="400px"></iframe>
    ??? code "Code"
        ``` py
        import random
        import plotly.express as px

        mylist = ["Heads", "Tails"]
        random.seed(23) # Set seed for reproducibility
        flips = random.choices(mylist, k=20)

        # Create a histogram
        fig = px.histogram(x=flips, nbins=2, histnorm='probability')

        # Change bar mode
        fig.update_traces(marker=dict(color='#00416E', line=dict(color='#00416E', width=0.5)))

        # Set overlay mode
        fig.update_layout(
            xaxis_title_text='Result',
            yaxis_title_text='Probability/Proportion',
            title=dict(
                    text=f'<b><span style="font-size: 10pt">Experiment: Flipping 20 Coins </span></b>',
                ),
            bargap=0.1,

        for i in range(0, 2):
            fig.add_shape(
                type='line',
                x0=i-0.46,
                x1=i+0.46,
                y0=0.5,
                y1=0.5,
                line=dict(color='#E87F2B', width=5),
                xref='x',
                yref='y',
                name='Probability' if i == 0 else None,
                showlegend=(i == 0) 
            )
        fig.show()
        ```

???+ question "Task"
    We will continue with our example of the fair and biased die. 

    1. Calculate the probability for each side of the fair/biased die by using the `pandas` `value_counts` function
    2. Visualize the experiment from before in a histogram and overlay the calculated probabilty. Use the `plotly express` `add_shape` function.

## Odds

When dealing with probabilities, you'll often encounter the term **odds**. So, what does odds mean? It’s frequently used in everyday language, especially in fields like medicine and gambling. While probability and odds are related, they are not the same thing. This explanation will clarify the meaning of odds and show how they differ from probability, as well as how to convert between them.

Odds typically describe the ratio between two possibilities: the chance of something not happening compared to it happening. For example, when you hear "the odds are five to one," this means the odds ratio is 5:1, or 5 divided by 1. In mathematical terms, odds represent the ratio of the probability of an event not happening to the probability of it happening. It can be written as:


???+ defi "Definition: Odds"

    \[
    \text{Odds ratio (r)} = \frac{p}{1 - p}
    \]

    where $p$ is the probability of the event happening, and $1 - p$ is the probability of the event not happening. To convert odds into probability, you can solve for $p$ using the equation:

    \[
    p = \frac{r}{1 + r}
    \]

    where $r$ is the odds ratio. 

???+ example "Example: Flip a Coin"

    When flipping a fair coin, there are two possible outcomes: **heads** or **tails**. Each outcome has an equal chance of occurring. Understanding the concept of **odds** in this simple scenario can help clarify the difference between probability and odds.

    - **Probability of getting heads (P)**: \( \frac{1}{2} \) or 0.5 (50%)
    - **Probability of getting tails**: \( 1 - P = \frac{1}{2} \) or 0.5 (50%)

    **Calculating Odds:**

    \[
    \text{Odds in favor of heads} = \frac{P(\text{heads})}{P(\text{not heads})} = \frac{0.5}{0.5} = \frac{1}{1} = 1
    \]

    This means the odds in favor of getting heads are **1 to 1**, often written as **1:1**. This indicates an equal chance of getting heads or tails.


???+ question "Task"
    1. Calculate the odds for the fair die to roll 6
    2. Now calculate the same thing for the biased die

## Mass & Density Function

In statistics, we often encounter the concepts of **probability mass functions (PMF)** and **probability density functions (PDF)**. These functions help describe the probabilities of different types of events—whether they are discrete or continuous.

### Probability Mass Function (PMF)
A **probability mass function** is used to describe probabilities for **discrete events**. Discrete events are those that occur in distinct, countable states, such as flipping a coin, rolling a die, or drawing a card. For example, if we roll a die, each face (1, 2, 3, 4, 5, or 6) is a discrete event. A PMF assigns probabilities to each possible outcome. In this case, each side of a fair die has a probability of 1/6, and these probabilities are represented in a **bar plot or histogram**.

Let’s say we have a biased die, and the probability of rolling a 6 is twice as hig than other numbers and there is no 3. In this case, the PMF would show different probabilities for each number, but the probabilities are still discrete values—there’s no such thing as rolling a 4.5 on a die.

???+ example "Example: Rolling the Die"
    <div class="grid cards" markdown>

    -   __Fair Die__

        ---
        <iframe src="/assets/statistics/random_dice_fair.html" width="100%" height="400px"></iframe>

        ??? code "Code"
            ``` py
            import numpy as np
            import plotly.express as px
            import pandas as pd

            x = [1,2,3,4,5,6]

            df = pd.DataFrame(x, columns=['fair'])

            fig = px.histogram(df, x='fair', nbins=6, histnorm='probability density')

            # Adjust the plot
            fig.update_layout(
                title=dict(
                        text='<b><span style="font-size: 10pt">Rolling a Fair Die</span></b>',
                    ),
                xaxis_title_text='Number',
                yaxis_title_text='Probability',
                bargap=0.1,
            )

            # Scale the axis
            fig.update_layout(yaxis_range=[0,1])

            # Show the plot
            fig.show()
            ```

    -   __Biased Die__

        ---
        <iframe src="/assets/statistics/random_dice_unfair.html" width="100%" height="400px"></iframe>

        ??? code "Code"
            ``` py
            import numpy as np
            import plotly.express as px
            import pandas as pd

            x = [1,2,4,5,6,6]

            df = pd.DataFrame(x, columns=['unfair'])

            fig = px.histogram(df, x='unfair', nbins=6, histnorm='probability density')

            # Adjust the plot
            fig.update_layout(
                title=dict(
                        text='<b><span style="font-size: 10pt">Rolling a Biased Die</span></b>',
                    ),
                xaxis_title_text='Number',
                yaxis_title_text='Probability',
                bargap=0.1,
            )

            # Scale the axis
            fig.update_layout(yaxis_range=[0,1])

            # Show the plot
            fig.show()
            ```
    </div>

    **For the Biased Die**

    The probability of rolling a 6 would be:

    \[
    P(X = 6) = \frac{2}{6} = 33.3\%
    \]

    Similarly, the probability of rolling a number greater than 4 would be:

    \[
    P(X > 4) = \frac{3}{6} = 50\%
    \]

    The probability of rolling a number between 1 and 4 is:

    \[
    P(1 < X < 4) = \frac{1}{6} = 16.7\%
    \]

One key rule of PMFs is that the sum of all probabilities must equal 1. For example, in a deck of cards, the sum of the probabilities for drawing any card must equal 1, since you're certain to draw **some** card from the deck.

### Probability Density Function (PDF)
In contrast, a **probability density function** is used for **continuous events**. Continuous events don’t have discrete outcomes; instead, they can take on any value within a range. For example, if we’re measuring the height of a person, we can’t pinpoint an exact value (down to the atom). Instead, we look at the probability of the height falling within a range, such as between 180 cm and 190 cm. Unlike PMFs, PDFs are represented by smooth curves, showing how the probability is distributed over a range of values.

With continuous data, we can’t assign a probability to a specific value (such as someone being exactly 165.432 cm tall). Instead, we compute the probability of a value falling within a range using the **area under the curve** of the PDF. For instance, we might ask, "What’s the probability that someone’s height is between 180 cm and 190 cm?" This probability is calculated by integrating the PDF over that range.

???+ example "Example: Height of a Person"
    <iframe src="/assets/statistics/probability_pdf.html" width="100%" height="400px"></iframe>

    ??? code "Code"
        ``` py
        import numpy as np
        import pandas as pd
        import plotly.express as px
        from scipy.stats import norm

        # Initialization
        limit_up = 190
        limit_down = 180

        # Generate data for the normal distribution
        x = np.arange(130, 210, 0.1)
        y = norm.pdf(x, 170, 10)
        df = pd.DataFrame({'x': x, 'y': y})

        # Create a column for the fill area
        df['fill'] = np.where((df['x'] >= limit_down) & (df['x'] <= limit_up), df['y'], 0)


        # Create the plot
        fig = px.line(df, x='x', y='y')
        fig.add_trace(px.line(df, x='x', y='fill').data[0])

        # Adjust the plot
        fig.data[0].update(line=dict(color='#00416E', width=2))

        fig.data[1].update(
            fill='tozeroy', 
            fillcolor='rgba(0, 65, 110, 0.4)',
            line=dict(width=0),)

        fig.update_layout(
            xaxis_title_text='x',
            yaxis_title_text='Density',
            title=dict(
                    text=f'<b><span style="font-size: 10pt">Probability Density Function </span><br> <span style="font-size:5">µ=170cm, std=10cm</span> </b>',
                ),
            showlegend=False,
        )

        fig.show()
        ```

    Calculating the probability, that a person is between 180 and 190 cm:

    \[
    P(180 \le X \le 190) = \int_{180}^{190} f(X)dx
    \]

    or smaller than 150 cm:

    \[
    P(X \le 150) = \int_{-\infty}^{150} f(X)dx
    \]

### Cumulative Distribution Function (CDF)

A **CDF** is a function that provides the cumulative probability for a given random variable. In simpler terms, it gives the probability that a random variable will take a value **less than or equal to** a specific point. To build a CDF from a PDF, you essentially **sum** all the probability values of the PDF **up to a certain point** on the x-axis. Mathematically, this is equivalent to calculating the **integral** of the PDF for continuous distributions. The CDF at a particular value \( x \) gives you the total probability of the random variable being less than or equal to \( x \).

For example, imagine a probability density function that describes the heights of people in a population. The CDF at a specific height (say 150 cm) tells you the probability of randomly selecting someone who is 150 cm or shorter. As you move further along the x-axis, the CDF will continue to increase until it reaches 1, which represents 100% probability.

???+ example "Example: Height of a Person"
    <iframe src="/assets/statistics/probability_cdf.html" width="100%" height="400px"></iframe>

    ??? code "Code"
        ``` py
        import numpy as np
        import pandas as pd
        import plotly.express as px
        from scipy.stats import norm

        # Initialization
        limit_up = 190
        limit_down = 180

        # Generate data for the normal distribution
        x = np.arange(130, 210, 0.1)
        y = norm.cdf(x, 170, 10)
        df = pd.DataFrame({'x': x, 'y': y})

        # Create a column for the fill area
        df['fill'] = np.where((df['x'] >= limit_down) & (df['x'] <= limit_up), df['y'], 0)


        # Create the plot
        fig = px.line(df, x='x', y='y')
        fig.add_trace(px.line(df, x='x', y='fill').data[0])

        # Adjust the plot
        fig.data[0].update(line=dict(color='#00416E', width=2))

        fig.data[1].update(
            fill='tozeroy', 
            fillcolor='rgba(0, 65, 110, 0.4)',
            line=dict(width=0),)

        fig.update_layout(
            xaxis_title_text='x',
            yaxis_title_text='Probability',
            title=dict(
                    text=f'<b><span style="font-size: 10pt">Cumulated Distribution Function </span><br> <span style="font-size:5">µ=170cm, std=10cm</span> </b>',
                ),
            showlegend=False,
        )

        fig.show()
        ```

    Calculating the probability, that a person is between 180 and 190 cm:

    \[
    P(180 \le X \le 190) = \int_{180}^{190} f(X)dx = 13.6\%
    \]

    or smaller than 150 cm:

    \[
    P(X \le 150) = \int_{-\infty}^{150} f(X)dx = 2.3\%
    \]

    ??? code "Code"
        ``` py
        print('Between 180cm and 190cm:', (norm.cdf(190, 170, 10) - norm.cdf(180, 170, 10))*100, '%')
        print('Smaller than 150cm:', (norm.cdf(150, 170, 10))*100, '%')
        ```


Key Properties of CDFs:

1. **CDFs start at 0**: The lowest x-value in the distribution will have a cumulative probability of 0.
2. **CDFs increase monotonically**: As you move along the x-axis, the CDF always increases or stays the same. It never decreases, since probabilities cannot decrease over time.
3. **CDFs approach 1**: As the x-values increase and encompass all possible outcomes, the cumulative probability approaches 1, representing 100%.


While PDFs describe the probability density, CDFs are the **cumulative sum** of those probabilities. One important distinction is that summing all the values of a **PDF** equals 1 (as it represents the total probability), but summing all the values of a **CDF** does not necessarily give 1. Instead, the CDF gradually approaches 1 as the x-values increase.

CDFs provide a powerful way to compute cumulative probabilities, especially when working with continuous distributions. By understanding the relationship between PDFs and CDFs, we can answer practical questions like "What is the probability of scoring above a certain value?" or "What is the probability of a variable falling within a specific range?"

In practical terms, CDFs allow you to compute probabilities **up to a certain value** on the x-axis, making them essential tools in statistics, probability theory, and real-world applications like exam scores or analyzing biological data.

???+ question "Task"
    Assume the heights of individuals in a certain population follow a normal distribution with a mean of 170 cm and a standard deviation of 10 cm (see examples above).

    Answer the following questions based on this normal distribution:

    1. What percentage of individuals are taller than 190 cm?
    2. What percentage of individuals are between 170 cm and 180 cm tall?
    3. Plot the Probability Density Function (PDF) for a normal distribution with a mean of 180 cm and a standard deviation of 5 cm.

    For the first two questions use the **Cumulative Distribution Function (CDF)** to calculate the corresponding probabilities.
