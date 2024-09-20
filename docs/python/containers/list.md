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

## Organizing a `#!python list`

For various reasons, often, your lists will be unordered. If you want to 
present your `#!python list` in a particular order, you can use the method `#!python 
sort()`, or the function `#!python sorted()`.

### `#!python sort()`

The `#!python sort()` method operates on the `#!python list` itself and 
changes its order.

```py hl_lines="2 5"
numbers = [5, 4, 1, 3, 2]
numbers.sort()  # sort in ascending order
print(numbers)

numbers.sort(reverse=True)  # sort in descending order
print(numbers)
```

above code snippet returns:

```
[1, 2, 3, 4, 5]
[5, 4, 3, 2, 1]
```

### `#!python sorted()`

The `#!python sorted()` **function** maintains the original order of a 
`#!python list` and returns a sorted `#!python list` as well.

```py hl_lines="2"
numbers = [5, 4, 1, 3, 2]
sorted_numbers = sorted(numbers)

print(f"Original list: {numbers}; Sorted list: {sorted_numbers}")
```
which prints:

```
Original list: [5, 4, 1, 3, 2]; Sorted list: [1, 2, 3, 4, 5]
```

## Length

You can easily find the length of a `#!python list` with `#!python len()`.

```py
print(len([3.0, 1.23, 0.5]))  # 3
```

## Slicing

To make a slice (part of a `#!python list`), you specify the index of the 
first and last
elements you want to work with. Elements **up until** the second index are 
included. To output the first three elements in a `#!python list`, you would request
indices 0 through 3, which would return elements 0, 1, and 2.

```py
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3])
```

???+ question "Slicing"

    Define a `#!python list` of your choice with at least `#!python 5` 
    elements. 
    
    - Now, perform a slice from the second to (including) the fourth element.
    - Next, omit the first index in the slice (only omit the number!). What 
    happens?
    - Lastly, re-add the first index and omit the second index of your 
    slice. Print the result.

## Copy

To copy a `#!python list`, you can use the `#!python copy()` method.

```py
original_list = [1, 2, 3]
copied_list = original_list.copy()

# perform some changes to both lists
original_list.append(4)
copied_list.insert(0, "zero")

print(f"Original list: {original_list}, Copied list: {copied_list}")
```

which prints:

```
Original list: [1, 2, 3, 4], Copied list: ['zero', 1, 2, 3]
```

### Be careful!

You might wonder why we can't simply do something along the lines of 
`#!python copied_list = original_list`. With lists, we have to be careful, 
as this syntax simply creates a reference to the original `#!python list`.
Let's look at an example:

```py
original_list = [1, 2, 3]
copied_list = original_list

# perform some changes to the original list
original_list.append(4)

print(f"Original list: {original_list}, Copied list: {copied_list}")
```

which leaves us with:
```
Original list: [1, 2, 3, 4], Copied list: [1, 2, 3, 4]
```

As you can see, the changes to the original `#!python list` are reflected in 
the copied one. You can read about this in more detail 
[here](https://realpython.com/pointers-in-python/).


???+ note

    We can actually check whether both lists point to the same object in memory
    by using `#!python id()` which returns the memory address of an object. 
    Just remember, to be careful when copying lists and check if your program 
    behaves as intended!

    ```py
    original_list = [1, 2, 3]
    copied_list = original_list
    
    print(id(original_list) == id(copied_list))  # True
    ```