# Law of Large Numbers

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