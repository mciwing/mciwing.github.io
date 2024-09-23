# More control structures

## Introduction

In this section, we will cover additional control structures. First, we 
discuss the `#!python if` statement, which allows us to execute code based on a 
condition. Followed by the `#!python elif`, `#!python else` and 
`#!python while` statements.

## `#!python if`

The `#!python if` statement lets you evaluate conditions. The simplest kind of 
`#!python if` statement has one condition and one action. Here is some 
pseudocode:

```
if condition is True:
    do something
```

You can put any condition in the first line and just about any action in the 
indented block following the test. If the condition evaluates to `True`,
`Python` executes the code following the `#!python if` statement. 
If the test evaluates to `False`, the code following the `#!python if` is ignored.

```py
age = 27

if age >= 18:
  print("You're allowed to enter")
```

```title=">>> Output"
You're allowed to enter
```

First, the condition `#!python age > 18` is evaluated. If it evaluates to 
`#!python True`, the 
indented print is executed. If the condition evaluates to `#!python False`, 
the indented code block is ignored.

Indentation plays the same role in `#!python if` statements as it did in 
`#!python for` loops (see the [previous section](for.md#indentationerror)).

???+ question "Password strength"

    <figure markdown="span">
      ![Secure lock](https://preview.redd.it/j7i00nnpx6211.jpg?width=640&crop=smart&auto=webp&s=d4b58226076d45f0c637fd3789d3ccb547a4a54a){ width=50% }
    </figure>

    In the section on [comparisons and logical operators](../comparisons_and_logic.md#not),
    you had to check whether a password meets
    certain criterias. The following example expands on this task as you are 
    given a list of passwords.
    You have to check if each password **exceeds** a length of 12 characters.

    Execute the first code cell to generate some random passwords 
    (note every time you rerun the code snippet, different passwords will be 
    generated).

    ```py
    # generate passwords - simply execute the code to generate some random
    # passwords
    import random
    import string
    
    passwords = []
    for i in range(10):
        length = random.randint(3, 25)
        password = "".join(random.choices(string.ascii_letters, k=length))
        passwords.append(password)
    ```

    The `#!python list` `passwords` should look something like this:
    
    ```
    ['PWgOYxQgnxgXm',
     'gpOMVTmCSjAcndowkUd',
     'ADKIEthzsGBr',
     'VRLzOIZtEz',
     'uOckmTJjeonUyMlnG',
     'gjOpWuHrIbG',
     'doxIylbRkNLdvdLNgVgYsDGzd',
     'KvUdsgZhPIrS',
     'LrdpffEqlBVQYr',
     'ncyqXNLnVstVxlx']
    ```
    
    Now, loop over the passwords and check if each password exceeds the 
    character limit of 12. If so, print the password.
    