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

## Probability vs. Proportion

Two concepts that students frequently mix up in statistics are **probability** and **proportion**.
Here’s the key distinction:

- **Probability** refers to the likelihood of an event occurring and is based on theoretical outcomes.
- **Proportion** reflects how often an event has actually occurred, relying on observed data.

In simpler terms, **probability** is typically used to discuss the likelihood of future events, while **proportion** is used to describe the frequency of events that have already happened. The following examples highlight the differences between these two concepts in various situations.

???+ example "Example: Flip a Coin"

    When flipping a fair coin, the **probability** of it landing on heads is 0.5, or 50%, which is based on theory. However, if we flip the coin 20 times, we can calculate the **proportion** of times it actually lands on heads. For instance, it might land on heads 40% of the time in those 20 flips.

    In this case, probability is a theoretical expectation, while proportion is based on real, observable outcomes that we can count.

???+ tip "Fun Fact: A Coin Toss is not 50/50"
    The term "coin toss" is often used as a symbol of randomness, but mathematicians have long suspected that even a fair coin has a slight tendency to land more often on one side. To investigate this bias, Ph.D. candidate František Bartoš gathered 47 volunteers who flipped coins over multiple weekends, eventually conducting 350,757 tosses. Their findings showed that coins landed with the same side facing upward as before the toss 50.8% of the time, confirming a small but significant bias in coin flips. (<cite>[Arxiv][2], [derStandard][3]</cite>)

[2]: https://arxiv.org/abs/2310.04153
[3]: https://www.derstandard.de/story/3000000191831/beim-muenzwurf-liegen-die-chancen-doch-nicht-genau-bei-50-zu-50


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

???+ defi "Definition"
    Probability of a specific outcome

    \[
    P(X = x) = \frac{\text{Number of favorable outcomes}}{\text{Total number of possible outcomes}}
    \]


## Probability Distribution
The **probability distribution** of a discrete random variable shows the likelihood of various outcomes occurring. While this distribution helps us understand the chances of different events, it doesn’t allow us to predict the result of any single experiment. However, if the experiment is repeated many times, the overall pattern becomes clearer, following predictable rules.

???+ example "Example: Biased Die"
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

    Consider a biased die with a manufacturing defect: it shows the number 6 twice and never shows the number 3. 

    <iframe src="/assets/statistics/random_dice_unfair.html" width="100%" height="400px"></iframe>

    ??? code "Code"
        ``` py
        import numpy as np
        import plotly.express as px
        import pandas as pd

        x = [1,2,4,5,6,6]

        df = pd.DataFrame(x, columns=['fair'])

        fig = px.histogram(df, x='fair', nbins=6, histnorm='probability density')

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


## Increasing Number of Experiments
