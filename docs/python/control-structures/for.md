# `#!python for`

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

```py
for number in [1, 2, 3]:
print(number)
```

```title=">>> Output"
  Cell In[4], line 2
    print(number)
    ^
IndentationError: expected an indented block after 'for' statement on line 1
```

As the `#!python IndentationError` states, `Python` expects an indented 
block of code after the `#!python for` statement.

#### Unexpected indentation

```py
message = "Hello"
    print(message)
```

```title=">>> Output"
  Cell In[9], line 2
    print(message)
    ^
IndentationError: unexpected indent
```

In this case, the code snippet contains an unnecessary indentation.
