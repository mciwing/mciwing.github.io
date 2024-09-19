# Frequency Distribution
Two variables, \(X\) and \(Y\), consist of \(n\) elements. The raw data list consists of the tuples \((x_1, y_1), \dots, (x_n, y_n)\). Possible values are \(a_1, \dots, a_k\) for \(X\) and \(b_1, \dots, b_m\) for \(Y\). The absolute frequency refers to how often a combination \((a_i, b_j)\) occurs.

Representation of frequencies can be done in the form of a table or a graphic. In tabular form, the so-called crosstab (or contingency table) is commonly used. For graphical representation, a histogram (or 2D bar chart) is suitable. It is important that the data remain the focal point and are presented as accurately and objectively as possible, avoiding distortions like 3D effects or shadows. Titles, axis labels, legends, the data source, and the time of data collection should always be clearly indicated.

???+ defi "Definition"
    **Absolute frequency** of the combination \( (a_i, b_j) \):

    \[
    h_{ij} = h(a_i, b_j)
    \]

    **Relative frequency** of the combination \( (a_i, b_j) \):

    \[
    f_{ij} = f(a_i, b_j) = \frac{h_{ij}}{n}
    \]

## Histogram
Histograms are also suitable for bivariate data to represent frequency. Both absolute and relative frequencies can be visualized using this method. Multidimensional histograms can be created using the Python package matplotlib. A specific type of representation is the density heatmap, which can also be generated using plotly.

??? example

    <iframe src="/assets/statistics/bi_heatmap.html" width="100%" height="400px"></iframe>
    ??? code "Code"
        ``` py
        from ucimlrepo import fetch_ucirepo 
        import plotly.express as px
  
        # fetch dataset 
        drugs = fetch_ucirepo(id=468) 
        # https://archive.ics.uci.edu/dataset/462
        
        # data (as pandas dataframes) 
        data = drugs.data.features

        # Create a density heatmap
        fig = px.density_heatmap(data, x="Region", y="VisitorType")

        # Adjust the plot
        fig.update_layout(
            xaxis_title_text='Region',
            yaxis_title_text='Visitor Type',
            title=dict(
                    text='<b><span style="font-size: 10pt">Densitiy Heatmap</span> <br> <span style="font-size:5">Data: drug_reviews_drugs_com; variable: Region, VisitorType</span></b>',
                ),
        )

        # Show the plot
        fig.show()

        ```


## Crosstab (Contingency Table)
The representation of the joint distribution of discrete features with few categories (if there are many categories, they need to be grouped into categories) can be done using contingency tables. These tables can display both absolute and relative frequencies. It is important to note that contingency tables use only the nominal scale level, even if a variable could be measured at a higher level (ordinal or numerical).

**Marginal Frequencies** refer to the row and column totals added to a table. The row totals are the marginal frequencies of the variable \(X\), calculated as \( h_{i.} = h_{i1} + \dots + h_{im} \) for \( i = 1, \dots, k \). The column totals are the marginal frequencies of the variable \(Y\), given by \( h_{.j} = h_{1j} + \dots + h_{kj} \) for \( j = 1, \dots, m \).

**Marginal Distribution** refers to the marginal frequencies of a variable, which are the **simple frequencies** without considering the second variable. The collection of all marginal frequencies for a variable gives the marginal distribution of \(X\) (\(h_{1.}, h_{2.}, \dots, h_{k.}\)) or \(Y\)(\(h_{.1}, h_{.2}, \dots, h_{.m}\)) in absolute frequencies:

### Absolute Frequency

???+ defi "Definition"
    Crosstab of the absolute Frequencies

    <div class="grid cards" markdown>

    -  
        \[
        \begin{array}{c|ccc|c}
            & b_1 & \dots & b_m & \sum \\ \hline
            a_1 & h_{11} & \dots & h_{1m} & h_{1.} \\
            a_2 & h_{21} & \dots & h_{2m} & h_{2.} \\
            \vdots & \vdots &  & \vdots & \vdots \\
            a_k & h_{k1} & \dots & h_{km} & h_{k.} \\ \hline
            \sum & h_{.1} & \dots & h_{.m} & n
        \end{array}
        \]

    -   
        - \( a_i \): Values of \( X \) with \( i = 1, \dots, k \)
        - \( b_j \): Values of \( Y \) with \( j = 1, \dots, m \)
        - \( h_{ij} \): The absolute frequency of the combination \( (a_i, b_j) \)
        - \( h_{1.}, \dots, h_{k.} \): The marginal frequencies of \( X \)
        - \( h_{.1}, \dots, h_{.m} \): The marginal frequencies of \( Y \)
        - \( n \): Total number of elements
    </div>


??? example
    Crosstab of the absolute Frequencies 
    
    \[
    \begin{array}{r|ccccccccc|c}
     & & & & & Region & & & & &	\\
    Visitor Types	& \textbf{1}  & \textbf{2}  & \textbf{3}  & \textbf{4}  & \textbf{5}  &\textbf{ 6}  & \textbf{7}  & \textbf{8}  &\textbf{9}  &	\sum\\\hline
    \textbf{New_Visitor} & 657 &	149&	312&	139&	50&	121&	100&	74&	92&	1694 \\
    \textbf{Returning_Visitor} & 4115	&982	&2083	&1038	&268	&683&	659&	359&	364&	10551 \\
    \textbf{Other} & 8	&5	&8	&5	&0	&1	&2	&1	&55	&85 \\ \hline
    \sum & 4780	&1136	&2403	&1182	&318	&805	&761	&434	&511	&12330\\
    \end{array}
    \]

    ??? code "Code"
        ``` py
        from ucimlrepo import fetch_ucirepo 
  
        # fetch dataset 
        drugs = fetch_ucirepo(id=468) 
        # https://archive.ics.uci.edu/dataset/462
        
        # data (as pandas dataframes) 
        data = drugs.data.features

        import pandas as pd

        # Create a crosstab
        pd.crosstab( data['VisitorType'],data['Region'], margins=True)
        ```

### Relative Frequency


???+ defi "Definition"
    Crosstab of the relative Frequencies

    <div class="grid cards" markdown>

    -  
        \[
        \begin{array}{c|ccc|c}
            & b_1 & \dots & b_m & \sum \\ \hline
            a_1 & f_{11} & \dots & f_{1m} & f_{1.} \\
            a_2 & f_{21} & \dots & f_{2m} & f_{2.} \\
            \vdots & \vdots &  & \vdots & \vdots \\
            a_k & f_{k1} & \dots & f_{km} & f_{k.} \\ \hline
            \sum & f_{.1} & \dots & f_{.m} & 1
        \end{array}
        \]

    -   
        - \( a_i \): Values of \( X \) with \( i = 1, \dots, k \)
        - \( b_j \): Values of \( Y \) with \( j = 1, \dots, m \)
        - \( f_{ij} = \frac{h_{ij}}{n} \): The relative frequency of the combination \( (a_i, b_j) \)
        - \( f_{i.} = \frac{h_{i.}}{n} \): The relative marginal frequencies of \( X \)
        - \( f_{.j} = \frac{h_{.j}}{n} \): The relative marginal frequencies of \( Y \)
    </div>

??? example
    Crosstab of the relative Frequencies in [%]
    
    \[
    \begin{array}{r|ccccccccc|c}
     & & & & & Region & & & & &	\\
    Visitor Types	& \textbf{1}  & \textbf{2}  & \textbf{3}  & \textbf{4}  & \textbf{5}  &\textbf{ 6}  & \textbf{7}  & \textbf{8}  &\textbf{9}  &	\sum\\\hline
    \textbf{New_Visitor}        &   5.3 &	  1.2 &	  2.5 &	  1.1 &	  0.4 &	  1.0 &	  0.8 &	  0.6 &	  0.7 &	 13.7 \\
    \textbf{Returning_Visitor}  &  33.4 &	  8.0 &	 16.9 &	  8.4 &	  2.2 &	  5.5 &	  5.3 &	  2.9 &	  3.0 &	 85.6 \\
    \textbf{Other}              &   0.1 &	  0.0 &	  0.1 &	  0.0 &	  0.0 &	  0.0 &	  0.0 &	  0.0 &	  0.4 &	  0.7 \\ \hline
    \sum                        &  38.8 &	  9.2 &	 19.5 &	  9.6 &	  2.6 &	  6.5 &	  6.2 &	  3.5 &	  4.1 &	100.0\\
    \end{array}
    \]

    ??? code "Code"
        ``` py
        from ucimlrepo import fetch_ucirepo 
  
        # fetch dataset 
        drugs = fetch_ucirepo(id=468) 
        # https://archive.ics.uci.edu/dataset/462
        
        # data (as pandas dataframes) 
        data = drugs.data.features

        import pandas as pd

        # Create a crosstab
        pd.crosstab( data['VisitorType'],data['Region'], margins=True, normalize='all')
        ```


## Conditional frequency

Absolute and relative frequencies are not suitable for determining the relationship between variables. For example, the frequency of regions for 'New_Visitors' and 'Returning_Visitors' cannot be directly compared because the sizes of both groups are different. The conditional relative frequency allows for this comparison by accounting for the differences in group sizes.


???+ defi "Definition"

    **Conditional Frequency Distribution of \( Y \) given \( X = a_i \):**

    \[
    f_{Y,ij} = \frac{f_{ij}}{f_{i.}} = \frac{h_{ij}}{h_{i.}}
    \]

    **Conditional Frequency Distribution of \( X \) given \( Y = b_j \):**

    \[
    f_{X,ij} = \frac{f_{ij}}{f_{.j}} = \frac{h_{ij}}{h_{.j}}
    \]

??? example
    Crosstab of the Conditional Frequencies for given Visitor Types in [%]
    
    \[
    \begin{array}{r|ccccccccc|c}
     & & & & & Region & & & & &	\\
    Visitor Types	& \textbf{1}  & \textbf{2}  & \textbf{3}  & \textbf{4}  & \textbf{5}  &\textbf{ 6}  & \textbf{7}  & \textbf{8}  &\textbf{9}  &	\sum\\\hline
    \textbf{New_Visitor}        & 38.8 & 8.8 & 18.4 & 8.2 & 3.0 & 7.1 & 5.9 & 4.4 &  5.4 & 100 \\
    \textbf{Returning_Visitor}  & 39.0 & 9.3 & 19.7 & 9.8 & 2.5 & 6.5 & 6.2 & 3.4 &  3.4 & 100 \\
    \textbf{Other}              &  9.4 & 5.9 &  9.4 & 5.9 & 0.0 & 1.2 & 2.4 & 1.2 & 64.7 & 100 \\ \hline
    \sum                        & 38.8 & 9.2 & 19.5 & 9.6 & 2.6 & 6.5 & 6.2 & 3.5 &  4.1 & 100\\
    \end{array}
    \]

    ??? code "Code"
        ``` py
        from ucimlrepo import fetch_ucirepo 
  
        # fetch dataset 
        drugs = fetch_ucirepo(id=468) 
        # https://archive.ics.uci.edu/dataset/462
        
        # data (as pandas dataframes) 
        data = drugs.data.features

        import pandas as pd

        # Create a crosstab
        print(pd.crosstab( data['VisitorType'],data['Region'], margins=True, normalize='index'))
        ```

??? example
    Crosstab of the Conditional Frequencies for given Region in [%]
    
    \[
    \begin{array}{r|ccccccccc|c}
     & & & & & Region & & & & &	\\
    Visitor Types	& \textbf{1}  & \textbf{2}  & \textbf{3}  & \textbf{4}  & \textbf{5}  &\textbf{ 6}  & \textbf{7}  & \textbf{8}  &\textbf{9}  &	\sum\\\hline
    \textbf{New_Visitor}        & 13.7 & 13.1 & 13.0 & 11.8 & 15.7 & 15.0 & 13.1 & 17.1 & 18.0 & 13.7  \\
    \textbf{Returning_Visitor}  & 86.1 & 86.4 & 86.7 & 87.8 & 84.3 & 84.8 & 86.6 & 82.7 & 71.2 & 85.6  \\
    \textbf{Other}              &  0.2 &  0.4 &  0.3 &  0.4 &  0.0 &  0.1 &  0.3 &  0.2 & 10.8 &  0.7  \\ \hline
    \sum                        & 100& 100& 100& 100& 100& 100& 100& 100& 100& 100\\
    \end{array}
    \]

    ??? code "Code"
        ``` py
        from ucimlrepo import fetch_ucirepo 
  
        # fetch dataset 
        drugs = fetch_ucirepo(id=468) 
        # https://archive.ics.uci.edu/dataset/462
        
        # data (as pandas dataframes) 
        data = drugs.data.features

        import pandas as pd

        # Create a crosstab
        print(pd.crosstab( data['VisitorType'],data['Region'], margins=True, normalize='columns'))
        ```

## Recap

- Frequencies in the bivariate case describe how often a combination of two values occurs.
- As in the univariate case, a distinction between absolute and relative frequency is made.
- 2D histograms or contingency tables can be used for representation.
- Relationships between variables are not easily identified in either absolute or relative contingency tables.
- The conditional frequency examines the frequency distribution of one variable while fixing the second variable.

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

    # Show the first 5 rows
    data.head()
    ```
    Work on the following task: 

    1. Generate a 2D Histogram for the variables **origin** and **horsepower** (think about attribute types, title, labeling of the axes). Interpret the results. 
    2. Calculate the crosstab for the absolute frequencies of the variables **origin** and **cylinders**
    3. Calculate the conditional crosstab for the relative frequencies to answer the following question: Whats the cylinder distributed within each origin? 