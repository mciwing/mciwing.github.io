# Variables

???+ info

    The structure of following sections is based on the official [Python
    tutorial](https://docs.python.org/3/tutorial/index.html).

    A huge thank you goes to [@jhumci](https://github.com/jhumci) for providing
    the initial resource materials!

## Getting started

---

<span style="color: red;">
  :fontawesome-solid-circle-exclamation:
  Important
  :fontawesome-solid-circle-exclamation:
</span>

We encourage you to execute **all** upcoming code snippets on your machine.
You can easily copy each code snippet to your clipboard, by clicking the icon
in the top right corner. By doing so, you will be prepared for all upcoming
tasks within the sections. Tasks are indicated by a
:fontawesome-solid-circle-question:-icon.

We recommend to create a new notebook for each chapter, e.g. create
`variables.ipynb` for this chapter. Doing so, your notebooks will follow
the structure of this crash course.

---

Let's start with the first task.

???+ question "Notebook + first code cell"

    Create a new Jupyter notebook and name it `variables.ipynb`.
    Paste the following code snippet into a new cell and execute it.

    ```python
    print("Hello World!")
    ```
    
    The output should be:

    ```title=">>> Output"
    Hello World!
    ```

???+ info "Code blocks & Output"
    
    The upcoming content contains a lot of code snippets. They are easily 
    recognizable due to their colourful syntax highlighting, such as:
    
    ```py
    print(1+1)
    ```

    Code snippets are an integral part, to illustrate concepts, which are 
    introduced and explained along the way. Commonly, these code snippets are
    accompanied by an output block to display the result, for instance:

    ```title=">>> Output"
    2
    ```

    Nevertheless note, output blocks can be missing as there is not always 
    an explicit result.

    Again, execute and experiment with all code snippets on your machine to 
    verify the results and get familiar with `Python` 
    :fontawesome-brands-python:!

## Variable

Computers can store lots of information. To do so, in `Python` :fontawesome-brands-python:
we use variables. A variable is a name that refers to a value. Following code
snippet, assigns the value `#!python 4` to the variable `number`. In 
general, you pick the variable name on the left hand side, assign a value 
with `=` and the value itself is on the right hand side.

```py
number = 4
```

You can change the value of a variable in your program at any time, and
Python will always keep track of its current value.

```py
number = 4
number = 4000
```

You will notice that none of the cells had any output. To display the value
of a variable we use the `#!python print()` function.

### `#!python print()`

```py
number = 4
print(number)
```

```title=">>> Output"
4
```

Now, we can also verify that in the above snippet the value of `number` was
actually changed.

```py
number = 4
print(number)
number = 4000
print(number)
```

```title=">>> Output"
4
4000
```

???+ info

    Within a notebook, the variables are stored in the background and can be 
    overwritten at any time. Therefore, it is good practice to execute all 
    cells from top to bottom of the notebook in the right order so that 
    nothing unexpected is stored in a variable.

### Comments

Comments exist within your code but are not executed. They are used to
describe your code and are ignored by the `Python` interpreter. Comments
are prefaced by a `#!python #`.

```py
# this is a comment
print("Hello World!")
```

```title=">>> Output"
Hello World!
```

???+ info

    Comments help you and others understand what your code is doing. It is
    good practice to use comments as a tool for documentation.

### Variable naming

When you’re using variables in `Python`, you need to adhere to a few rules and
guidelines. Breaking some of these rules will cause errors; other guidelines
just help you write code that’s easier to read and understand. Be sure to keep
the following rules in mind:

- Variable names are lower case and can contain only letters, numbers, and
  underscores.
  They can start with a letter or an underscore, but not with a number.
  For instance, you can call a variable `message_1` but not `1_message`.
- Whitespace is not allowed in variable names, but an underscores `_` can be
  used to separate words in variable names. For example, `greeting_message`
  works, but `greeting message` won't.
- Avoid using `Python` keywords and function names as variable names;
  that is, do not use words that `Python` has reserved for a particular
  programmatic purpose, such as the word `print`.
- Variable names should be short but descriptive. For example, `name` is better
  than `n`, `student_name` is better than `s_n`, and `name_length` is better
  than `length_of_persons_name`.

### Errors (`#!python NameError`)

Every programmer makes mistakes and even after years of experience, mistakes
are part of the process. With time, you get more efficient in debugging
those errors.

<blockquote class="reddit-embed-bq" style="height:500px" data-embed-height="670"><a href="https://www.reddit.com/r/ProgrammerHumor/comments/thzuhm/debugging_tactics/">Debugging tactics</a><br> by<a href="https://www.reddit.com/user/0ajs0jas/">u/0ajs0jas</a> in<a href="https://www.reddit.com/r/ProgrammerHumor/">ProgrammerHumor</a></blockquote><script async="" src="https://embed.reddit.com/widgets.js" charset="UTF-8"></script>

Let’s look at an error you’re likely to make early on and learn how to fix it.
We’ll write some code that generates an error on purpose. Copy the code and
run your cell.

```py
message = "Hello Python Crash Course reader!"
print(mesage)
```

Which should result in:

```
NameError: name 'mesage' is not defined
```

When an error occurs in your program, the `Python` interpreter does its best to
help you figure out where the problem is. The interpreter provides a traceback
which is a record of where the interpreter ran into trouble when trying to
execute your code.
Here’s an example of the traceback that `Python` provides, after you’ve
accidentally misspelled a variable’s name:

```pytb
Traceback (most recent call last):
  File "C:\\IPython\core\interactiveshell.py", line 3577, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-35-c8f2adeaed02>", line 2, in <module>
    print(mesage)
          ^^^^^^
NameError: name 'mesage' is not defined. Did you mean: 'message'?
```

The output reports that an error occurs in *line 2*. The interpreter shows this
line to help us spot the error quickly and tells us what kind of error it
found. In this case, it found a `#!python NameError` and reports that
the variable `mesage` has not been defined. A name error usually means we made
a spelling mistake when entering the variable’s name or that the variable
simply does not exist.

???+ question "Your first fix"

    Fix the `#!python NameError` in your code cell.

## Recap

In this section, we have covered variables in `Python`
:fontawesome-brands-python:.

You have learned (about):

- To create and assign a value to a variable.
- `#!python print()` to display the value of a variable.
- Comments
- Naming conventions for variables.
- How to fix a `#!python NameError`.