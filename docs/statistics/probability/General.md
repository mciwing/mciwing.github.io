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

We rely on probability whenever uncertainty exists about the outcome of an event. For example, determining whether men are generally taller than women requires probability because it isn't universally true that all men are taller than all women. Similarly, probability helps assess the accuracy of medical tests, as even highly reliable tests can produce false positives. In contrast, for questions with known answers, such as the speed of light versus the speed of sound, probability isn't needed.

### Probability vs. Proportion

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



