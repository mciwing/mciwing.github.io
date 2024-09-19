# Boolean and None

In this section, we introduce two more data types, namely boolean (`#!python 
bool`) and None (`#!python NoneType`). Let's start with the latter one, `#!
python NoneType`.

## None (`NoneType`)

`#!python NoneType` is a special data type in Python that represents the absence
of a value.

```py
nothing = None
print(type(nothing))
```

... which outputs:

```
<class 'NoneType'>
```

`#!python None` can be used as a placeholder for a variable which will be
assigned a value later on. Furthermore, if a program was not able to return 
a value, `#!python None` can be used as a return value. 

Later, `#!python None` will play a bigger role.
For now, we simply keep in mind that `#!python None` is a thing.


### Detour: `#!python TypeError`

Often, you’ll want to use a variable’s value within a message. For example, say
you want to wish someone a happy birthday. You might write code like this:

```py
age = 23
message = "Happy " + age + "rd Birthday!"
print(message)
```

... results in.

```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-17-80a141e301d6> in <cell line: 2>()
      1 age = 23
----> 2 message = "Happy " + age + "rd Birthday!"
      3 print(message)

TypeError: can only concatenate str (not "int") to str
```

You might expect this code to print the simple birthday greeting, `Happy
23rd birthday!`. But if you run this code, you’ll see that it generates an 
error.

This is a `#!python TypeError`. It means Python encounters an unexpected 
type in `age`, as strings were mixed with integers in the expression.

When you use integers within strings like this, you need to specify explicitly 
that you want Python to use the integer as a string of characters. 
You can do this by wrapping the variable in the `#!python str()`
function, which tells `Python` to represent non-string values as strings:

```py
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)
```

Changing the type of `age` to string is called casting.

???+ info


    A `#!python TypeError` can stem from various 'sources'. This is just one 
    common example.

In the following example the integers `#!python 3` and `#!python 2` were 
implicitly cast to floating point numbers, to calculate the result, 
which is a floating point number.

```py
print(type(3 / 2))
```

```
<class 'float'>
```

With the function `#!python int()` any value can be explicitly cast into an 
integer, if possible. The value to be cast is passed as the input parameter.

```py
number = 3.0
print(type(number)) # <class 'float'>

# casting
number = int(number)
print(type(number)) # <class 'int'>
```

To explicitly cast a value into a float, use the function `#!python float()`.

???+ question "Casting"
    
    For each of the given variables, check whether you can cast them to
    another type. First, print the type of each variable. Then, use
    `#!python int()`, and `#!python float()` to cast the variables.
    
    ```py
    # variables
    first = "12"
    second = "1.2"
    third = 12
    ```

???+ note

    Remember the f-string (`#!python f"..."`) from the previous section?
    Try a slightly modified example from above.

    ```py hl_lines="2"
    age = 23
    message = f"Happy {age}rd Birthday!"
    print(message)
    ```
    
    You'll notice, that there's no need for any explicit casting of `age`.

    Whenver, you want to include a variable in a string, remember that 
    f-strings might be more convenient. 😉

---

## Booleans

Computers work with binary (e.g. `#!python True` or `#!python False`).
Such information can be stored in a single bit. A boolean is either
`#!python True` or `#!python False`. Booleans are often used to keep 
track of certain conditions, such as whether a game is running or whether a 
user can edit certain content on a website:

```py
game_active = True
can_edit = False

print(type(True))
```

```
<class 'bool'>
```

## Recap

In this section, we have introduced two more data types in Python:

- None (`#!python NoneType`)
- and Booleans (`#!python bool`)

Now, we have covered all basic types! 🎉 With that knowledge, we can already 
start to do comparisons and logical operations.
