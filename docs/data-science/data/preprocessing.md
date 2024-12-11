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


| Column      | Missing Values |
|-------------|----------------|
| id          | 0              |
| age         | 0              |
| default     | 0              |
| housing     | 0              |
| loan        | 0              |
| contact     | 0              |
| ...         | ...            |


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
