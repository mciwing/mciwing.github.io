## Introduction

To achieve our end goal we have to carefully analyze and preprocess the data.
We will start by exploring the data set, handling missing values, identifying 
attribute types, and then proceed to preprocessing techniques.

???+ info

    To build a proper machine learning model for the bank marketing data set, 
    we need to channel all our knowledge obtained so far!

Create a new notebook or script.

```plaintext hl_lines="5"
📁 bank_model/
├── 📁 .venv/
├── 📁 data/
├───── 📄 bank-merged.csv
├── 📄 preparation.ipynb
```

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

    If you need a refresher on attribute types, check out the appropriate
    [section](../data-basics/basics.md#attribute-types).

<quiz>
Which attribute types are present in the data set?
- [ ] numerical
- [ ] nominal, ordinal
- [x] nominal, ordinal, numerical
- [ ] ordinal
- [ ] ordinal, numerical
- [ ] nominal
- [ ] nominal, numerical

We are dealing with quite a mixed data set. All three different
types (nominal, ordinal and numerical) are present. For example:

- **Job** - nominal
- **Education** - ordinal
- **Age** - numerical

</quiz>

#### Feature description

With a broad overview, let's explore the different features/attributes more 
in-depth. Since we are dealing with a couple of features, categories were 
built. 

<div class="grid cards" markdown>

-   :old_man: __Client Demographics__

    ---
    
    Demographic information about each client such as the education level
    (high school, university, etc.).

    | Variable  | Description                                       |
    |-----------|---------------------------------------------------|
    | id        | Client identifier (we will ignore the identifier) |
    | age       | Age                                               |
    | job       | Type of occupation                                |
    | marital   | Marital status                                    |
    | education | Education level                                   |

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
    | poutcome    | Outcome of previous campaign                   |

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
    (`#!python 0`).

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

    - `#!python "age"` is a "measurable" quantity and expressed as a number, 
        thus is a numerical attribute.

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

    If you want to know more on visualizing different attribute types, visit 
    the [Frequency Distribution](../../statistics/univariate/Frequency.md) 
    chapter of the Statistics course.

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

    Use these `pandas` resources, if you're having trouble:

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
    
    `nominal` and `ordinal` attributes are categorical and require one-hot
    encoding to be suitable for machine learning algorithms.

    We are creating bins for `age`, `campaign`, `pdays`, and `previous`, since
    these features have a large number of outliers. By binning these features,
    we can try to reduce the impact of outliers and noise in the data.

    Z-Score normalization is applied to the remaining numerical features to
    ensures that features don't have a larger impact on the model just 
    because of their larger magnitude.

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

binning = KBinsDiscretizer(n_bins=5, strategy="uniform")
binning.fit_transform(data[["age", "campaign", "pdays", "previous"]])

# and so on...
```

... the above approach itself is perfectly fine, but we can do better!
But first, we need to get the term information leakage out of the way, a 
common pitfall in machine learning/data science projects.

### Information leakage

To explain the term information leakage, let's look at an example.

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

With information leakage in mind, we introduce a more elegant way to apply 
multiple preprocessing steps.

### `ColumnTransformer`

<div style="text-align: center;">
    <h4>
        Not the kind of transformer you are expecting, but cool nonetheless!
        🤖
    </h4> 
    <img src="https://static1.cbrimages.com/wordpress/wp-content/uploads/2023/12/split-images-of-transformers-anime.jpg" 
    alt="Transformers">
</div>

Since we do not want to apply each preprocessing step one at a time, we 
simply bundle them.

The [`ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html) 
is a class in `scikit-learn` that allows us to bundle our preprocessing steps
together. This way, we can apply all transformations in one go.

First, we import all necessary classes:

```python hl_lines="1"
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import KBinsDiscretizer, OneHotEncoder, StandardScaler
```

Next, we can already initiate our transformer. We define the exact same steps 
as we did in written form at the beginning of this section. Note that the 
`ColumnTransformer` takes a `#!python list` of `#!python tuple`.

```python linenums="1"
preprocessor = ColumnTransformer(
    transformers=[
        ("nominal", OneHotEncoder(), 
         ["default", "housing", "loan", "contact", "poutcome", "job", "marital"]),
        
        ("ordinal", OneHotEncoder(), 
         ["month", "day_of_week", "education"]),
        
        ("binning", KBinsDiscretizer(n_bins=5, strategy="uniform", encode="onehot"),  # (1)!
         ["age", "campaign", "pdays", "previous"]),
        
        ("zscore", StandardScaler(), 
         ["emp.var.rate", "cons.price.idx", "cons.conf.idx", "euribor3m", "nr.employed"]),
    ]
)
```

1. Conveniently, we can create categories (bins) with the `KBinsDiscretizer` 
   and directly apply one-hot encoding with `#!python encode="oneheot"`.

Let's break it down:

- Our instance `preprocessor` has 4 steps, named `nominal`, `ordinal`, 
  `binning`, and `zscore`.
- Each step is defined as a `#!python tuple`, with the first element being 
  the name of the step, the second element the preprocessing technique, and 
  the third element being a list of columns to apply the technique to.
- By default, all columns which are not specified in the `ColumnTransformer` 
  will be dropped! See the [`remainder`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html)
  parameter in the docs.

So far we only defined the necessary preprocessing steps, but didn't apply 
them just yet (that's part of the next chapter).

### Detour: Didn't we forget something?

We completely neglected the missing values in the data set. Thus, we still 
need to handle them with an imputation technique.

???+ tip

    During the development process of a data science project, you will often 
    find yourself jumping back and forth between different steps. This is 
    perfectly normal and part of the process. Seldom will you follow a 
    linear path from start to finish.

```python
print(data.isna().sum())
```

If you execute the above line, you will see that we still have many missing 
values in a couple of columns. No worries, we can easily handle them with:

```python
from sklearn.impute import SimpleImputer

impute = SimpleImputer(strategy="most_frequent", missing_values=None)
```

The `SimpleImputer` lets us fill in missing values with the most frequent
value in the respective column. But why did we choose this specific strategy?

<quiz>
Why do we plan to fill missing values with the most frequent value (the mode) and not the mean or median?
- [ ] The mode is the most common imputation strategy.
- [x] The columns with any missing values are either nominal or ordinal. Thus, the most frequent value (mode) is a valid choice for imputation. Mean and median are not suitable for nominal and ordinal data.
- [ ] It is just an initial choice, we could have used any other strategy.
- [ ] The mode is the most robust imputation strategy.

<p>Correct! 👍🏽</p>
</quiz>

???+ info

    You might wonder why we didn't include the imputation step in the
    `ColumnTransformer`. The reason is that passing the same column to more 
    than one step leads to issues. As the `ColumnTransformer` runs in 
    parallel and does not apply the steps sequentially.

## Recap

In this chapter, we started our practical data science project by exploring 
the bank marketing data set further. We handled missing values and identified 
attribute types. We then visualized the data to get a better understanding of 
the features. During our discussion of appropriate preprocessing methods, 
we discovered the term information leakage and how to prevent it.
Finally, we introduced the `ColumnTransformer` to bundle preprocessing
steps together.

### Code recap

This time around, we also do a code recap. The essential findings in this 
chapter can be distilled to:

```python linenums="1"
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import KBinsDiscretizer, OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer

data = pd.read_csv("data/bank-merged.csv")
data = data.replace("unknown", None)

impute = SimpleImputer(strategy="most_frequent", missing_values=None)

preprocessor = ColumnTransformer(
    transformers=[
        ("nominal", OneHotEncoder(), 
         ["default", "housing", "loan", "contact", "poutcome", "job", "marital"]),
        
        ("ordinal", OneHotEncoder(), 
         ["month", "day_of_week", "education"]),
        
        ("binning", KBinsDiscretizer(n_bins=5, strategy="uniform", encode="onehot"),
         ["age", "campaign", "pdays", "previous"]),
        
        ("zscore", StandardScaler(), 
         ["emp.var.rate", "cons.price.idx", "cons.conf.idx", "euribor3m", "nr.employed"]),
    ]
)
```

In the next chapter we will apply the preprocessing steps to a train and 
test split. Subsequently, we fit the first model.
