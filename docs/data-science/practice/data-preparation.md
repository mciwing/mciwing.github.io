## Introduction

To achieve our end goal we have to carefully analyze and preprocess the data.
We will start by exploring the data set, handling missing values, identifying 
attribute types, and then proceed to apply preprocessing techniques.

???+ info

    To build a proper machine learning model for the bank marketing data set, 
    we need to channel all our knowledge obtained so far!

## Data

We start by loading the data.

```python
import pandas as pd

data = pd.read_csv("data/bank-merged.csv")
```

???+ question "A look at the data"

    It's always a good idea to take a look at the data before proceeding.

    1. Check the shape of the data.
    2. Display the first few rows.

## Missing values

In the data preprocessing chapter we discussed missing values. Recall that 
in this specific data set, the missing values are a bit more 
[hidden](../data/preprocessing.md#missing-values-in-disguise).
They are encoded as `#!python "unknown"`. So let's replace these values with
`#!python None`.

```python
data = data.replace("unknown", None)
```

With a cleaned data set, we can now proceed to the next step - data 
exploration. 

## Attribute types

Start by checking the attribute types.

???+ question "Attribute types"

    Again, look at the data set. The task is to identify which attribute types 
    are generally present in the dataset. Answer, the following quiz question.

    <!--- TODO: add a link to the data types page. --->
    If you need a refresher on attribute types, check the
    [data types](../../databasics/DataBasics.md#attribute-types).

<?quiz?>
question: Which attribute types are present in the data set?
answer: numerical
answer: nominal, ordinal
answer-correct: nominal, ordinal, numerical
answer: ordinal
answer: ordinal, numerical
answer: nominal
answer: nominal, numerical
content:
<p>Correct, we are dealing with quite a mixed data set. All three different 
types (nominal, ordinal and numerical) are present. For example:
<ul>
    <li><strong>Job</strong> - nominal</li>
    <li><strong>Education</strong> - ordinal</li>
    <li><strong>Age</strong> - numerical</li>
</ul>
<?/quiz?>

#### Feature description

With a broad overview, let's explore the different features/attributes more 
in-depth. Since we are dealing with a couple of features, categories were 
built. 

<div class="grid cards" markdown>

-   :old_man: __Client Demographics__

    ---
    
    Demographic information about each client such as the education level
    (high school, university, etc.).

    | Variable  | Description                                          |
    |-----------|------------------------------------------------------|
    | id        | Client identifier (we will disregard the identifier) |
    | age       | Client's age                                         |
    | job       | Type of occupation                                   |
    | marital   | Marital status                                       |
    | education | Education level                                      |

-   :money_mouth_face: __Financial Status__

    ---

    Does the client have a housing or personal loan, etc.

    | Variable | Description           |
    |----------|-----------------------|
    | default  | Credit default status |
    | housing  | Housing loan status   |
    | loan     | Personal loan status  |

-   :telephone: __Campaign Information__

    ---
    
    Remember, bank clients were contacted by phone. Some were contacted 
    multiple times over the span of multiple campaigns.

    | Variable    | Description                                    |
    |-------------|------------------------------------------------|
    | contact     | Contact type                                   |
    | month       | Last contact month                             |
    | day_of_week | Last contact day                               |
    | campaign    | Number of contacts in current campaign         |
    | pdays       | Days since last contact from previous campaign |
    | previous    | Number of contacts before this campaign        |
    | poutcome    | Previous campaign outcome                      |

-   :factory: __Economic Indicators__

    ---
    
    Some economic indicators at the time of the contact like the current
    interest rate ([Euribor rate](https://www.euribor-rates.eu/en/)).

    | Variable       | Description               |
    |----------------|---------------------------|
    | emp.var.rate   | Employment variation rate |
    | cons.price.idx | Consumer price index      |
    | cons.conf.idx  | Consumer confidence index |
    | euribor3m      | Euribor 3-month rate      |
    | nr.employed    | Number of employees       |

</div>

???+ info

    Lastly, one column remains - `#!python "y"`. This column is the target, 
    whether a customer subscribed to a term deposit (`#!python 1`) or not
    `#!python 0`.

With a better understanding of the features at hand, we can proceed to the 
next step, assigning attribute types to the columns. Doing so, will help us 
later to pick the appropriate preprocessing steps.

#### Assigning attribute types

???+ question "Assigning attributes"

    Assign an attribute type to each column. Look at the data and go 
    over each column/attribute and add the column name to one of the three 
    empty lists.

    Disregard the unique identifier `#!python "id"` and the target 
    `#!python "y"`.

    ```python
    nominal = []
    ordinal = []
    numerical = []
    ```

    ---    

    For example (part of the solution): 

    - `#!python "age"` is a measurable quantity and expressed as number, thus
        is a numerical attribute.

    - The next attribute `#!python "default"` is clearly categorical with 
        its unique values `#!python ["no", None, "yes]`. But since the 
        attribute has no meaningful order, it is nominal.
    
    Resulting so far in:

    ```python
    nominal = ["default"]
    ordinal = []
    numerical = ["age"]
    ```

    Now, go ahead and assign all of the remaining attributes.

???+ danger

    Since the attribute assignment is crucial, we strongly urge you to solve 
    the task. It will help your understanding of the data set and the next 
    steps.

    Check your solution with the answer below and correct any mistakes you've
    made.

??? info

    The solution is as follows (column names are ordered according to 
    `data`):

    ```python
    nominal = [
        "default",
        "housing",
        "loan",
        "contact",
        "poutcome",
        "job",
        "marital",
    ]
    
    ordinal = [
        "month",
        "day_of_week",
        "education",
    ]
    
    numerical = [
        "age",
        "campaign",
        "pdays",
        "previous",
        "emp.var.rate",
        "cons.price.idx",
        "cons.conf.idx",
        "euribor3m",
        "nr.employed",
    ]
    ```

### Visualizing the data

To get an even better understanding of the data, we can visualize it. For 
convenience, we will use `pandas` built-in plotting 
[capabilities](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html). 

???+ tip
    
    <!-- TODO: update link; once available in the data science course -->
    As a refresher on how to visualize different attribute types, you can visit 
    the [Frequency Distribution](../../statistics/univariate/Frequency.md) 
    chapter.

For example, we can plot numerical attributes like `#!python "campaign"` as a
box plot.

```python
import matplotlib.pyplot as plt

data.plot(
    kind="box", y="campaign", title="Number of contacts in current campaign"
)
plt.show()
```

<div style="text-align: center;">
    <img src="/assets/data-science/practical/boxplot-campaign.svg" alt="Campaign boxplot">
</div>

???+ info

    As you might have noticed, you need to install `matplotlib`.

Or how about a pie chart for nominal attributes like `#!python "marital"`?

```python
# first, count the occurrence of each category
marital_count = data["marital"].value_counts()
marital_count.plot(kind="pie", autopct="%1.0f%%", title="Marital status")  # (1)!
plt.show()
```

1. The `autopct` parameter is used to display the percentage on the pie chart.

<div style="text-align: center;">
    <img src="/assets/data-science/practical/pie-marital.svg" alt="Pie chart marital">
</div>

???+ question "Visualize"

    Pick two more attributes of your choice and plot them.

    1. Choose a numerical attribute and plot it as a histogram.
    2. Select a nominal or ordinal attribute and plot it as a bar chart.

    Use the `pandas` resources, if you're having trouble:

    - `DataFrame.plot()` docs [:octicons-link-external-16:](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html)
    - Chart visualization [:octicons-link-external-16:](https://pandas.pydata.org/docs/user_guide/visualization.html)

???+ info

    It's crucial to visualize your data before diving into further analysis. 
    Visualizations can help you understand the distribution, identify patterns,
    and detect anomalies or outliers in your data. This step ensures that you
    have a clear understanding of your data, which is essential for making 
    informed decisions in your analysis process.

## Preprocessing

Now that we have a better understanding of the data, we can proceed to the
preprocessing steps. Depending on the attribute type, we will apply different
techniques.

Since we are dealing with a mixed data set, we will keep things relatively 
simple and plan our approach accordingly:

- For `nominal` attributes, we apply one-hot encoding.
- For `ordinal` attributes, we use one-hot encoding as well.
- For `numerical` attributes, we follow two strategies:
    - Create bins for `age`, `campaign`, `pdays`, and `previous`.
    - Z-Score normalization for the remaining features: `emp.var.rate`, 
      `cons.price.idx`, `cons.conf.idx`, `euribor3m`, and `nr.employed`.

???+ info

    We are creating bins for `age`, `campaign`, `pdays`, and `previous`, since
    these features have a large number of outliers. By binning these features,
    we can try to reduce the impact of outliers and noise in the data.

To apply these preprocessing steps, we have to look for the corresponding
`scikit-learn` classes.

<div class="grid cards" markdown>

-   :toolbox: __Preprocessing technique__

    ---

    - One hot encoding
    - Binning
    - Z-Score normalization (standardization)

-   :package: __Corresponding `scikit-learn` class__

    ---
    
    - `OneHotEncoder`
    - `KBinsDiscretizer`
    - `StandardScaler`

</div>

???+ tip

    All these techniques and classes were previously introduced in the 
    [Data preprocessing chapter](../data/preprocessing.md).

Just like in the Data preprocessing chapter we could apply each technique
one at a time, e.g.:

```python
from sklearn.preprocessing import OneHotEncoder, KBinsDiscretizer

nominal_encoder = OneHotEncoder()
nominal_encoder.fit_transform(data[nominal])

ordinal_encoder = OneHotEncoder()
ordinal_encoder.fit_transform(data[ordinal])

binning = KBinsDiscretizer(n_bins=5)
binning.fit_transform(data[["age", "campaign", "pdays", "previous"]])

# and so on...
```

... the approach itself is perfectly fine, but it can lead to a common 
pitfall - information leakage. 

### Information leakage

Let's look at an example first, to explain the term information leakage.

???+ danger "Information leakage"

    Assume, we want to predict the target `#!python "y"` based on the features 
    `#!python "emp.var.rate"` and `#!python "euribor3m"`. First, we apply 
    Z-Score normalization to these features. 

    ```python
    from sklearn.preprocessing import StandardScaler

    scaler = StandardScaler()
    features = scaler.fit_transform(
        data[["emp.var.rate", "euribor3m"]]
    )
    ```
    
    As always, we are splitting the data into training and test set to 
    later evaluate the model.

    ```python
    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(
        features, data["y"], test_size=0.2, random_state=42
    )
    ```
    
    Now, we are already dealing with information leakage. Put simply - the
    train set `X_train` already "knows" something about the test set `X_test`. 
    
    Why?
    
    ---

    Remember the definition of Z-Score normalization - it calculates the mean
    and standard deviation of the data set. If we calculate these values on the
    whole data set; in our case `data` - just like we did above, `X_train` 
    contains information about `X_test`. Thus, the test set is no longer a 
    good representation of unseen data, hence any scores calculated with the 
    test set are no longer a good indicator of the model's performance.

    This is a common pitfall in machine learning! To prevent information 
    leakage, we ==have to split the data before applying any preprocessing 
    steps==.

In turn this means, we have to apply all preprocessing twice - once for the
training set and once for the test set, which means a lot of code duplication.

So we streamline things and introduce a new functionality to group all 
preprocessing steps together which we then can easily apply on train and 
test set.

### `ColumnTransformer`

<div style="text-align: center;">
    <h4>
        Not the kind of transformer you are expecting, but cool nonetheless!
        🤖
    </h4> 
    <img src="https://static1.cbrimages.com/wordpress/wp-content/uploads/2023/12/split-images-of-transformers-anime.jpg" 
    alt="Transformers">
</div>

The [`ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html) 
is a class in `scikit-learn` that allows us to bundle our preprocessing steps
together. This way, we can apply all transformations in one go.

First, we import all necessary classes:

```python hl_lines="1"
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import KBinsDiscretizer, OneHotEncoder, StandardScaler
```
