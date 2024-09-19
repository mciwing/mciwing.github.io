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


```py hl_lines="2"
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

There is a special syntax for accessing the last element in a `#!python list`.
Use the index `#!python -1` to access the last element, `#!python -2` to access
the second-to-last element, and so on.

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

## List manipulation

`Python` provides several ways to add or remove data to existing lists.

### Adding elements

The simplest way to add a new element to a `#!python list`, is to append it. 
When you append an item to a `#!python list`, the new element is added at 
the end.

```py hl_lines="3"
numbers = [1, 2, 3]
print(numbers)
numbers.append(4)
print(numbers)
```

... prints:

```
[1, 2, 3]
[1, 2, 3, 4]
```

The `#!python append()` method makes it easy to build lists dynamically. For
example, you can start with an empty `#!python list` and then add items by 
repeatedly calling `#!python append()`.

```py hl_lines="2-4"
numbers = [1.0, 2.0, 0.5]
numbers.append(4.0)
numbers.append(3.0)
numbers.append("one hundred")

print(numbers)
```

```
[1.0, 2.0, 0.5, 4.0, 3.0, 'one hundred']
```

Up until now, our lists contained only one type of elements - strings. However,
as in the example above, you can store multiple different types of data in a
`#!python list`. Moreover, you can do nesting (for example, you can store a 
`#!python list` within a `#!python list` - more on that later). Hence, 
lists can represent complex data structures.
Nevertheless, don't mix and match every imaginable data type within a single 
`#!python list` (just because you can) as it makes the handling of your 
`#!python list` quite difficult.

???+ info

    Later, we will learn how to perform the same task without repeatedly 
    calling the same `#!python append()` method over and over.

### Inserting elements

You can add a new element at **any position** in your `#!python list` by using
the `#!python insert()` method. You do this by specifying the index of the new
element and the value of the new item.

```py hl_lines="2"
pokemon = ["Charmander", "Charizard"]
pokemon.insert(1, "Charmeleon")
print(pokemon)
```

which gives:

```
['Charmander', 'Charmeleon', 'Charizard']
```

### Removing elements

To remove an item from a `#!python list`, you can use the `#!python remove()` 
method. You need to specify the value which you want to remove. However, 
this it will only remove the first occurrence of the item.

```py hl_lines="2"
pokemon = ["Charmander", "Squirtle", "Charmeleon", "Charizard", "Squirtle"]
pokemon.remove("Squirtle")
print(pokemon)
```

... prints:

```
['Charmander', 'Charmeleon', 'Charizard', 'Squirtle']
```

### Popping elements

Sometimes you’ll want to use the value of an item after you remove it from a
`#!python list`. The `#!python pop()` method removes a specified element of a 
`#!python list`. Additionally, the item is returned so you can work with that 
item after removing it. 

The term pop comes from thinking of a `#!python list` as a stack of items and
popping one item off the top of the stack. In this analogy, the top of a stack 
corresponds to the end of a `#!python list`.

```py hl_lines="2"
pokemon = ["Charmander", "Charmeleon", "Bulbasaur", "Charizard"]
bulbasaur = pokemon.pop(2)
print(pokemon)
print(bulbasaur)
```

... prints:

```
['Charmander', 'Charmeleon', 'Charizard']
Bulbasaur
```

???+ question "List manipulation"

    Define a `#!python list` with a couple of elements (of your choice). Play
    around with the methods `#!python append()`, `#!python insert()`, 
    `#!python remove()` and `#!python pop()`. Print the `#!python list` after 
    each operation to see the changes.