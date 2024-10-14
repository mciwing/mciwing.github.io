# Dictionaries

In this section, you’ll learn how to use dictionaries which allow you
to connect pieces of related information. Dictionaries let you model a
variety of real-world objects more accurately. We will create, modify and 
access elements of a dictionary.

## Creating a dictionary

```py
experiment = {"description": "resource optimization"}
print(type(experiment))
```

Above code snippet creates a simple dictionary and prints its type:

```title=">>> Output"
<class 'dict'>
```

In `Python`, a dictionary is wrapped in curly braces (`{}`), with a series 
of key-value pairs inside the braces. Each key is connected to a value, and 
you can use a key to access the value associated with that key. 
A key’s value can be any type, like a string, integer, list, or even 
another dictionary. In the above example, the key is `#!python "description"` 
and its value `#!python "resource optimization"`

Every key is connected to its value by a colon. Individual key-value pairs
are separated by commas. You can store as many key-value pairs as you want in a
dictionary.

```py
experiment = {
    "description": "resource optimization",
    "sample_weight_in_grams": 5,
}
```

## Accessing values

To get the value associated with a key, give the name of the dictionary and
then place the key inside a set of square brackets.

```py
experiment = {"sample_weight_in_grams": 5}
print(experiment["sample_weight_in_grams"])
```

```title=">>> Output"
5
```

???+ question "Create a dictionary"

    Manage the cost of raw materials in a dictionary. The dictionary should 
    contain the following key-value pairs:

    - `#!python "steel"`: `#!python 100`
    - `#!python "aluminium"`: `#!python 150`
    - `#!python "copper"`: `#!python 200`
    - `#!python "plastic"`: `#!python 50`
  
    Create the dictionary and print the price of copper.

## Adding key-value pairs

You can add new key-value pairs to a dictionary at any time. For example, 
to add a new key-value pair, you would give the name of the dictionary followed
by the new key in square brackets along with the new value.

```py
experiment = {}
experiment["description"] = "resource optimization"
print(experiment)
```

In the above example, we start with an empty dictionary and add a key-value
pair to it.

```title=">>> Output"
{'description': 'resource optimization'}
```

However, we can't add the same key a second time to the dictionary. **Every key
is unique within the dictionary**.

## Modifying values

Values can be overwritten:

```py
experiment = {"sample_weight_in_grams": 10}
experiment["sample_weight_in_grams"] = 10.2
```

## Removing key-value pairs

We can remove key-value-pairs using the key and the `#!python del` statement:

```py hl_lines="8"
experiment = {
    "supervisor": "Alex",
    "sample_weight_in_grams": 10,
}

print(experiment)

del experiment["supervisor"]

print(experiment)
```

```title=">>> Output"
{'supervisor': 'Alex', 'sample_weight_in_grams': 10}
{'sample_weight_in_grams': 10}
```

???+ question "Modify a dictionary"

    Remember that a value can hold any data type? You are given a dictionary with
    production data.
    
    ```py
    production = {
        "singapore": {"steel": 100, "aluminium": 150},
        "taipeh": {"steel": 200, "aluminium": 250},
        "linz": {"steel": 300, "aluminium": 350, "copper": 100},
    }
    ```
    
    Each key represents a location and has another dictionary as value. This
    dictionary contains the production quantity of different materials.
    
    - Remove `linz` from the dictionary.
    - Add a new location `vienna` with the production of 200 steel 
    and 250 aluminium.
    - Print the `aluminium` value of `taipeh` (try accessing it step
    by step and use variables for each step).

???+ info

    At first, the above example might seem a bit too overcomplicated. However, 
    nesting (in this example: storing a dictionary within a dictionary) is 
    common practice and as already discussed, lets you represent more 
    complex data structures. Even databases like [Redis](https://redis.io/)
    and [MongoDB](https://www.mongodb.com/) are at it's core key value
    stores, just like our dictionary above.


## Recap

We have covered following topics in this section:

- Dictionaries store key-value pairs.
- How to get and modify values
- Adding key-value pairs
- Removing key-value pairs with `#!python del`

Lastly, as part of the `Containers` topic, we will have a look at tuples.
