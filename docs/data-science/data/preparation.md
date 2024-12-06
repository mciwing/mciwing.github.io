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

[Bank Marketing :fontawesome-solid-download:](../../assets/data-science/data/bank.txt){ .md-button }
[Bank Marketing Social Features :fontawesome-solid-download:](../../assets/data-science/data/bank-social.csv){ .md-button }

Place the files in a new folder called `data`. Your project now should look 
like this:

```
📁 bank_marketing/
├── 📁 .venv/
├── 📁 data/
├───── 📄 bank.txt
└───── 📄 bank-social.csv
```
