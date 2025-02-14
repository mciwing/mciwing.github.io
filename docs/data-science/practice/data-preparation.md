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
