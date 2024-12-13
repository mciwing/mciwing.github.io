# Data preprocessing

![Continue your quest!](../../assets/data-science/data/continue-quest.png)
<figcaption style="text-align: center;">
    Continue your data preprocessing quest! 🧙‍♂️
</figcaption>

???+ info "`scikit-learn`"
    
    This chapter introduces the package
    [`scikit-learn`](https://scikit-learn.org/stable/), the swiss-army knife
    for data preprocessing, transformation and machine learning.

    We will continue to work with the Portuguese retail bank data 
    set[^1] and preprocess it further. Alongside we start to explore 
    `scikit-learn`'s functionalities.

    [^1]:
        Decision Support Systems, Volume 62, June 2014, Pages 22-31:
        [https://doi.org/10.1016/j.dss.2014.03.001](https://doi.org/10.1016/j.dss.2014.03.001)

    Check-out the excellent [scikit-learn documentation](https://scikit-learn.org/stable/),
    especially [6.3 Preprocessing data](https://scikit-learn.org/stable/modules/preprocessing.html)
    which this section is based on.

## Prerequisites

If you have followed the previous chapter closely, your project structure 
looks like this:

```plaintext hl_lines="2 5"
📁 bank_marketing/
├── 📁 .venv/
├── 📁 data/
├───── 📄 bank.tsv
├───── 📄 bank-merged.csv
└───── 📄 bank-social.csv
```

With `bank-merged.csv` being the `#!python "inner"` join of `bank.csv` and 
`social.csv`, minus all duplicated customer data. 

If you are missing the file `bank-merged.csv`, we strongly recommend you to 
go back and complete the previous chapter. For the sake of completeness, 
we provide a distilled version of the code from 
[Data preparation](preparation.md):

??? info "Merge the data sets"

    ```python linenums="1"
    # Steps from the Data preparation chapter
    import pandas as pd
    
    data = pd.read_csv("bank.tsv", sep="\t")
    data_social = pd.read_csv("bank-social.csv", sep=";")
    
    data = data.drop_duplicates()
    data_social = data_social.drop_duplicates()
    
    data_merged = data.merge(data_social, on="id", how="inner")
    data_merged.to_csv("data/bank-merged.csv", index=False)
    ```
    
    <div class="center-button" markdown>
    [Merged data :fontawesome-solid-download:](../../assets/data-science/data/bank-merged.csv){ .md-button }
    </div>

Again, we urge you to use a virtual environment which by now, should be second 
nature anyway.

## Missing values

After dropping duplicates and merging the data, the next step is to check 
for missing values. First, we read the data.

```python
import pandas as pd

data = pd.read_csv("preprocessing/bank-merged.csv")
```

We chain a couple of methods to count the missing values in each column.

```python
print(data.isna().sum())
```

The `#!python isna()` method checks each element and whether it is a missing 
value or not. The result is a `DataFrame` with boolean values of the same 
shape as the initial `DataFrame` (in our case `data`), with `#!python True` 
being a missing value. With the addition of `#!python sum()` we simply sum the 
`#!python True` values (missing values) for each column.

A truncated version of the output is shown below:

| Column    | Missing Values |
|-----------|----------------|
| id        | 0              |
| age       | 0              |
| default   | 0              |
| housing   | 0              |
| ...       | ...            |
| job       | 0              |
| marital   | 0              |
| education | 0              |
| ...       | ...            |

It seems like the columns have no missing values. To sum missing values of 
the whole `DataFrame`, we can chain another `#!python sum()`.

```python
print(data.isna().sum().sum())
```

The output once more indicates that the whole data set has `#!python 0` 
missing values. So far so good, but this is not the end of the story (who 
saw that coming 🤯).

<div style="text-align: center;">
    <iframe src="https://giphy.com/embed/aWPGuTlDqq2yc" width="480" height="254" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/celebrity-reshuffle-aWPGuTlDqq2yc"></a></p>
    <figcaption>
        Plot twist...
    </figcaption>
</div>

Although, it seems like we don't have to bother with missing values, they 
are simply a bit more hidden.

### Missing values in disguise

`pandas` considers types like `#!python None` or `#!python np.nan` as 
missing. However in practice, missing values are encoded in various ways.
For instance, strings like `#!python "NA"` or integers like `#!python -999` 
are used. Consequently, we can't detect these ways of encoding with 
simply calling `#!python isna()`.

Since we have to manually detect these encoded missing values, it is 
essential to have a good understanding of the data. Let's get more 
familiarized with the data.

Visit the UCI Machine Learning Repository 
[here](https://archive.ics.uci.edu/dataset/222/bank+marketing) which also 
hosts the data set and some additional information. Interestingly, the section 
*Dataset Information* states:

> **Has Missing Values?**
>
> No

Although that might be technical correct (the data contains no empty values), 
we have to dig deeper.

???+ question "Detect the encoding of missing values"
    
    Open the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/222/bank+marketing).
    Look at the *Variables Table*. How are the missing values encoded in the 
    data set?

    Use the following quiz question to validate your answer.

    Remember, the bigger picture :fontawesome-solid-arrow-right:
    get familiar with the data, to train the best possible model to predict 
    the target variable `y` (subscribed to term deposit).

<?quiz?>
question: How are missing values encoded in this specific data set?
answer-correct: "unknown"
answer: -1
answer: "NA"
answer: 999
content:
<p>Correct, the label "unknown" is used for missing values. Nominal attributes 
like <u>occupation</u>, <u>marital status</u> and ordinal attributes for 
example <u>education</u> contain "unknown" values.</p>
<?/quiz?>

### Missing values uncovered

Now that we now the encoding of missing values, we replace them with 
`#!python None` to properly detect them and handle them more easily.

???+ question "Replace encoding with `#!python None`"
    
    Since, you've detected the particular encoding of missing values, replace 
    them with `#!python None` across the whole data frame.
    
    Use the `DataFrame.replace()` method and read the 
    [docs](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.replace.html), 
    especially the *Examples* section for usage guidance.

Again, let's sum up the missing values per column.

```python
print(data.isna().sum())
```

A truncated version of the output:

| Column    | Missing Values |
|-----------|----------------|
| id        | 0              |
| age       | 0              |
| default   | 760            |
| housing   | 97             |
| ...       | ...            |
| job       | 35             |
| marital   | 11             |
| education | 161            |
| ...       | ...            |

At first glance, a lot of columns contain missing values. Let's calculate 
the ratio to get a better feeling.

```python hl_lines="4"
count_missing = data.isna().sum()
n_rows = len(data)

missing_ratio = (count_missing / n_rows) * 100
print(missing_ratio.round(2))
```

| Column    | Missing Values (%) |
|-----------|--------------------|
| id        | 0.00               |
| age       | 0.00               |
| default   | 19.35              |
| housing   | 2.47               |
| ...       | ...                |
| job       | 0.89               |
| marital   | 0.28               |
| education | 4.10               |
| ...       | ...                |

Compared to the initial observation where we found `#!python 0` 
missing values across the whole data set, it's a stark contrast.

Looking at the attribute *default*, nearly a fifth of the observations are 
missing (19.35 %). Other attributes contain less, yet we still need to handle 
them. Therefore, we explore different strategies to deal with missing values.

???+ info

    Though it might not seem much, being able to detect these missing values 
    will prove invaluable in the future.

    By identifying and properly handling these gaps, we might be able to 
    train a better fitting model as unaddressed missing values can lead to 
    biased predictions. Most importantly, most algorithms can't handle 
    missing values at all.

### Sources

We have extensively covered how to detect missing values but have not 
talked about their possible origins.

The reasons for missing values can be manifold:

- Data collection issues
    - Non-responses in a survey
    - Equipment failures
    - Simple human errors when entering data
- Technical challenges
    - Preprocessing errors (i.e., merging data sets from multiple sources)
- Intentional omissions
    - Privacy concerns or legal restrictions

... or the information is simply not available.

### Drop columns/rows

One simple way to handle missing values is to drop (i.e. remove) the 
respective columns which contain any missing values.

```python
data_dropped = data.dropna(axis=1)
```

`#!python axis=1` specified the columns to be dropped.

To comprehend the impact of this operation, we calculate the number of 
columns that were removed.

```python
print(data.shape[1] - data_dropped.shape[1])
```
This operation removed `#!python 6` out of `#!python 21` columns/attributes. 

???+ question "Remove rows with missing values"

    Contrary, we can leave all columns and instead drop the rows containing 
    missing values.

    1. Use the [`DataFrame.dropna()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html)
    method to remove rows with missing values.
    2. Calculate the number of rows that were removed.

Depending on the data at hand, dropping rows or columns might be a valid 
option if you're dealing with a small number of missing values. However, in 
other cases these operations might lead to a significant loss of information.
Since, we are dealing with a substantial amount of missing values, we are 
looking for more sophisticated ways to handle them.

### Imputation techniques

What about filling in the missing values? The process of replacing missing 
values is called imputation.

![](../../assets/data-science/data/imputation.gif)
<figcaption style="text-align: center;">
    Data imputation
</figcaption>

There are various imputation techniques available, each with its own
advantages and disadvantages.

##### Fill manually

Of course, there is always the option to fill the values manually which 
could be time-consuming and infeasible for large data sets.

##### Global constant

The simplest way to impute missing values is to replace them with a global
constant, i.e., filling gaps across ^^all^^ columns with the same value.

```python
data_filled = data.fillna("no")
```

This method is straightforward and easy to implement. However, there are 
some drawbacks:

- how to choose the global constant?
- introduces further challenges with mixed attributes (i.e., 
  nominal/ordinal and numerical attributes)

##### Central tendency

Another common approach is to replace missing values with the mean, median,
or mode of the respective column.

Fill a nominal attribute with the mode:

```python
job_mode = data["job"].mode()
print(job_mode)

data["job"] = data["job"].fillna(job_mode[0])
```

```title=">>> Output"
0    admin.
```

Fill a numerical attribute with the mean:

```python
age_mean = data["age"].mean()
print(age_mean)

data["age"] = data["age"].fillna(age_mean)
```

```title=">>> Output"
np.float64(40.1433299389002)
```

???+ info

    Since the bank data does not contain any numerical attribute with 
    missing values, the above code snippet assumed gaps in *age*. As there 
    are none, the operation did not change the data. 

#### Machine Learning

Lastly, we can use machine learning algorithms to predict the missing values.
The idea is to estimate the missing values based on the other attributes. 
Linear regression, k-nearest neighbors, or decision trees are common choices.

???+ info

    As we have not covered machine learning yet, we won't get into the details.
    But feel free to return to this section. Especially, 
    [this](https://scikit-learn.org/stable/auto_examples/impute/plot_missing_values.html)
    scikit-learn comparison of imputation techniques (including k-nearest 
    neighbors) is a good starting point for further exploration.

## Transformation

Step by step, we are getting closer to actually train a machine learning 
model. Beforehand, we introduce data transformations that are commonly applied
to improve the fit of the model.

For starters, install the `scikit-learn` package within your activated 
environment.

```bash
pip install scikit-learn
```

<div style="text-align: center;">
    <iframe src="https://giphy.com/embed/xT5LMxAxpGSb5AZt8A" width="480" height="362" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/season-5-the-simpsons-5x8-xT5LMxAxpGSb5AZt8A"></a></p>
    <figcaption>
        <code>scikit-learn</code> the swiss-army knife for data 
        preprocessing and machine learning in Python.
    </figcaption>
</div>

From now on, we will heavily use `scikit-learn`'s functionalities.

### Discretize numerical attributes

When dealing with noisy data, it is often beneficial to discretize 
numerical (continuous) attributes.

???+ "Noise in data"

    Noise is a random error or variance in a measured variable. It is 
    meaningless information that can distort the data.
    
    Noise can be identified using basic statistical methods and 
    visualization techniques like boxplots or scatter plots.

The process of discretizing is called binning. I.e., the continuous data 
is separated into intervals (bins).
Bins can generally lead to a smoothing effect which in turn reduce the noise.

As an example, we pick the attribute *age* and visualize it with a boxplot.

<div style="text-align: center;">
    <iframe src="/assets/data-science/data/age-boxplot.html" width="350px" height="500px">
    </iframe>
</div>

??? tip "Create a static boxplot"

    To create a static version of the boxplot, perfect for a quick overview:
      
    ```python
    import matplotlib.pyplot as plt
    
    data["age"].plot(kind="box")  # (1)!
    plt.show()
    ```
    
    1.  The `#!python plot()` method uses `matplotlib` as backend.
  
    <div style="text-align: center;">
        <img src="/assets/data-science/data/age-boxplot.svg" alt="Age boxplot">
    </div>

Since, *age* contains outliers, we discretize the attribute *age* into five 
^^equal^^ sized bins.

```python
from sklearn.preprocessing import KBinsDiscretizer

bins = KBinsDiscretizer(n_bins=5, strategy="uniform", encode="ordinal")
bins.fit(data[["age"]])
bins.transform(data[["age"]])
```

Though the actual binning is just two three lines of code, we have a couple of 
things to dissect.

???+ tip "Working with `scikit-learn`"

    Although the package is named `scikit-learn`, it is imported as 
    `#!python import sklearn`. Package names on 
    [PyPI (Python Package Index)](../../python/packages.md/#pypi)
    can be different from the import name.

    ---

    `scikit-learn` frequently uses classes (e.g., `KBinsDiscretizer`)
    to represent different models and preprocessing techniques. Two important 
    methods that many of these classes implement are `fit` and `transform`.

    - `#!python fit(X)`: This method is used to learn the parameters from the 
    data (referred to as `X`). 
    
    - `#!python transform(X)`: This method is used to apply the learned 
    parameters to the data :fontawesome-solid-arrow-right: `X`.

    Put simply, think about the `#!python fit(X)` method as scikit-learn takes 
    a look at the data and learns from it. The `#!python transform(X)` 
    method then transfers this knowledge and applies it to the data.

    The `#!python fit_transform()` method combines both of these steps in one.
