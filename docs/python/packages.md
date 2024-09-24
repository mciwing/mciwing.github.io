# Package management :material-package-variant:

## Introduction

One reason, why `Python` is widespread, is its vibrant community. This community
develops code to solve a variety of problems in the widest range of scientific
fields. This code is bundled and shared for free (as open-source) in the
form of packages. You can download and use these packages. The usage of
packages will facilitate your coding process as they offer implementations to
solve common problems. Therefore, you won't have to reinvent the wheel.

For example the package `pandas` is the go-to tool for data manipulation and
analysis. With `pandas` you can read text and Excel files 
:fontawesome-regular-file-excel: among a lot of other
formats and offers a lot of functionality to manipulate and even plot your
data. Hence, you will rarely see `Python` projects that are not dependent on
`pandas`. Apart from `pandas` there are a wide variety of popular packages:

- [`scipy`](https://scipy.org/) - statistics (which will be covered in the next
  course)
- [`tqdm`](https://tqdm.github.io/) - build progress bars
- [`scikit-learn`](https://scikit-learn.org/stable/) - for machine learning
- [`numpy`](https://numpy.org/) - scientific computing
- ... and many many more

This section serves as a guide on how to install and manage packages.
Additionally, the concept of virtual environments is explained.

## Standard library

`Python` comes with a couple of modules which do not need to be installed and can
be used 'out of the box'. For simplicity, we will call these modules packages
as well. If you're interested in the difference between packages and modules,
Real Python has a nice [article](https://realpython.com/python-modules-packages/)
on the topic. [Here](https://docs.python.org/3/py-modindex.html) is
an extensive list of all the packages that `Python` ships with.

Let's use the `#!python random` package to generate some random numbers. 
First, we have to import the package with following command:

```py
import random

# with the package imported we can use its functions
# e.g., random integer (between 1 and 100)
print(random.randint(1, 100))
```

```title=">>> Output"
42
```

Note, the output will be different when you run the code, since it is random.

The corresponding documentation is
available [here](https://docs.python.org/3/library/random.html#random.randint).
Generally speaking, almost all packages offer an online documentation page. It
is good practice, to consult these documentation sites as they offer a lot of
information on how to use their package and which methods/functions are
available. Usually, functionalities are illustrated with examples that can be a
good starting point for your project.

???+ info

    If you remember, `#!python random` was used in one of the previous 
    sections on [control structures](control-structures/if.md#if) to generate 
    passwords of variable length.


???+ question "Calculate the median"
    
    Use the built-in `#!python statistics` package to calculate the median of 
    the below given values. Use Google to search for the `#!python statistics` 
    documentation page and try to find the appropriate function.

    ```py
    values = [13, 58, 90, 34, 49, 41]
    ```

We will continue with another exercise.

???+ question "Variance of random values"
    
    Generate a list of random values (can be integers and/or floats) and 
    calculate the variance. Hint: Use both the `#!python random` and 
    `#!python statistics` package.

## Installing packages

To get access to all the packages available online, we need to install them
using a package manager. One such manager is `pip` which is 
automatically installed alongside `Python`. To check if `pip` is available 
on your system add following command as a code cell to your Jupyter notebook
and execute it.

```
!pip
```

... you should see a list of commands and their description:

```
Usage:   
  pip <command> [options]

Commands:
  install                     Install packages.
  download                    Download packages.
  uninstall                   Uninstall packages.
  freeze                      Output installed packages in requirements format.
  inspect                     Inspect the python environment.
  list                        List installed packages.
  show                        Show information about installed packages.
...
```

???+ info

    The exlamation mark (!) is used to run shell commands directly from your 
    notebook. Alternatively, if you don't want to enter commands in your
    notebook, open a new command prompt and execute the same command without
    the exclamation mark.

Now, we'll install our first package, called [`seaborn`](https://seaborn.pydata.org/).
To install a package use pip's `install` command followed by the package name 
(`!pip install <package-name>`). Execute the cell.
Don't worry, it might take a couple of seconds.

```
!pip install seaborn
```

`seaborn` is a quite common package to visualize data. Now, run the following
code to create your first plot. The code snippet was copied from the
`seaborn` documentation
[here](https://seaborn.pydata.org/examples/grouped_boxplot.html).

```py
# taken from https://seaborn.pydata.org/examples/grouped_boxplot.html
import seaborn as sns
sns.set_theme(style="ticks", palette="pastel")

# Load the example tips dataset
tips = sns.load_dataset("tips")

# Draw a nested boxplot to show bills by day and time
sns.boxplot(x="day", y="total_bill",
            hue="smoker", palette=["m", "g"],
            data=tips)
sns.despine(offset=10, trim=True)
```

You don't have to fully understand the code snippet. It's more about the
successful usage of a package. You might have noticed, that you didn't solely
install `seaborn`. Among `seaborn`, `pip` also installed `pandas` (for data
handling). We can 'verify' that by checking the type of `tips` (from the code
snippet above).

```py
print(type(tips))
```

```title=">>> Output"
<class 'pandas.core.frame.DataFrame'>
```

Most of the time, a package does not 'stand on its own'. It uses the
functionalities of other packages as well. In our case, `seaborn` also needs
`pandas` to properly function. Hence, a lot of packages are dependent on each
other.

???+ question "Remove a package"

    Remove the `seaborn` package. Use `!pip` within a code cell to list all 
    commands and find the appropriate one. Execute the command within a cell.

<blockquote class="reddit-embed-bq" style="height:500px" data-embed-height="740"><a href="https://www.reddit.com/r/ProgrammerHumor/comments/70we66/it_works_on_my_machine/">It works on my machine...</a><br> by<a href="https://www.reddit.com/user/Shaheenthebean/">u/Shaheenthebean</a> in<a href="https://www.reddit.com/r/ProgrammerHumor/">ProgrammerHumor</a></blockquote><script async="" src="https://embed.reddit.com/widgets.js" charset="UTF-8"></script>
