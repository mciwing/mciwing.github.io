# Data Basics

This chapter kicks off the foundational building blocks of a data science 
pipeline. We start by taking a closer look at data itself. Understanding 
different attribute types is crucial for choosing appropriate visualizations, 
preprocessing techniques and machine learning algorithms.

???+ question "Create a new project"

    1. For this chapter create a new project. Revisit the 
        [wrap-up](../basics/setup.md#wrap-up) section from the setup guide.
    2. Install the packages `seaborn` and `pandas`

## Tabular Data

Throughout this course, we will primarily work with **tabular data**, simply 
think of spreadsheets. Tabular data is organized in a rectangular 
format with:

- **Rows**: Individual observations or samples (e.g., one student)
- **Columns**: Attributes or features describing each observation (e.g., name,
  age, average grade)

| Name    | Age | Average Grade |
|---------|-----|---------------|
| Claudia | 19  | 1.45          |
| Stefan  | 22  | 3.4           |
| Max     | 20  | 2.12          |

Each row represents one student, while each column contains a specific 
attribute about that student.

Understanding the structure of tabular data is essential because most machine 
learning algorithms expect data in this format. Now let's explore what types 
of information each column can contain.

## Attribute Types

Not all data is created equal. The type of data in each column determines 
what operations we can perform and which visualizations make sense. We 
distinguish between two main categories: numerical and categorical data.

### Numerical (Quantitative)

Numerical data represents measurable quantities, i.e., values you can perform 
mathematical operations on.

```python
import pandas as pd

temperatures = pd.Series([22.5, 18.3, 25.1, 19.8, 23.4])

print(f"Average temperature: {temperatures.mean()}°C")
print(f"Maximum temperature: {temperatures.max()}°C")
```

```title=">>> Output"
Average temperature: 21.82°C
Maximum temperature: 25.1°C
```

Numerical data comes in two types:

**Continuous**: Can take any value within a range, including decimals. 
Examples include temperature (22.5°C), body mass (3750.5g) or height (1.75m).

**Discrete**: Can only take specific, countable values, typically integers. 
Examples include number of students (5) or age (22).

???+ tip

    A simple rule of thumb: If you can meaningfully have fractional values, 
    it's continuous. If counting whole units makes more sense, it's discrete.
