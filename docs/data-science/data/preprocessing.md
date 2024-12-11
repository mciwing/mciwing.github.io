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
