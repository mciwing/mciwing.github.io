# Strings

So far, we have already stored some text in a variable. For example 
`#!python "Hello World!"` which is called a string. A string is a primitive data
type. Integer, float, boolean and None are also primitive data types which we 
will cover later.

A string is simply a series of characters. Anything inside quotes is considered
a string in `Python`, and you can use single (`#!python '`) or double 
quotes (`#!python "`)
around your strings like this:

```py
text = "This is a string."
another_text = 'This is also a string.'
```

This flexibility allows you to use quotes and apostrophes within your strings:

```py
text = "One of Python's strengths is its diverse and supportive community."
print(text)
```

```title=">>> Output"
One of Python's strengths is its diverse and supportive community.
```

```py
text = 'I told my friend, "Python is my favorite language!"'
print(text)
```

```title=">>> Output"
I told my friend, "Python is my favorite language!"
```

## `#!python type()`

Let's check the type of the variable `text`.

```py
text = "The language 'Python' is named after Monty Python, not the snake."
print(type(text))
```

```title=">>> Output"
<class 'str'>
```

`#!python type()` comes in handy to check the type of variables. In this 
case, we can verify that `text` is indeed a string. Just like 
`#!python print()`, `#!python type()` 
is an important tool in your programming arsenal.

???+ info

    It is advisable to consistently enclose your strings with either single 
    `#!python '...'` or double quotes `#!python "..."`. This will make your 
    code easier to read and maintain.

## String methods

One of the simplest string manipulation, is to change the case of 
the words in a string.

```py hl_lines="2"
name = "paul atreides"
print(name.title())
```

```title=">>> Output"
Paul Atreides
```

A method is an action performed on an object (in our case the 
variable). The dot (.) in `#!python name.title()` tells `Python` to 
make the `#!python title()` method act on the variable `name` which holds 
the value `#!python "paul atreides"`.

Every method is followed by a set of parentheses, because methods often need
additional information to do their work. That information is
provided inside the parentheses. The `#!python title()` method doesn’t need
any additional information, so its parentheses are empty.

### Methods vs. functions

We have already encountered functions like `#!python print()` and `#!python 
type()`. Functions are standalone entities that perform a specific task.

On the other hand, methods are associated with objects. In this case, the 
`#!python title()` method is associated with the string object `name`.

???+ question "String methods"

    You start with the variable `input_string` that holds the value 
    `#!python "fEyD rAuThA"`. 

    ```py
    input_string = "fEyD rAuThA"
    ```

    Experiment and apply a combination of the following methods:

    - `capitalize()`
    - `istitle()`
    - `isupper()`
    - `upper()`
    - `lower()`

    Eventually you should end up with the string `#!python "Feyd Rautha"`, 
    print it.
    
## Concatenation

It’s often useful to combine strings. For example, you might want to store
first and last name in separate variables, and then combine them when
you want to display someone’s full name.

Python uses the plus symbol (`#!python +`) to combine strings. In this 
example, we use `#!python +` to create a full name by combining a 
`first_name`, a space, and a `last_name`:

```py
first_name = "paul"
last_name = "atreides"
full_name = first_name + " " + last_name
print(full_name)
```

```title=">>> Output"
paul atreides
```

Here, the full name is used in a sentence that greets the user, and
the `title()` method is used to format the name appropriately. This code
returns a simple but nicely formatted greeting:

```py
full_name = "paul atreides"
print("Hello, " + full_name.title() + "!")
```

```title=">>> Output"
Hello, Paul Atreides!
```

Another way to nicely format strings is by using f-strings. To achieve the same
result as above, simply put an `#!python f"..."` in front of the string and use 
curly braces `{}` to insert the variables. 

```py
full_name = "Alia Atreides"

print(f"Hello, {full_name}!")

# you can even apply methods directly to the variables 
# (within the curly braces)
print(f"Hello, {full_name.lower()}!")
```

```title=">>> Output"
Hello, Alia Atreides!
Hello, alia atreides!
```

???+ question "A quote"

    Find a quote from a famous person you admire. Store the 
    quote and name in variables and print both with an f-string.

    Your output should look something like the following, 
    including the quotation marks: 
    
    `Frank Herbert (Dune opening quote): "I must not fear. Fear is the 
    mind-killer."`

## Recap

This section was all about strings, we have covered:

- Creation of strings
- Usage of `#!python type()`
- String methods
- Methods vs. functions
- Concatenation

Next, up we will introduce numbers in Python, namely integers and floats. 
