# Tabular data

With a couple of practical examples, we will discover tips on how to work with
tabular data, where to find it, and the various sources and formats you
can explore. This chapter will guide you through working with different types
of structured data, enabling you to extract, transform, and analyze information
from multiple sources.

???+ info
    
    This chapter is an extension to the previous `pandas` chapter. It 
    should equip you with the necessary skills to acquire data from various 
    different sources.

Our journey will cover a selection of following topics:

1. Excel: Learn how to read spreadsheets
2. Web Scraping: Extract tables directly from online sources
3. File Writing: Save your data to disk
4. Various Sources: An incomplete list of data sources

## Prerequisites

For this chapter we recommend to create a new project. Additionally, create 
a new virtual environment and **activate** it.

You should end up with a project structure similar to:

```
📁 tabular/
├── 📁 .venv/
└── 📄 tabular_data.ipynb
```

## :fontawesome-solid-file-excel: Excel

Let's start off with arguably the most common data source: Excel spreadsheets.

<div style="text-align: center;">
    <img src="https://miro.medium.com/v2/resize:fit:640/format:webp/1*FAzumPnvzKUDolMG7SNcHw.png" alt="I Excel in Excel" width="370"/>
</div>

Reading Excel files can be straightforward, ==if they are properly structured==.
However, if you see files like these...

![](../../assets/python-extensive/data/tabular/awesome-excel.PNG)

... run, or it will take you several days to parse the file. :winking_face:

Although, the example might exaggerate, it is not uncommon to encounter 
spreadsheets that are easily readable by humans but hard to parse by machines.
Like in the example, the title, empty rows and columns, merged cells, 
column names spanning multiple lines, pictures and other formatting can 
make it difficult to extract the data in a structured manner.

### Reading Excel files

Download the following (structured) file to get started:

<div class="center-button" markdown>
[Student data :fontawesome-solid-download:](../../assets/python-extensive/data/tabular/fhsstud.xlsx){ .md-button }
</div>

Data source: Statistik Austria - data.statistik.gv.at[^1]

[^1]:
    [Studien an Fachhochschulen](https://data.statistik.gv.at/web/meta.jsp?dataset=OGD_fhsstud_ext_FHS_S_1)
    At the time of writing (December 2024), the data was last updated on 
    2024-07-25.

Place the file within your project directory. The data set contains the 
number of students enrolled at universities of applied sciences in Austria 
per semester. 

If you are an MCI student, you are part of this data set!

??? info "Interested in the creation of the Excel?"
    
    Since, Statistik Austria provides the data across three files, a
    `Python` :fontawesome-brands-python: script was used to merge everything 
    into a single Excel. Below you can find the code snippet:

    ```python
    # Data from:
    # https://data.statistik.gv.at/web/meta.jsp?dataset=OGD_fhsstud_ext_FHS_S_1
    import pandas as pd
    
    students = pd.read_csv("OGD_fhsstud_ext_FHS_S_1.csv", sep=";")
    semester = pd.read_csv(
        "OGD_fhsstud_ext_FHS_S_1_C-SEMESTER-0.csv",
        sep=";",
        usecols=["code", "name"],
    )
    header = pd.read_csv(
        "OGD_fhsstud_ext_FHS_S_1_HEADER.csv", sep=";", usecols=["code", "name"]
    )
    
    # replace column codes with their corresponding names
    students = students.rename(
        columns={row["code"]: row["name"] for _, row in header.iterrows()}
    )
    # replace semester codes with their descriptions
    students.Berichtssemester = students.Berichtssemester.replace(
        {row["code"]: row["name"] for _, row in semester.iterrows()}
    )
    
    # get term
    students["Semester"] = students.Berichtssemester.str.split(" ").str[0]
    
    # write Excel
    students.to_excel("fhsstud.xlsx", index=False)
    ```

---

To read the Excel file, we will use `pandas` in conjunction with `openpyxl` 
(to read and write Excel files):

```bash
pip install pandas openpyxl
```

???+ tip

    You can install multiple packages with a single command. Simply 
    separate the pacakge name with a space.

To read the file, it's as simple as:

```python
import pandas as pd

data = pd.read_excel("fhsstud.xlsx")
```

As the file is structured, the data loads without any issues. 

#### Reading specific sheets

By default, [`#!python pd.read_excel()`](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html)
loads the first sheet. If you want to read another sheet, you can specify it 
with the `sheet_name` parameter:

???+ question "Create and read a new sheet"

    1. Open `fhsstud.xlsx` within Excel. 
    2. Manually create a new sheet and fill it with some data of your choice.
    3. Save the file.
    4. Read the new sheet with `pd.read_excel()`.

#### Detour: Visualize enrolled students

To further consolidate your visualization skills, obtained in the 
[Plotting](../plotting.md) chapter, we create a simple plot to visualize the 
total of newly enrolled students per winter term in Austria.

<div style="text-align: center;">
    <iframe
        src="/assets/python-extensive/data/tabular/winter-term.html" 
        width="100%" height="450">
    </iframe>
</div>

On a side note, it's quite interesting that the numbers are steadily rising, 
with a dip in the winter term 2022/23.

???+ question "Create a static version of the plot"

    Recreate the above plot with `pandas` and `matplotlib` as backend. 
    It does ^^not^^ have to be the same colors, background, title etc.

    1. Subset the data by winter term.
    2. Create a suitable plot (e.g., line plot, area plot).

### Writing Excel files

You can't just easily read Excel files, but also write them.

```python
data.to_excel("fhsstud_copy.xlsx", index=False)  # (1)!
```

1. The `#!python index=False` parameter omits the index to be written to the 
   file. Have a look at your `DataFrame`'s index with `#!python data.index`.

Or you can write multiple sheets:

```python hl_lines="1"
with pd.ExcelWriter("fhsstud_multiple.xlsx") as writer:
    data.to_excel(writer, sheet_name="Students", index=False)
    data.to_excel(writer, sheet_name="Students-Copy", index=False)
```

Although the same data is written to two different named sheets, you should 
get the idea.

#### `#!python with` statement

The `#!python with` statement is used to wrap the execution of a block of code.
It is commonly used for resource management, such as opening files or managing
database connections, ensuring that resources are properly cleaned up after use

In the above example, the `#!python with` statement is used to open an Excel
file for writing and ensures that the Excel writer is properly closed after
writing the data.

## Web Scraping

Web scraping is a technique to extract data from websites. It can be used to
extract structured data from HTML pages, such as tables.

To illustrate web scraping, we pick an example from Wikipedia as our 
HTML. We use the english article of the 
[ATX (Austrian Traded Index)](https://en.wikipedia.org/wiki/Austrian_Traded_Index)
to retrieve a data set with all companies listed in the ATX.

???+ question "Visit the article"

    1. Open a new browser tab and visit the 
    [ATX Wikipedia article](https://en.wikipedia.org/wiki/Austrian_Traded_Index).
    2. Open the source code of the page, the HTML code.
    To do so, right-click on the page and select `View page source`. 
    Alternatively, use the shortcut ++ctrl+u++.
    Simply scroll through the HTML code a bit.

You might have noticed that the HTML code is quite complex. Nevertheless, 
we can easily extract all the tables on the page with `pandas`:

```python
tables = pd.read_html("https://en.wikipedia.org/wiki/Austrian_Traded_Index")
print(type(tables))
```

```title=">>> Output"
<class 'list'>
```

Simply by passing the URL to `#!python pd.read_html()`, we get a list
of `DataFrame` objects. Each `DataFrame` corresponds to a table found on the
page.

The second table on the page contains the companies listed in the ATX. 
Let's have a look:

```python
atx_companies = tables[1]
print(atx_companies.head())
```

| Company    | Industry                    | Sector                             |
|------------|-----------------------------|------------------------------------|
| Erste Bank | Financials                  | Banking                            |
| Verbund    | Utilities                   | Electric Utilities                 |
| OMV        | Basic Industries            | Oil & Gas                          |
| BAWAG      | Financials                  | Banking                            |
| Andritz    | Industrial Goods & Services | Industrial Engineering & Machinery |

The resulting `DataFrame` `atx_companies` can be perfectly used as is, 
without any further data cleaning.

???+ tip

    The `#!python pd.read_html()` function is a powerful tool to extract 
    tables from HTML pages. However, it might not always work out of the 
    box by simply passing a URL.
    Most websites have a complex structure, and the tables might not be
    directly accessible. In such cases, you might need to use a more
    sophisticated web scraping packages like
    
    - [`BeautifulSoup`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
    - [`Scrapy`](https://docs.scrapy.org/en/latest/)
    - [`Selenium`](https://selenium-python.readthedocs.io/)

???+ info

    Be nice to the websites you scrape, seriously! Always check the website's
    `robots.txt` file to see if web scraping is allowed. For example, 
    Wikipedia's `robots.txt` file can be found at 
    [https://en.wikipedia.org/robots.txt](https://en.wikipedia.org/robots.txt).

    Respect the website's terms of service and don't overload the 
    server with requests.

## File Writing

So far we have written data solely to Excel files. However, `pandas` supports
a variety of file formats for writing data. Using the `atx_companies` data 
set, we explore two more useful file formats.

### :fontawesome-solid-file-csv: CSV

Writing to a CSV (Comma Separated Values) file is as simple as:

```python
atx_companies.to_csv("atx_companies.csv", index=False)
```

???+ tip

    If you are dealing with large data sets, you might want to consider 
    compressing the output file and thus reducing the file size.

    Simply pass a compression algorithm as `#!python str` (e.g.,`#!python "gzip"`),
    to the `compression` parameter:
    
    ```python
    atx_companies.to_csv("atx_companies.csv.gz", index=False, compression="gzip")
    ```
    
    To read a compressed file:
        
    ```python
    _atx_companies = pd.read_csv("atx_companies.csv.gz", compression="gzip")
    ```
    
    Have a look at the documentation of 
    [`DataFrame.to_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html)
    for further options.

### LaTeX

Including your data in a LaTeX document can be easily achieved with:
    
```python
atx_companies.to_latex("atx_companies.tex", index=False)
```

???+ info "Additional dependency"

    To use the LaTeX export functionality, `Jinja2` is required.

    ```bash
    pip install Jinja2
    ```

Since CSV and LaTeX formats are just a fraction of the supported file formats,
navigate to [panda's Input/Output](https://pandas.pydata.org/docs/reference/io.html)
section for further reference. 

## Data Sources

Apart from Excel files and web scraping, there are numerous other 
online sources where you can find structured data. Here are a 
couple of further links to explore:

- [data.gv.at](https://www.data.gv.at/) - Open government data from Austria 
  covering various topics like economy, environment, and society.
- [data.statistik.gv.at](https://data.statistik.gv.at/web/catalog.jsp) - 
  Statistics Austria portal for open data ranging from population, 
  environment to economy and tourism.
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php) -
  Popular data repository for machine learning, hosting classic data sets 
  from various domains.
- [Kaggle](https://www.kaggle.com/datasets) - A platform owned by Google to 
  share data sets, models and code. Although kaggle is free to access, you need
  to create an account to download data sets.
- [Google Dataset Search](https://datasetsearch.research.google.com/) - 
  Google's search engine for data sets. It helps you find data sets stored 
  across the web.
