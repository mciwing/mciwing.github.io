# Linear Regression


In many cases, simply characterizing the data is not sufficient. Beyond explaining the data, the goal is often to enable predictions. This chapter introduces the basic approach of **linear regression**, which allows for approximating **bivariate** data. The topics covered include linear regression and the coefficient of determination. Regression aims to model the relationships between a dependent variable and one or more independent variables.

## Motivation

To understand the motivation behind linear regression we will start this chapter with an example. Consider a mobile plan that costs €26, including unlimited SMS, calls, and data within the country. Data roaming costs €0.84 per MB. The bills for the last year show monthly expenses based on roaming usage.

| Month       | Roaming [MB] | Bill [€] || Month       | Roaming [MB] | Bill [€] |
|-------------|:---------------:|:----------:||-------------|:---------------:|:----------:|
| January     | 25            | 47.00    || July        | 125           | 131.00   |
| February    | 300           | 278.00   || August      | 62            | 78.08    |
| March       | 258           | 242.72   || September   | 94            | 104.96   |
| April       | 135           | 139.40   || October     | 381           | 346.04   |
| May         | 12            | 36.08    || November    | 12            | 36.08    |
| June        | 0             | 26.00    || December    | 18            | 41.12    |

<iframe src="/assets/statistics/regression_roaming.html" width="100%" height="400px"></iframe>

??? code "Code"
    ``` py
    import pandas as pd
    import numpy as np
    from sklearn.linear_model import LinearRegression
    import plotly.express as px

    # Create a DataFrame
    df = pd.DataFrame([(25, 47.00), (300, 278.00), (258, 242.72), (135, 139.40), (12, 36.08), 
                    (0, 26.00), (125, 131.00), (62, 78.08), (94, 104.96), 
                    (381, 346.04), (12, 36.08), (18, 41.12)], 
                    columns=['Roaming', 'Price'])

    # Linear Regression
    model = LinearRegression()
    model.fit(df[['Roaming']], df['Price'])

    intercept = model.intercept_
    slope = model.coef_[0]
    r_sq = model.score(df[['Roaming']], df['Price'])

    # Generate regression line
    df['Regression Line'] = intercept + slope * df['Roaming']

    # Create Plotly Express figure
    fig = px.scatter(df, x='Roaming', y='Price')
    fig['data'][0]['marker'] = {'color':'red', 'size':10}

    # Add regression line
    fig.add_traces(px.line(df, x='Roaming', y='Regression Line').data)

    # Adjust the plot
    fig.update_layout(
        xaxis_title_text='Roaming [MB]',
        yaxis_title_text='Price [€]',
        title=dict(
                text='<b><span style="font-size: 10pt">Smartphone Bill</span> <br> <span style="font-size:5">Variables: roaming, price</span></b>',
            ),
    )

    # Show the plot
    fig.show()
    ```

A scatter plot of the data reveals a **perfect linear relationship**, allowing us to describe the relationship with a linear function:

\[
y = 26 + 0.84 \cdot x
\]

This has several advantages. For one, the bill amount can be **explained** through fixed and variable costs, specifically showing how the MB usage affects the total cost. Additionally, it allows for **predictions** of the bill amount for any unobserved amount of MB.

However, in reality, most relationships are not perfectly linear. Let's consider two samples, each with variables \(X\) and \(Y\).

| \(X_1\) | \(Y_1\) || \(X_2\) | \(Y_2\) |
|:---------:|:---------:||:---------:|:---------:|
| 0.00    | 0.23    || 0.14    | 2.00    |
| 0.12    | 0.31    || 0.25    | 2.41    |
| 0.18    | 0.49    || 0.18    | 2.69    |
| 0.26    | 1.11    || 0.27    | 3.41    |
| 0.40    | 1.03    || 0.42    | 3.43    |
| 0.51    | 1.32    || 0.50    | 3.82    |
| 0.60    | 1.58    || 0.62    | 4.18    |
| 0.68    | 1.66    || 0.70    | 4.36    |
| 0.80    | 1.65    || 0.79    | 4.45    |
| 0.80    | 1.85    || 0.85    | 4.75    |
| 0.99    | 1.69    || 1.00    | 4.69    |

When analyzing these samples, we find:

- Sample 1 has a Pearson correlation coefficient of \( \rho_1 = 0.938 \).
- Sample 2 has a Pearson correlation coefficient of \( \rho_2 = 0.942 \).

These values are very similar and suggest a strong correlation.

<div class="grid cards" markdown>

-   

    <iframe src="/assets/statistics/regression_scatter_unscale1.html" width="100%" height="400px"></iframe>

-  

    <iframe src="/assets/statistics/regression_scatter_unscale2.html" width="100%" height="400px"></iframe>

</div>

??? code "Code"
    ``` py
    import pandas as pd
    import plotly.express as px

    x1 = [0.00, 0.12, 0.18, 0.26, 0.40, 0.51, 0.60, 0.68, 0.80, 0.80, 0.99]
    y1 = [0.23, 0.31, 0.49, 1.11, 1.03, 1.32, 1.58, 1.66, 1.65, 1.85, 1.69]

    x2 = [0.14, 0.25, 0.18, 0.27, 0.42, 0.50, 0.62, 0.70, 0.79, 0.85, 1.00]
    y2 = [2.00, 2.41, 2.69, 3.41, 3.43, 3.82, 4.18, 4.36, 4.45, 4.75, 4.69]

    df = pd.DataFrame({'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2})


    # Create Plotly Express figure
    fig = px.scatter(df, x='x1', y='y1')

    # Adjust the plot
    fig.update_layout(
        xaxis_title_text='x1',
        yaxis_title_text='y1',
        title=dict(
                text='<b><span style="font-size: 10pt">Dataset 1</span></b>',
            ),
    )

    # Show the plot
    fig.show()


    # Create Plotly Express figure
    fig2 = px.scatter(df, x='x2', y='y2')

    # Adjust the plot
    fig2.update_layout(
        xaxis_title_text='x2',
        yaxis_title_text='y2',
        title=dict(
                text='<b><span style="font-size: 10pt">Dataset 2</span></b>',
            ),
    )

    # Show the plot
    fig2.show()
    ```


At first glance, a scatter plot supports this conclusion, but the impression changes when the axes are normalized equally. 

<div class="grid cards" markdown>

-   

    <iframe src="/assets/statistics/regression_scatter_scale1.html" width="100%" height="400px"></iframe>

-  

    <iframe src="/assets/statistics/regression_scatter_scale2.html" width="100%" height="400px"></iframe>

</div>

??? code "Code"
    ``` py
    import pandas as pd
    import plotly.express as px

    x1 = [0.00, 0.12, 0.18, 0.26, 0.40, 0.51, 0.60, 0.68, 0.80, 0.80, 0.99]
    y1 = [0.23, 0.31, 0.49, 1.11, 1.03, 1.32, 1.58, 1.66, 1.65, 1.85, 1.69]

    x2 = [0.14, 0.25, 0.18, 0.27, 0.42, 0.50, 0.62, 0.70, 0.79, 0.85, 1.00]
    y2 = [2.00, 2.41, 2.69, 3.41, 3.43, 3.82, 4.18, 4.36, 4.45, 4.75, 4.69]

    df = pd.DataFrame({'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2})


    # Create Plotly Express figure
    fig = px.scatter(df, x='x1', y='y1')

    # Adjust the plot
    fig.update_layout(
        xaxis_title_text='x1',
        yaxis_title_text='y1',
        title=dict(
                text='<b><span style="font-size: 10pt">Dataset 1</span></b>',
            ),
    )

    fig.update_layout(yaxis_range=[0,6])

    # Show the plot
    fig.show()
    fig.write_html("outputpic/regression_scatter_unscale1.html", full_html=False, include_plotlyjs='cdn')


    # Create Plotly Express figure
    fig2 = px.scatter(df, x='x2', y='y2')

    # Adjust the plot
    fig2.update_layout(
        xaxis_title_text='x2',
        yaxis_title_text='y2',
        title=dict(
                text='<b><span style="font-size: 10pt">Dataset 2</span></b>',
            ),
    )

    fig2.update_layout(yaxis_range=[0,6])

    # Show the plot
    fig2.show()
    ```

Proper scaling reveals:

1. For every \(X\) value, the corresponding \(Y\) value in Sample 2 is consistently larger than in Sample 1.
2. The change in \(Y\) is more significant in Sample 2 compared to Sample 1 when \(X\) changes.


This phenomenon occurs because we intuitively focus on the **overall picture** and draw a mental line through the points. The question then arises: how do we determine this line? This leads us into the core of linear regression, where we aim to model the relationship between variables and make informed predictions.

<div class="grid cards" markdown>

-   

    <iframe src="/assets/statistics/regression_scatter_scale_fit1.html" width="100%" height="400px"></iframe>

-  

    <iframe src="/assets/statistics/regression_scatter_scale_fit2.html" width="100%" height="400px"></iframe>

</div>

??? code "Code"
    ``` py
    import pandas as pd
    import numpy as np
    from sklearn.linear_model import LinearRegression
    import plotly.express as px

    x1 = [0.00, 0.12, 0.18, 0.26, 0.40, 0.51, 0.60, 0.68, 0.80, 0.80, 0.99]
    y1 = [0.23, 0.31, 0.49, 1.11, 1.03, 1.32, 1.58, 1.66, 1.65, 1.85, 1.69]

    x2 = [0.14, 0.25, 0.18, 0.27, 0.42, 0.50, 0.62, 0.70, 0.79, 0.85, 1.00]
    y2 = [2.00, 2.41, 2.69, 3.41, 3.43, 3.82, 4.18, 4.36, 4.45, 4.75, 4.69]

    df = pd.DataFrame({'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2})

    # Linear Regression Sample 1
    model1 = LinearRegression()
    model1.fit(df[['x1']], df['y1'])
    intercept1 = model1.intercept_
    slope1 = model1.coef_[0]
    df['y1_hat'] = intercept1 + slope1 * df['x1']

    # Linear Regression Sample 2
    model2 = LinearRegression()
    model2.fit(df[['x2']], df['y2'])
    intercept2 = model2.intercept_
    slope2 = model2.coef_[0]
    df['y2_hat'] = intercept2 + slope2 * df['x2']

    # Create Plotly Express figure
    fig = px.scatter(df, x='x1', y='y1')
    fig['data'][0]['marker'] = {'color':'red', 'size':10}

    # Add regression line
    fig.add_traces(px.line(df, x='x1', y='y1_hat').data)

    # Adjust the plot
    fig.update_layout(
        xaxis_title_text='x1',
        yaxis_title_text='y1',
        title=dict(
                text='<b><span style="font-size: 10pt">Sample 1</span></b>',
            ),
    )

    fig.update_layout(yaxis_range=[0,6])

    # Show the plot
    fig.show()


    # Create Plotly Express figure
    fig2 = px.scatter(df, x='x2', y='y2')
    fig2['data'][0]['marker'] = {'color':'red', 'size':10}

    # Add regression line
    fig2.add_traces(px.line(df, x='x2', y='y2_hat').data)

    # Adjust the plot
    fig2.update_layout(
        xaxis_title_text='x2',
        yaxis_title_text='y2',
        title=dict(
                text='<b><span style="font-size: 10pt">Sample 2</span></b>',
            ),
    )

    fig2.update_layout(yaxis_range=[0,6])

    # Show the plot
    fig2.show()
    ```




## Linear Regression

In linear regression, the relationship between variables is not exactly described. To account for this, a **random error** \( e_i \) is added. 

???+ defi "Definition"
    Approximation of the real values \( y_i \)

    \[
    y_i = \hat{y}_i + e_i
    \]

    With the linear regression

    \[
    \hat{y}_i = a + b \cdot x_i
    \]


The goal of linear regression is to find the **best fit line** by solving a minimization problem. This problem minimizes the sum of the squared residuals, expressed as

???+ defi "Definition"
    Minimization problem for fitting the linear regression

    \[
    \min_{a,b} \sum_{i=1}^{n}e_i^2 = \min_{a,b} \sum_{i=1}^{n}(y_i-\hat{y}_i)^2= \min_{a,b} \sum_{i=1}^{n}(y_i-a-bx_i)^2
    \]



By solving this, the **coefficients of the regression line** can be determined, with

???+ defi "Definition"
    Intercept

    \[
    a = \bar{y} - b \bar{x}
    \]

    Slope

    \[
    b = \frac{\text{cov}(X, Y)}{\sigma_x^2}
    \]


The best fit line is the one that minimizes the sum of squared differences between observed and predicted values. These differences, known as residuals, represent the distance between the actual \( Y \)-values and the predicted \( Y \)-values from the model.

<figure markdown="span">
  ![Correlation Types](/assets/statistics/Regression.svg){ width="400" }
</figure>

## Coefficient of Determination

To evaluate the **goodness of fit** of a model, the coefficient of determination \( R^2 \) can be used. It is calculated as:

???+ defi "Definition"
    Coefficient of Determination

    \[
    R^2 = \frac{\sum_{i=1}^{n}(\hat{y}_i - \bar{y})^2}{\sum_{i=1}^{n}(y_i - \bar{y})^2} = \rho_{X,Y}^2
    \]

The coefficient of determination indicates the proportion of variance explained by the model. In essence, \( R^2 \) measures how well the regression model fits the observed data.

\( R^2 \) can range from zero to one:

- \( R^2 = 0 \):  
  **None of the variance is explained** by the model, indicating a poor fit.

- \( R^2 = 1 \):  
  **All of the variance is explained** by the regression, indicating a perfect fit, which can only occur when the original data points lie exactly on the regression line.


## Recap

- Linear regression attempts to model the relationship between multiple variables.
- Using the model, further values can be predicted.
- In linear regression, the squared distance between the raw data points and the regression line is minimized.
- The coefficient of determination \(R^2\) is used to assess the model's goodness of fit.
- The closer the \(R^2\) value is to one, the better the model fits the data.


## Tasks
???+ question "Task"
    Use the following dataset:
    ``` py
    from ucimlrepo import fetch_ucirepo 
    
    # fetch dataset 
    cars = fetch_ucirepo(id=9) 
    # https://archive.ics.uci.edu/dataset/9/auto+mpg
    
    # data (as pandas dataframes) 
    data = cars.data.features
    data = data.join(cars.data.ids)

    # Show the first 5 rows
    data.head()
    ```
    Work on the following task: 

    1. Perform a linear regression for the following attribute combinations: 
        - Displacement vs. Weight
        - Displacement vs. Acceleration
        - Acceleration vs. Weight
    2. For all performed regressions calculate the coefficient of determination
    3. Write down the formula for all performed regressions 