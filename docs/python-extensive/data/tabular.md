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

Our journey will cover selected data acquisition methods:

1. Excel: Learn how to read spreadsheets
2. Web Scraping: Extract tables directly from online sources
3. Database: First interaction with a local database

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

Download the following file to get started:

<div class="center-button" markdown>
[Student data :fontawesome-solid-download:](../../assets/python-extensive/data/tabular/fh-students.xlsx){ .md-button }
</div>
