# Package Management :material-package-variant:

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
formats and it offers a lot of functionality to manipulate and even plot your
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
First, we have to import the package with the following command:

```py hl_lines="1"
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
on your system open a new terminal within VSC by navigating in the menu bar 
`Terminal` :octicons-arrow-right-24: `New Terminal` 

<figure markdown="span">
  ![Terminal](../assets/python/package/terminal.png){ width=100% }
  <figcaption>VSC Terminal</figcaption>
</figure>


and execute the following command:

```
pip
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
    
    You can run shell commands directly from your notebook by using an 
    exclamation mark (`!`) as a prefix (e.g., `!pip`). However, in some cases,
    such as when uninstalling a package, this approach may cause issues. 
    Therefore, it's often recommended to use the terminal instead.

Now, we'll install our first package, called [`seaborn`](https://seaborn.pydata.org/).
To install a package use pip's `install` command followed by the package name 
(`pip install <package-name>`).
Don't worry, it might take a couple of seconds.

```
pip install seaborn
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

    Remove the `seaborn` package. Like above, use `pip` within a terminal to 
    list all commands and find the appropriate one. Execute the command 
    to remove the package.

### PyPI

<figure markdown="span">
  ![PyPI logo](https://pypi.org/static/images/logo-large.516e776d.svg){ width="75%" }
</figure>

You might wonder where `pip` downloads the packages?! In short, all packages
are downloaded from the [Python Package Index (PyPI)](https://pypi.org/).
That's where the open-source community (usually) publishes their packages.
Simply put, if you type `pip install seaborn`, `pip` looks for a package called
`seaborn` on PyPI and downloads it. `PyPI` is a valuable resource if you're
searching for packages, certain versions, etc.

## Virtual environments

Previously, we have installed the package `seaborn`. The package itself was
available system-wide as we did not create a virtual environment beforehand.
That might not sound too bad, but it's actually considered bad practice. But
what is good practice and what the heck is a virtual environment?

To answer the latter, simply put, a virtual environment is a folder which
encapsulates all packages for a specific project. Each project should have its
own virtual environment. With a package manager like `pip`, you install the
necessary packages into the project's virtual environment. `pip` lets you
manage these packages/dependencies.

### Why?

To summarize, the `pip`/virtual environment combination facilitates:

- **Dependency management**: You can keep track of the packages that your
  project needs to function.
- **Version management**: You can specify the exact versions of a package that
  your project needs. This is important, because different versions of a 
  package may have different functionalities or bugs.
- **Environment management**: It's easier to work on multiple projects on a
  single machine as you can install multiple versions of a package on a
  per-project basis.
- **Shareable**: Your projects will be shareable with other developers as they
  can easily install all dependencies with a single command. No more it worked
  on my machine excuses!

<blockquote class="reddit-embed-bq" style="height:500px" data-embed-height="740"><a href="https://www.reddit.com/r/ProgrammerHumor/comments/70we66/it_works_on_my_machine/">It works on my machine...</a><br> by<a href="https://www.reddit.com/user/Shaheenthebean/">u/Shaheenthebean</a> in<a href="https://www.reddit.com/r/ProgrammerHumor/">ProgrammerHumor</a></blockquote><script async="" src="https://embed.reddit.com/widgets.js" charset="UTF-8"></script>

### How?

#### Create a virtual environment

To create a virtual environment, open a new command prompt within VSCode (you
can use the shortcut ++ctrl++ + `ö`).

Execute the following command:

```bash
python -m venv .venv
```

This command creates a new folder structure. The folder is called `.venv`.
Instead of `.venv` you can choose any name you want. However, this section
assumes that you named it `.venv`.

#### Activate a environment

Now, we have to activate the environment in order to use it. Depending on your
operating system, the command is slightly different.

---

=== "Windows :fontawesome-brands-windows:"
  
    As a Windows user type

    ```
    .venv\Scripts\activate
    ```
    
    If an error occurs ("the execution of scripts is deactivated on this 
    system") run
    
    ```
    Set-ExecutionPolicy Unrestricted -Scope Process
    ```
    
    ... and use the previous command again.

=== "macOS/Linux :fontawesome-brands-apple:/:fontawesome-brands-linux:"

    Type

    ```bash
    source .venv/bin/activate
    ```
    
    to activate your environment.

---

#### Deactivate a environment

Deactivating the environment is the same on all operating systems.
To deactivate it, simply use

```
deactivate
```

in your command prompt/terminal.

---

???+ question "Fit a machine learning model"

    Assuming your virtual environment is activated, try to get the following
    code cell running. 
 
    ```py
    # Taken from https://scikit-learn.org/stable/auto_examples/tree/plot_unveil_tree_structure.html#train-tree-classifier

    # pyplot is a submodule of matplotlib and can be directly imported with the `from` statement
    from matplotlib import pyplot 
    
    # or you can import functions (like load_iris()) directly from its submodule (datasets)
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    from sklearn.tree import DecisionTreeClassifier, plot_tree
    
    iris = load_iris()
    X = iris.data
    y = iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    
    clf = DecisionTreeClassifier(max_leaf_nodes=3, random_state=0)
    clf.fit(X_train, y_train)
    
    plot_tree(clf)
    pyplot.show()
    ```

    Install the packages `matplotlib` and `scikit-learn` with `pip`.
    Then try to execute the code cell 
    (the code was taken from [here](https://scikit-learn.org/stable/auto_examples/tree/plot_unveil_tree_structure.html#train-tree-classifier)).
   

Congratulations 🎉, you've just fitted a machine learning model (simple decision
tree) on a data set and visualized the model. That's the power of `Python` -
easily accessible packages with a lot of functionality ready to use. 🦾

Don't worry too much about the actual code lines above. Again, the
important thing is to get the code running. With the above exercise, you've 
reproduced the result from the motivational section 
[Why Python?](index.md/#machine-learningai).

### `requirements.txt`

In the following exercise, you will learn how to export all your packages 
(your project's dependencies) to a file. We will cover a simple command that 
facilitates sharing your project/code with co-developers.

???+ question "Export dependencies"

    Assume you want to share the code snippet from the previous task with 
    someone. First, your colleague might not know which packages you used to 
    get the code running. With no more information, one has to read the code 
    and manually determine which packages are necessary.
    To circumvent such situations, you export all your packages to a file. 
    Open a command prompt/terminal and execute

    ```bash
    pip freeze > requirements.txt
    ```
    
    A `requirements.txt` is written which contains all your used 
    packages.

Your colleague can now take the file and install all packages needed, at once.

```bash
pip install -r requirements.txt
```
... is the corresponding command.

???+ info

    A `requirements.txt` file is a common way to share project dependencies.
    However, it will also help you, to restore your environment, in case 
    something goes wrong. Hence, keep your requirements file up-to-date.

## Other choices?/Outlook 

Apart from `pip` there are a couple of other package managers available.
For example, there are

* [`uv`](https://docs.astral.sh/uv/)
* [`pipenv`](https://pipenv.pypa.io/en/latest/)
* [`poetry`](https://python-poetry.org/docs/)
* [`miniconda`](https://docs.anaconda.com/miniconda/)

... and this is by no means an extensive list.
All of these tools let you install and manage packages. Nevertheless, they have
their differences. In the end, it is up to you, the developer which tool fits
best. `pip` is always a solid choice (and the go-to choice to get the hang of
package/virtual environment management). However, if you're working on larger
scale projects with a couple of other developers, one of these package managers
might offer some functionalities which facilitates the development workflow.

## Recap

In this section, you have learned how to install packages and manage them 
within virtual environments. The topics covered:

* `pip`
* How to install/uninstall packages
* PyPI - the package hub
* Concept and benefits of virtual environments
* Creation and basic usage of a virtual environment
