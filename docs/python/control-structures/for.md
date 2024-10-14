# Loops - `#!python for`

## Introduction

In this section, you’ll learn how to loop through elements using just a few
lines of code. Looping allows you to take the same action, or set of actions
with every item in an iterable. Among iterables are for example, lists or
dictionaries. As a result, you'll be able to streamline tedious tasks. First,
we'll loop over lists.

## Looping over lists

You’ll often want to run through all entries in a `#!python list`, performing the same
task with each item. In the below example, we loop through a `#!python list` of passwords
and print the length of each one.

````py
passwords = ["1234", "password", "admin", "123456"]
for password in passwords:
    print(f"Password: {password} is {len(password)} characters long.")
````

```title=">>> Output"
Password: 1234 is 4 characters long.
Password: password is 8 characters long.
Password: admin is 5 characters long.
Password: 123456 is 6 characters long.
```

A loop is written with the `#!python for` statement. The `#!python password` is
a temporary variable that holds the current item in the `#!python list`. You can 
choose any name you want for the temporary variable that holds each value. 
However, it’s helpful to choose a meaningful name that represents a single item
from the `#!python list`. For example:

````
for experiment in experiments:
    ...
for user in users:
    ...
````

???+ info

    When you’re using loops for the first time, keep in mind that the set 
    of steps is repeated once for each item in the `#!python list`, no matter 
    how many items are in the `#!python list`. If you have a million items 
    in your `#!python list`, `Python` repeats these steps a million times.

## Scope

Python uses indentation (whitespace) to indicate, what is part of the loop. 
With an indentation being four characters of whitespace. For a faster way to 
intend, use the tab key ++tab++.

Let's extend the example from above:

```py
passwords = ["1234", "password", "admin", "123456"]
for password in passwords:
    print(f"Password: {password} is {len(password)} characters long.")

print("All passwords have been checked.")
```

```title=">>> Output"
Password: 1234 is 4 characters long.
Password: password is 8 characters long.
Password: admin is 5 characters long.
Password: 123456 is 6 characters long.
All passwords have been checked.
```

You can easily see that only the first `#!python print` statement is part of 
the loop, simply because it is indented. The second `#!python print` statement
is executed after the loop has finished as it is outside the loop.

### `#!python IndentationError`

In longer programs, you’ll notice blocks of code indented at a few different
levels. These indentation levels help you gain a general sense of the overall
program’s organization.

As you begin to write code that relies on proper indentation, you’ll need to
watch for a few common indentation errors.

#### Expected indentation

```py hl_lines="2"
for number in [1, 2, 3]:
print(number)
```

```pytb
  Cell In[4], line 2
    print(number)
    ^
IndentationError: expected an indented block after 'for' statement on line 1
```

As the `#!python IndentationError` states, `Python` expects an indented 
block of code after the `#!python for` statement.

#### Unexpected indentation

```py hl_lines="2"
message = "Hello"
    print(message)
```

```pytb
  Cell In[9], line 2
    print(message)
    ^
IndentationError: unexpected indent
```

In this case, the code snippet contains an unnecessary indentation.

???+ question "Square numbers"
    
    Square each number in a given list and print the result.
    First, initialize a list of numbers from 1 to 10. Square each number and
    `#!python print` it. Use a `#!python for` loop.


## `#!python range()`

The `#!python range()` function makes it easy to generate a series of numbers. 
For example, you can use `#!python range()` to print a series of numbers like
this:

```py
for value in range(3):
  print(value)
```

```title=">>> Output"
0
1
2
```

Remember, that `Python` 'starts counting at `#!python 0`'. `#!python 3` is not 
included in the output, as `#!python range()` generates a sequence up to, but not including, the
number you provide. You can also pass two arguments to `#!python range()`, the first and
the last number of the sequence. In this case, the sequence will start at the
first number and end at the last number minus one.

```py
for value in range(3, 6):
    print(value)
```

```title=">>> Output"
3
4
5
```

???+ question "`#!python range()`"

    Use `#!python range()` to build a `#!python list` which holds the numbers
    from 15 to 20 - including 20.


???+ question "Savings account growth"

    Write a `#!python for` loop to calculate the growth of savings over a 
    period of time. Use following formula to calculate the future value of 
    savings in year $t$:

    $$
    \text{A} = \text{P} \times \left(1 + \frac{\text{r}}{100} \right)^{\text{t}}
    $$
    
    where:

    - $\text{A}$ is the future value of the savings account or investment.
    - $\text{P}$ is the present value of the savings account or investment.
    - $\text{r}$ is the annual interest rate.
    - $\text{t}$ is the number of years the money is invested for.
    
    Given values:
    
    - $\text{P} = 1000$
      - $\text{r} = 5$
    
    Print the future value of the savings account over a period of 10 years. 
    Skip each second year. Use 
    [Python's documentation on range()](https://docs.python.org/3.12/library/stdtypes.html#range)
    as a starting point.

## Detour: Simple statistics on lists with numbers

A few functions are specific to lists of numbers. For example, you
can easily find the minimum, maximum, and sum of a list of numbers:

```py
numbers = [1.0, 8.38, 3.14, 7.0, 2.71]
print(
    f"Minimum: {min(numbers)}",
    f"Maximum: {max(numbers)}",
    f"Sum: {sum(numbers)}", sep="\n"
)
```

```title=">>> Output"
Minimum: 1.0
Maximum: 8.38
Sum: 22.23
```

???+ question "Calculate the average"

    Calculate the average of the following list:
    ```py
    numbers = [4.52, 3.14, 2.71, 1.0, 8.38]
    ```

## List comprehensions

... are a concise way to create lists.

A list comprehension combines a `#!python for` loop to create a new list in
a single line.


???+ question "Rewrite a list comprehension"

    Rewrite the following list comprehension in a regular for-loop to 
    achieve the same result:
    
    ```py
    squares = [value**2 for value in range(1,11)]
    print(squares)
    ```

    ```title=">>> Output"
    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    ```

## Looping over dictionaries

As previously discussed, you can not only loop over a `#!python list`, but 
also iterate over a variety of different data types, such as dictionaries.
You can loop over a dictionary’s key-value pairs, solely over the keys 
or just the values.

### `#!python items()`

Using the `.items()` method, we can loop over the key-value pairs. Take note,
that the method returns two values, which we store in
two separate variables (`key` and `value`).

We can freely choose the variable names in the `#!python for`-loop. It does 
not have to be `key` and `value` respectively.

```py hl_lines="7"
parts = {
    "P100": "Bolt",
    "P200": "Screw",
    "P300": "Hinge",
}

for key, value in parts.items():
    print(key, value)
```

```title=">>> Output"
P100 Bolt
P200 Screw
P300 Hinge
```

### `#!python values()`, `#!python keys()`

???+ question "Dictionary methods"

    Define a (non-empty) dictionary of your choice and use both methods
    `.values()` and `.keys()` to access solely values and keys respectively.

## Recap

With the introduction of the `#!python for` loop, you can now start to 
automate re-occurring tasks. We have covered:

- Looping over lists
- Indentation and possible resulting `#!python IndentationError`
- `#!python range()` to generate a series of numbers
- Simple statistics on lists of numbers
- List comprehensions
- Specific methods to loop over dictionaries
