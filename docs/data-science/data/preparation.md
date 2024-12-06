# Data preparation

## Preface

???+ info

    Starting with this chapter, we will work with data from:
    
    ^^S. Moro, P. Cortez and P. Rita (2014). *A Data-Driven Approach to 
    Predict the Success of Bank Telemarketing*[^1]^^
    
    [^1]:
        Decision Support Systems, Volume 62, June 2014, Pages 22-31:
        [https://doi.org/10.1016/j.dss.2014.03.001](https://doi.org/10.1016/j.dss.2014.03.001)
    
    The publicly available dataset is from a Portuguese retail bank 
    and houses information on direct marketing campaigns (phone calls). Bank 
    customers were contacted and asked to subscribe to a term deposit. Using 
    this practical example, we will explore the realms of:
    
    - Data merging
    - Data cleaning
    - Data transformation
    - Machine learning (with selected algorithms)
    - Comparison of model performance
    - Model persistence (practical guide on how to save and load machine 
      learning models)
    
      Eventually, you will end up with a model that predicts whether a customer
      will subscribe to a term deposit or not.

## Obtaining the data

???+ tip "Set up a project"

    As always, we strongly recommend to set up a new project *including* a 
    virtual environment. We will perform all steps from data merging to 
    saving the model in this project.

    If you are having trouble setting up a virtual environment, please refer 
    to the [virtual environment creation](../../python-extensive/packages.md#create-a-virtual-environment) 
    guide.

Let's dive right in and download both files:

[Bank Marketing :fontawesome-solid-download:](../../assets/data-science/data/bank.tsv){ .md-button }
[Bank Marketing Social Features :fontawesome-solid-download:](../../assets/data-science/data/bank-social.csv){ .md-button }

Place the files in a new folder called `data`. Your project now should look 
like this:

```
📁 bank_marketing/
├── 📁 .venv/
├── 📁 data/
├───── 📄 bank.tsv
└───── 📄 bank-social.csv
```

???+ question "Open the files"

    Before we start, open the files simply with a text editor
    to get a first impression of the data. Scroll through both files and 
    read a couple of rows to get acquainted with the data.

## Read the files

Since we are obviously dealing with two files, we need to read them both 
with `Python` :fontawesome-brands-python:. At the end of this section we 
want to end up with a single (clean!) data set.

???+ info
    
    Conveniently, in our case the data was already collected, saving us hours 
    and hours of work. Thus, we can focus on the data preparation step. 
    Since data is commonly obtained from different sources and in various 
    different formats, both data sets we have at hand (`bank.tsv` and `bank-social.csv`)
    will mimic theses scenarios.

To start, we are using `pandas` for reading and manipulating data. If you 
haven't already, install the package within your environment. 
Assuming your Jupyter Notebook or script is located at the project's root, we
start by reading the first file :fontawesome-solid-arrow-right: `bank.tsv`.

```python
import pandas as pd

data = pd.read_csv("data/bank.tsv", sep="\t")
```

Although, we can use a simple single-liner to read the file, there are a 
couple of things to break down:

1. We are dealing with a tab-separated file, meaning values within the file 
   are separated by a tab character (`\t`). The fact that we are dealing 
   with a tab-separated file is indicated by the file extension `.tsv` and 
   the space surrounding the values within the file.
2. Although we do not have a `csv` file at hand `pandas` is versatile enough 
   to handle different separators. 
   Thus, we can utilize the `#!python pd.read_csv()` function to read the 
   file. ==Tip==: All sorts of text files can be usually read with 
   `#!python pd.read_csv()`.
3. Lastly, the `sep` parameter is set to `\t` to indicate the tab 
   separation.

Let's read the second file :fontawesome-solid-arrow-right: `bank-social.csv`.

<?quiz?>
question: Open the file `bank-social.csv` with your text editor. Which separator is used in the file?
answer: : (colon)
answer: None, it is not a valid csv file.
answer-correct: ; (semicolon)
answer: , (comma)
content:
<p>Exactly, values are separated by a semicolon.</p>
<?/quiz?>

???+ question "Read the second file"
    
    Simply read the second file (`bank-social.csv`) with `pd.read_csv()` 
    and specify the appropriate seperator.
