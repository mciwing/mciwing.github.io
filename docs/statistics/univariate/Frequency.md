# Frequency Distribution

A list \( X \) consists of \( n \) elements \( x_1, \dots, x_n \). Within this list, \( X \) contains \( k \) distinct values (\( a_1, \dots, a_k \)). The **frequency** refers to how often a specific value \( a_k \) appears in \( X \). 


```py 
drinks = ['small', 'small', 'small', 'medium', 'medium', 'medium', 'large']
```

In this example, 

- \( X \): `#!python drinks`
- \( n \): `#!python 7`
- \( x_1, \dots, x_n \): `#!python ['small', 'small', 'small', 'medium', 'medium', 'medium', 'large']`
- \( k \): 3
- \( a_1, \dots, a_k \): `#!python ['small', 'medium', 'large']`

In the case of a nominal scale, \( k \) is equal to the number of categories, with \( k \) typically much smaller than \( n \). For a metric scale, there are often only a few identical values, meaning \( k \) is approximately equal to \( n \).

The **representation of frequencies** can be done in the form of a **table** or a **graphical** format. When a frequency distribution is depicted as a bar chart, it is referred to as a histogram. 

```py 
import plotly.express as px

df = px.data.tips()
fig = px.histogram(df, x="total_bill")
fig.show()
```

It is important that the data remains the focal point and is presented as accurately and objectively as possible, avoiding distortions such as 3D effects or shadows. Titles, axis labels, legends, the data source, and the time of data collection should always be clearly indicated.

???+ defi "Definition"
    **Absolute Frequency** of the value \( a_j \)
    
    \[
    h(a_j) = h_j
    \]

    **Relative Frequency** of the value \( a_j \)

    \[
    f(a_j) = f_j = \frac{h_j}{n}
    \]

    **Absolute Frequency Distribution**: \( h_1, \dots, h_k \)

    **Relative Frequency Distribution**: \( f_1, \dots, f_k \)


???+ code "Code"
    For the upcoming analysis, the following data will be used: 
        ``` py
        # Import Libraries
        import pandas as pd
        
        # Import Data
        data = pd.read_csv('https://raw.githubusercontent.com/JeffSackmann/tennis_atp/master/atp_matches_2023.csv')
        ```
        

## Nominal Scale
For nominally scaled variables, the values correspond to the possible categories. The internal order of these categories is not relevant in the substantive analysis.

???+ example
    <div class="grid cards" markdown>

    -   

        <iframe src="/assets/statistics/uni_nominal_histo.html" width="100%" height="400px"></iframe>
        ??? code "Code"
            ``` py
            import plotly.express as px

            # Generate Histogram
            fig = px.histogram(
                data, 
                x="surface",
            )

            # Adjust the plot
            fig.update_layout(
                xaxis_title_text='Surface',
                yaxis_title_text='Absolute Frequency',
                title=dict(
                        text='<b><span style="font-size: 10pt">Nominal Variable: Histogram</span> <br> <span style="font-size:5">Data: atp_matches_2023.csv; variable: surface</span></b>',
                    ),
            )

            # Show the plot
            fig.show()
            ```

    -   

        <iframe src="/assets/statistics/uni_nominal_pie.html" width="100%" height="400px"></iframe>
        ??? code "Code"
            ``` py 
            import plotly.express as px

            # Generate Pie Chart
            fig = px.pie(
                data,
                names="surface",
            )

            # Adjust the plot
            fig.update_layout(
                title=dict(
                        text='<b><span style="font-size: 10pt">Nominal Variable: Pie Chart</span> <br> <span style="font-size:5">Data: atp_matches_2023.csv; variable: surface</span></b>',
                    ),
            )
            fig.update_traces(textposition='outside', textinfo='percent+label')

            # Show the plot
            fig.show()
            ```
    </div>

## Ordinal Scale
For ordinally scaled variables, the values also correspond to the possible categories. However, the internal order of these categories is relevant in the substantive analysis. The values should always be presented in either ascending or descending order.
In order to tell `Python` the correct order, we need to define it first

```py 
round_order = ['F', 'SF', 'QF', 'R16', 'R32', 'R64', 'R128', 'RR']
```

Afterwards we can use this order in the histogram
```py 
fig = px.histogram(
                data, 
                x="round",
                category_orders={"round": round_order}
                )
```

and for the calculation of the corsstable
```py 
data['round'] = pd.Categorical(data['round'], categories=round_order, ordered=True)
```
            

???+ example
    <div class="grid cards" markdown>

    -   __Histogram WITHOUT Order__

        ---
        <iframe src="/assets/statistics/uni_ordinal_histo_unsort.html" width="100%" height="400px"></iframe>
        ??? code "Code"
            ``` py
            import plotly.express as px

            # Generate Histogram
            fig = px.histogram(
                data, 
                x="round",
            )
            # Adjust the plot
            fig.update_layout(
                title=dict(
                        text='<b><span style="font-size: 10pt">Ordinal Variable: NO Order</span> <br> <span style="font-size:5">Data: atp_matches_2023.csv; variable: round</span></b>',
                    ),
                xaxis_title_text='Round',
                yaxis_title_text='Absolute Frequency',
            )
            # Show the plot
            fig.show()
            ```

    -   __Histogram WITH Order__

        ---
        <iframe src="/assets/statistics/uni_ordinal_histo_sort.html" width="100%" height="400px"></iframe>
        ??? code "Code"
            ``` py
            import plotly.express as px

            # Define the order of the ordinal variable
            data_ord = data.copy()
            round_order = ['F', 'SF', 'QF', 'R16', 'R32', 'R64', 'R128', 'RR']  # Define order of the rounds

            # HISTOGRAM sorted
            # Generate Histogram
            fig = px.histogram(
                data_ord, 
                x="round",
                category_orders={"round": round_order[::-1]},
            )

            # Adjust the plot
            fig.update_layout(
                title=dict(
                        text='<b><span style="font-size: 10pt">Ordinal Variable: WITH Order</span> <br> <span style="font-size:5">Data: atp_matches_2023.csv; variable: round</span></b>',
                    ),
                xaxis_title_text='Round',
                yaxis_title_text='Absolute Frequency',
            )

            # Show the plot
            fig.show()
            ```

    -   __Table WITHOUT Order__

        ---
        | round   |   Absoulte Frequency  |   Relative Frequency [%]  |
        |:--------|:---------------------:|:-------------------------:|
        | F       |                   68  |                  2.278    |
        | QF      |                  256  |                  8.57     |
        | R128    |                  416  |                 13.93     |
        | R16     |                  512  |                 17.15     |
        | R32     |                  880  |                 29.47     |
        | R64     |                  432  |                 14.47     |
        | RR      |                  286  |                  9.58     |
        | SF      |                  136  |                  4.55     |
        ??? code "Code"
            ``` py
            # FREQUENCY TABLE unsorted
            # Generate table with absolute and relative frequencies
            absolutefrequency_ord_unsort = pd.crosstab(index=data['round'], columns='Absoulte Frequency')
            relativefrequency_ord_unsort = pd.crosstab(index=data['round'], columns='Relative Frequency [%]',normalize=True)*100

            # Combine the tables
            frequencytable_ord_unsort = pd.concat([absolutefrequency_ord_unsort, relativefrequency_ord_unsort], axis=1).reset_index()
            frequencytable_ord_unsort.columns.name = None

            # Show table
            print(frequencytable_ord_unsort)
            ```

    -   __Table WITH Order__

        ---
        | Round   |   Absoulte Frequency  |   Relative Frequency [%]  |
        |:--------|:---------------------:|:-------------------------:|
        | F       |                   68  |                  2.28     |
        | SF      |                  136  |                  4.55     |
        | QF      |                  256  |                  8.57     |
        | R16     |                  512  |                 17.15     |
        | R32     |                  880  |                 29.47     |
        | R64     |                  432  |                 14.47     |
        | R128    |                  416  |                 13.93     |
        | RR      |                  286  |                  9.58     |
        ??? code "Code"
            ``` py
            # FREQUENCY TABLE sorte
            round_order = ['F', 'SF', 'QF', 'R16', 'R32', 'R64', 'R128', 'RR']  # Define order of the roundsd
            data['round'] = pd.Categorical(data['round'], categories=round_order, ordered=True)  # Define order of the rounds

            # Generate table with absolute and relative frequencies
            absolutefrequency_ord_sort = pd.crosstab(index=data['round'], columns='Absoulte Frequency')
            relativefrequency_ord_sort = pd.crosstab(index=data['round'], columns='Relative Frequency [%]',normalize=True)*100

            # Combine the tables
            frequencytable_ord_sort = pd.concat([absolutefrequency_ord_sort, relativefrequency_ord_sort], axis=1).reset_index()
            frequencytable_ord_sort.columns.name = None

            # Show table
            print(frequencytable_ord_sort)
            ```
    </div>

In the case of ordinally scaled variables, a cumulative absolute or relative frequency can also be calculated. The cumulative absolute frequency indicates how often a reference value (or category) has not been exceeded. The cumulative relative frequency is this number divided by the total number of observations.

To calculate the cumulative relative frequency in the histogram, we need to add the lines: 
```py hl_lines="5-6"
fig = px.histogram(
                data, 
                x="round",
                category_orders={"round": round_order[::-1]},
                cumulative=True,
                histnorm="percent"
                )
```
To do the same for the crosstab we need to add:

```py hl_lines="4-5"
freq_rel_cum = pd.crosstab(
                index=data['round'], 
                columns='Relative Frequency',
                normalize=True
                ).cumsum()
```

???+ example
    <div class="grid cards" markdown>

    -   __Histogram (Abolute, Cumulative)__

        ---
        <iframe src="/assets/statistics/uni_ordinal_histo_sort_abs_cum.html" width="100%" height="400px"></iframe>
        ??? code "Code"
            ``` py
            import plotly.express as px

            # HISTOGRAM sorted Cumulative Absolute
            round_order = ['F', 'SF', 'QF', 'R16', 'R32', 'R64', 'R128', 'RR']  # Define order of the roundsd
            data['round'] = pd.Categorical(data['round'], categories=round_order, ordered=True)  # Define order of the rounds

            # Generate Histogram
            fig = px.histogram(
                data, 
                x="round",
                category_orders={"round": round_order[::-1]},
                cumulative=True,
            )

            # Adjust the plot
            fig.update_layout(
                xaxis_title_text='Round',
                yaxis_title_text='Absolute Frequency',
                title=dict(
                        text='<b><span style="font-size: 10pt">Ordinal Variable: Cumulated</span> <br> <span style="font-size:5">Data: atp_matches_2023.csv; variable: round</span></b>',
                    ),
            )

            # Show the plot
            fig.show()
            ```

    -   __Histogram (Relative, Cumulative)__

        ---
        <iframe src="/assets/statistics/uni_ordinal_histo_sort_rel_cum.html" width="100%" height="400px"></iframe>
        ??? code "Code"
            ``` py
            import plotly.express as px
            # HISTOGRAM sorted cumulated Relative
            round_order = ['F', 'SF', 'QF', 'R16', 'R32', 'R64', 'R128', 'RR']  # Define order of the roundsd
            data['round'] = pd.Categorical(data['round'], categories=round_order, ordered=True)  # Define order of the rounds

            # Generate Histogram
            fig = px.histogram(
                data, 
                x="round",
                category_orders={"round": round_order[::-1]},
                cumulative=True,
                histnorm="percent"
            )

            # Adjust the plot
            fig.update_layout(
                xaxis_title_text='Round',
                yaxis_title_text='Relative Frequency [%]',
                title=dict(
                        text='<b><span style="font-size: 10pt">Ordinal Variable: Cumulated</span> <br> <span style="font-size:5">Data: atp_matches_2023.csv; variable: round</span></b>',
                    ),
            )

            # Show the plot
            fig.show()
            ```

    -   __Table (Abolute, Cumulative)__

        ---
        | Round   |   Absoulte Frequency  |   Absoulte Frequency Cumulated  |
        |:--------|:---------------------:|:-------------------------------:|
        | F       |                   68  |                             68  |
        | SF      |                  136  |                            204  |
        | QF      |                  256  |                            460  |
        | R16     |                  512  |                            972  |
        | R32     |                  880  |                           1852  |
        | R64     |                  432  |                           2284  |
        | R128    |                  416  |                           2700  |
        | RR      |                  286  |                           2986  |

        ??? code "Code"
            ``` py
            # FREQUENCY TABLE sorted cumulated absolute
            round_order = ['F', 'SF', 'QF', 'R16', 'R32', 'R64', 'R128', 'RR']  # Define order of the roundsd
            data['round'] = pd.Categorical(data['round'], categories=round_order, ordered=True)  # Define order of the rounds

            # Generate table with absolute and relative frequencies
            absolutefrequency_ord_sort = pd.crosstab(index=data['round'], columns='Absoulte Frequency')
            relativefrequency_ord_sort = pd.crosstab(index=data['round'], columns='Relative Frequency [%]',normalize=True)*100

            # Combine the tables
            frequencytable_ord_sort = pd.concat([absolutefrequency_ord_sort, relativefrequency_ord_sort], axis=1).reset_index()
            frequencytable_ord_sort.columns.name = None

            frequencytable_ord_sort['Absoulte Frequency Cumulated'] = frequencytable_ord_sort['Absoulte Frequency'].cumsum()
            frequencytable_ord_sort.drop(columns='Relative Frequency [%]', inplace=True)
            print(frequencytable_ord_sort)
            ```

    -   __Table (Relative, Cumulative)__

        ---
        | Round   |   Relative Frequency [%]  |   Relative Frequency Cumulated   |
        |:--------|:-------------------------:|:--------------------------------:|
        | F       |                  2.28     |                         2.28     |
        | SF      |                  4.55     |                         6.83     |
        | QF      |                  8.57     |                        15.41     |
        | R16     |                 17.15     |                        32.55     |
        | R32     |                 29.47     |                        62.02     |
        | R64     |                 14.47     |                        76.49     |
        | R128    |                 13.93     |                        90.42     |
        | RR      |                  9.58     |                       100        |

        ??? code "Code"
            ``` py
            # FREQUENCY TABLE sorted cumulated relative
            round_order = ['F', 'SF', 'QF', 'R16', 'R32', 'R64', 'R128', 'RR']  # Define order of the roundsd
            data['round'] = pd.Categorical(data['round'], categories=round_order, ordered=True)  # Define order of the rounds

            # Generate table with absolute and relative frequencies
            absolutefrequency_ord_sort = pd.crosstab(index=data['round'], columns='Absoulte Frequency')
            relativefrequency_ord_sort = pd.crosstab(index=data['round'], columns='Relative Frequency [%]',normalize=True)*100

            # Combine the tables
            frequencytable_ord_sort = pd.concat([absolutefrequency_ord_sort, relativefrequency_ord_sort], axis=1).reset_index()
            frequencytable_ord_sort.columns.name = None

            frequencytable_ord_sort['Relative Frequency Cumulated '] = frequencytable_ord_sort['Relative Frequency [%]'].cumsum()
            frequencytable_ord_sort.drop(columns='Absoulte Frequency', inplace=True)
            print(frequencytable_ord_sort)
            ```
    </div>


## Numeric Scale
When the number of values \( k \) for a metrically scaled variable is small, it can be presented in the same way as an ordinal scale. However, when \( k \) is large, the representation can become cluttered and lose clarity.

???+ example
    <div class="grid cards" markdown>

    -   __Numeric Variable with Few of Values__

        ---
        <iframe src="/assets/statistics/uni_numeric_histo_small.html" width="100%" height="400px"></iframe>
        ??? code "Code"
            ``` py
            import plotly.express as px
            # HISTOGRAM Small Number of Values
            # Generate Histogram
            fig = px.histogram(
                data, 
                x="draw_size",
            )

            # Adjust the plot
            fig.update_layout(
                xaxis_title_text='Draw Size',
                yaxis_title_text='Absolute Frequency',
                title=dict(
                        text='<b><span style="font-size: 10pt">Small Number of Values</span> <br> <span style="font-size:5">Data: atp_matches_2023.csv; variable: draw_size</span></b>',
                    ),
            )

            # Show the plot
            fig.show()
            ```

    -   __Numeric Variable with Many Values__

        ---
        <iframe src="/assets/statistics/uni_numeric_histo_large.html" width="100%" height="400px"></iframe>
        ??? code "Code"
            ``` py
            import plotly.express as px
            # HISTOGRAM Large Number of Values
            # Generate Histogram
            fig = px.bar(
                data['winner_rank_points'].value_counts().reset_index(), 
                x='winner_rank_points', 
                y='count'
                )

            # Adjust the width of the bars
            fig.update_traces(width=50)

            # Adjust the plot
            fig.update_layout(
                xaxis_title_text='Winner Rank Points',
                yaxis_title_text='Absolute Frequency',
                title=dict(
                        text='<b><span style="font-size: 10pt">Large Number of Values</span> <br> <span style="font-size:5">Data: atp_matches_2023.csv; variable: winner_rank_points</span></b>',
                    ),
            )

            # Show the plot
            fig.show()
            ```
    </div>

In such cases, categories (intervals or bins) should be created to reduce the number of displayed values, making the data easier to interpret. This can be done automatically e.g. by `#!python px.histogram()` or manually:

```py
data['points_cat'] = pd.cut(
                        data['winner_rank_points'], 
                        bins=range(0,int(data['winner_rank_points'].max()),100), 
                        right=False)
```

??? example
    <div class="grid cards" markdown>

    -   __Automatic Binning__

        ---
        <iframe src="/assets/statistics/uni_numeric_histo_large_binned.html" width="100%" height="400px"></iframe>
        ??? code "Code"
            ``` py
            import plotly.express as px

            # HISTOGRAM Large Number of Values
            # Generate Histogram
            fig = px.histogram(
                data, 
                x="winner_rank_points",
            )

            # Adjust the plot
            fig.update_layout(
                xaxis_title_text='Winner Rank Points',
                yaxis_title_text='Absolute Frequency',
                title=dict(
                        text='<b><span style="font-size: 10pt">Automatic Binning</span> <br> <span style="font-size:5">Data: atp_matches_2023.csv; variable: winner_rank_points</span></b>',
                    ),
            )

            # Show the plot
            fig.show()
            ```

    -   __Manual Binning__

        ---
        <iframe src="/assets/statistics/uni_numeric_histo_large_binned_self.html" width="100%" height="400px"></iframe>
        ??? code "Code"
            ``` py
            import plotly.express as px
            # Binning of the Data
            data['points_cat'] = pd.cut(data['winner_rank_points'], bins=range(0,int(data['winner_rank_points'].max()),100), right=False) # 100 Bins between 0 and the maximum value of winner_rank_points
            # data_num['points_cat'] = pd.cut(data_num['winner_rank_points'], bins=[0, 60, 120, 180, 240, 300, 360, 420, 480, 540, 600, 660, 720, 780, 840, 900, 960, 1020, 1080, 1140, 1200], right=False) # Custom Bins

            # Count the values in each bin
            points_cat_count = data['points_cat'].value_counts().sort_index()
            points_cat_count.index = points_cat_count.index.astype(str)

            # Generate Bar Chart
            fig = px.bar(
                points_cat_count,
                )


            # Adjust the plot
            fig.update_layout(
                xaxis_title_text='Winner Rank Points',
                yaxis_title_text='Absolute Frequency',
                showlegend=False,
                title=dict(
                        text='<b><span style="font-size: 10pt">Manual Binning</span> <br> <span style="font-size:5">Data: atp_matches_2023.csv; variable: winner_rank_points</span></b>',
                    ),
            )

            # Show the plot
            fig.show()
            ```
    </div>

Tables and charts are well-suited for providing an overview of the data. However, in some cases, it is beneficial to further condense the information within the data to reduce complexity. Nevertheless, care must be taken not to oversimplify, as this could lead to misleading interpretations. There are several key metrics available for further reducing complexity. These are typically divided into measures of central tendency and measures of dispersion.

## Recap

- Data should always be the focus, with an unbiased representation.
- Frequencies indicate how often a particular value occurs.
- Relative frequency (%) is the absolute frequency divided by the total number of observations.
- The form of representation depends on the scale level of the variable.
- In general, both tables and charts can be used.
- Cumulative frequencies show how often a reference value has not been exceeded.

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

    1. Analyse the Dataset
        - Look at the [website](https://archive.ics.uci.edu/dataset/9/auto+mpg) of the dataset and get familiar 
        - What attribute types do we have? (use `cars.variables`)
    2. Generate the following plot (think about attribute types, title, labeling of the axes)
        - Histogram | Absolute Frequency | Variable: `origin`
        - Bar Chart | Absoulte Frequency | no binning | Variable: `weight`
        - Histogram | Absoulte Frequency | automatic binning | Variable: `weight` 
        - Histogram | Relative Frequency | cumulated | Variable: `hoursepower`
        - Pie Chart | Relative Frequency | Variable: `cylinders`