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
`Python` executes the indented code following the `#!python if` statement. 
If the test evaluates to `False`, the indented code block (following the 
`#!python if`) is ignored.

```py
user = "admin"

if user == "admin":
  print(f"Welcome {user}!")
```

```title=">>> Output"
Welcome admin!
```

First, the condition `#!python user == "admin"` is evaluated. If it 
evaluates to `#!python True`, the indented print is executed. If the condition
evaluates to `#!python False`, the indented code block is ignored.

Indentation plays the same role in `#!python if` statements as it did in 
`#!python for` loops (see the [previous section](for.md#indentationerror)).

???+ question "Password strength: Part 1"

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

### `#!python else`

Previously, every time the condition in the `#!python if` statement 
evaluated to `#!python False`, 
no action was taken. Hence, the `#!python else` clause is introduced which 
allows you to define a set of actions that are executed when the conditional
test fails.

```py
user = "random_user"

if user == "admin":
  print(f"Welcome {user}!")
else:
  print("Only admins can enter this area!")
```

```title=">>> Output"
Only admins can enter this area!
```

???+ question "Password strength: Part 2"
    
    Let's expand on our previous example. Re-use your code to check the length
    of the generated passwords. Now, we would like to store all passwords that
    did not meet our criteria in the empty list `invalid_passwords`.

    *Hint*: Introduce an `else` statement to save the invalid passwords.

### `#!python elif`

Often, you’ll need to test more than two possible situations, and to evaluate
these, you can use an `if-elif-else` syntax. `Python` executes only one
block in an `if-elif-else` chain. It runs each conditional test in order until
one passes. When a test passes, the code following that test is executed and
the rest is skipped.

```py hl_lines="12"
user = "xX_user_Xx"
registered_users = [
    "admin",
    "guest",
    "SwiftShark22",
    "FierceFalcon66",
    "BraveWolf11"
]

if user == "admin":
  print(f"Welcome {user}!")
elif user not in registered_users:
  print("Please create an account first!")
else:
  print("Only admins can enter this area!")
```

```title=">>> Output"
Please create an account first!
```

???+ info
    
    As you might have noticed, you can use a single `#!python if` statement or
    `#!python if` in combination with `#!python else`. For multiple conditions 
    you can add as many `#!python elif` parts as you wish.

## `#!python while`

The `#!python for` loop takes an iterable and executes a block of 
code once for each element. In contrast, the `#!python while` loop runs as 
long as a certain condition is `#!python True`.

For instance, you can use a `#!python while` loop to count up through a 
series of numbers. Here is an example:

```py hl_lines="4"
# set a counter
current_number = 1

while current_number <= 5:
  print(current_number)
  # increment the counter value by one
  current_number += 1
```

```title=">>> Output"
1
2
3
4
5
```

Note, that the variable, that is checked in the `#!python while`-condition 
must be defined prior to the loop, otherwise we will encounter a 
`#!python NameError`.

???+ info "Addition assignment"

    In the above example, we used the `#!python +=` operator, referred to as 
    addition assignment. It is a shorthand for incrementing a variable by a 
    certain value.

    ```py hl_lines="2"
    a = 10
    a += 5
    print(a)
    ```

    ```title=">>> Output"
    15
    ```
    
    The above code is equivalent to `#!python a = a + 5`.
    This shorthand assignment can be used with all arithmetic
    operators, such as subtraction `#!python -=` or division `#!python /=`.


???+ question "While loop"
    
    Write some code, to print all **even** numbers up to 42 using a while 
    loop.

## Detour: User input

Most programs are written to solve an end user’s problem. To do so, usually 
we need to get some information from the user. For a simple example, let’s 
say someone wants to enter a username.

You can store the user input in the variable `user_name` like in the example 
below.

```py
user_name = input("Please enter your username:")
```


## `#!python break`

To exit any loop immediately without running any remaining code, use the 
`#!python break` statement. The `#!python break` statement directs the flow of 
your program; you can use it to control which lines of code are executed and 
which aren’t, so the program only executes code that you want it to, when you
want it to.

````py hl_lines="3"
for i in range(5):
    if i == 3:
        break
    print(i)
````

```title=">>> Output"
0
1
2
```

## `#!python continue`

Rather than breaking out of a loop entirely, you can use the `#!python continue` 
statement to return to the beginning of the loop based on the result of a 
condition.

```py hl_lines="3"
for i in range(5):
    if i == 3:
        continue
    print(i)
```

```title=">>> Output"
0
1
2
4
```

## Recap

In this section we have expanded on control structures. We discussed:

- `#!python if` statements and how to use them
- `#!python else` clauses
- `#!python elif` statements for multiple conditions
- `#!python while` loops
- `#!python break` and `#!python continue` statements for more 'fine-grained'
  control
