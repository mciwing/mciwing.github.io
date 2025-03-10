# Data Science in Practice

## Introduction

In this course block and its subsequent chapters we will demonstrate how to 
build a machine learning model in practice. In the end, you will have a 
"ready-to-go" model that can predict whether a bank customer will subscribe 
to a term deposit.

Along the way we will explore useful functionalities of `scikit-learn`, common
pitfalls in data science projects, how to properly save a model, and conclude
with a bonus section on pipelines to automate the entire modelling process.

Let's get started! :rocket:

---

Remember the bank marketing data set that we used to explore in the Data
Preparation & Preprocessing portion and then completely abandoned in the last
couple of chapters? Well, it's time to bring it back!

???+ info
    
    The bank marketing data was adapted from:

    ^^S. Moro, P. Cortez and P. Rita (2014). *A Data-Driven Approach to 
    Predict the Success of Bank Telemarketing*[^1]^^
    
    [^1]:
        Decision Support Systems, Volume 62, June 2014, Pages 22-31:
        [https://doi.org/10.1016/j.dss.2014.03.001](https://doi.org/10.1016/j.dss.2014.03.001)
    
    The publicly available dataset is from a Portuguese retail bank 
    and houses information on direct marketing campaigns (phone calls). Bank 
    customers were contacted and asked to subscribe to a term deposit.

## Prerequisites

### 0. :trophy: What's our goal?

First, let's define the end goal: 

<div style="text-align: center; margin-top: 1em;">
    <p>
        <i>Build a machine learning model that can predict whether a bank 
        customer will subscribe to a term deposit.</i>
    </p>
</div>

???+ tip

    Put simply, a term deposit is a type of bank account where you agree to
    lock away your money for a fixed period of time (the "term") in exchange 
    for a guaranteed interest rate that's typically higher than a regular 
    savings account.

Using information such as clients' demographic details, economic 
indicators, and marketing campaign data, we aim to solve this binary 
classification task.

---

Before we dive in, you have to set up the project which will be used throughout
the remainder of this course.

### 1. :file_folder: Project structure

Start with creating the following project structure:

```plaintext
📁 bank_model/
├── 📁 data/
```

### 2. :down_arrow: Download data

???+ danger

    Since we want to make sure that everyone uses the same initial data set,
    we urge you to re-download it and place it within your `data/` folder.


    <div class="center-button" markdown>
    [Bank marketing :fontawesome-solid-download:](../../assets/data-science/data/bank-merged.csv){ .md-button }
    </div>

    ```plaintext hl_lines="4"
    📁 bank_model/
    ├── 📁 data/
    ├───── 📄 bank-merged.csv
    ```

### 3. :computer: Virtual environment

Create a [virtual environment](../../python/packages.md#create-a-virtual-environment).
Now, you should have the following structure:

```plaintext
📁 bank_model/
├── 📁 .venv/
├── 📁 data/
├───── 📄 bank-merged.csv
```

Be sure to activate the environment!

### 4. :package: Install packages

Install the necessary packages - `pandas` and `scikit-learn`.
