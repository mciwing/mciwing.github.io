# List

## Introduction

In `Python`, a container is a type of data structure that holds and organizes
multiple values or objects. Containers are used to store collections of
elements, allowing you to group related data together for easier management and
manipulation. `Python` provides several built-in container types, each with its
own characteristics and use cases. In this first section, we cover 
`#!python list` objects, followed by dictionaries and tuples.

## What Is a `#!python list`?

A `#!python list` is a collection of items. You can make a `#!python list` 
including the letters of the alphabet or the digits from `#!python 0` to 
`#!python 9`. You can put anything you want into a `#!python list` and the
items in your `#!python list` don’t have to be related in any particular way.

Because a `#!python list` usually contains more than one element, it’s a good 
idea to use the plural for a variable of type `#!python list`, such as 
`letters`, `digits`, or `names`.

A `#!python list` is created with an opening and closing square bracket 
`#!python []`.
Individual elements in the `#!python list` are separated by commas. Here’s a 
simple example of a `#!python list`:

```py
beatles = ["John", "Paul", "George", "Ringo"]
print(beatles)
```

which prints:

```
['John', 'Paul', 'George', 'Ringo']
```

```py
print(type([]))  # print the type of an empty list
```

```
<class 'list'>
```

## Accessing elements

You can access any element in a `#!python list` by
using the `index` of the desired item. To access an
element in a `#!python list`, write the name of the `#!python list` followed by
the index of the item enclosed in square brackets. For example, let’s pull out 
the first Beatle in `beatles`:

```py
beatles = ["John", "Paul", "George", "Ringo"]
print(beatles[0])
```

... returns:

```
John
```

## `#!python IndexError`

???+ info

    In Python, index positions **start at 0**, not 1. This is true of most 
    programming languages. If you’re receiving unexpected results, determine 
    whether you are making a simple off-by-one error.


```py
beatles = ["John", "Paul", "George", "Ringo"]
print(beatles[4])
```

... results in

```
Traceback (most recent call last):
  File "<ipython-input-7-68dd8df4c868>", line 2, in <module>
    print(beatles[4])
          ~~~~~~~^^^
IndexError: list index out of range
```

... since there is no official 5<sup>th</sup> Beatle. :fontawesome-solid-guitar:

There is a special syntax for accessing the last element in a list. Use the 
index `#!python -1` to access the last element, `#!python -2` to access the 
second-to-last element, and so on.

```py
beatles = ["John", "Paul", "George", "Ringo"]
print(beatles[-1])  # Ringo
print(beatles[-2])  # George
```

???+ question "Indexing"

    Define a list that stores following programming languages:
    
    - R
    - Python
    - Julia
    - Java
    - C++
    
    
    and use `#!python print()` to output:
    `"My favourite language is Python!"`

