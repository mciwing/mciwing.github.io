# Strings

So far, we have already stored some text in a variable. For example `"Hello 
World!"` which is called a string. A string is a primitive data type. Integer, 
float, boolean and None are also primitive data types which we will cover 
later.

A string is simply a series of characters. Anything inside quotes is considered
a string in `Python`, and you can use single (`'`) or double quotes (`"`)
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

```py
text = 'I told my friend, "Python is my favorite language!"'
print(text)
```

## `type()`

Let's check the type of the variable `text`.

```py
text = "The language 'Python' is named after Monty Python, not the snake."
print(type(text))
```

which results in:

```
<class 'str'>
```

`type()` comes in handy to check the type of variables. In this case, we 
can verify that `text` is indeed a string.

???+ info

    It is advisable to consistently enclose your strings with either single 
    `'...'` or double quotes `"..."`. This will make your code easier 
    to read and maintain.