# Integers & Floats

## Integers

`Python` :fontawesome-brands-python: treats numbers in several different ways,
depending on how they are used. Let’s first look at how `Python` manages whole 
numbers called integers (`#!python int`).

Any number **without** decimal places is automatically interpreted as an
integer.

```py
number = 10176
```

We can verify the type of the variable `number` with `#!python type()`.

```py
number = 10176
print(type(number))
```

```
<class 'int'>
```

## Arithmetic operators

Of course, with integers, you can perform basic arithmetic operations.
These are:

| Operator | Description                                            |
|----------|--------------------------------------------------------|
| `+`      | Addition                                               |
| `-`      | Subtraction                                            |
| `*`      | Multiplication                                         |
| `/`      | Division                                               |
| `**`     | Exponentiation                                         |
| `%`      | Modulo (Used to calculate the remainder of a division) |
| `//`     | Floor division                                         |


```py
# Modulo
20 % 3 # = 2

# Floor division
20 // 3 # = 6
```

Moreover, you can use multiple operations in one expression. You can also
use parentheses to modify the order of operations so Python can evaluate your 
expression in the order you specify. For example:

```py
2 + 3 * 4 # = 14
```

```py
(2 + 3) * 4 # = 20
```

---

## Floats

Any number with decimal places is automatically interpreted as a `#!python 
float`.

```py
number = 10176.0
print(type(number))
```

```
<class 'float'>
```

All previously introduced arithmetic operations can be used for floats as well.

```py
3.0 + 4.5
# operations with floats and integers
3.0 * (4 / 2)
```

### Limitations

???+ info

    Floats are not 100% precise. "[...] n general, the decimal floating-point 
    numbers you enter are only approximated by the binary floating-point 
    numbers actually stored in the machine." (The Python Tutorial, 2024)[^1]
    [^1]: [The Python Tutorial](https://docs.python.org/3/tutorial/floatingpoint.html#floating-point-arithmetic-issues-and-limitations)
    
    So be aware that these small numerical errors could add up in complex 
    calculations.

```py
print(34.3 + 56.4)
```

... results in

```
90.69999999999999
```

???+ task "Calculate the BEP"

    Use variables and arithmetic operations to calculate the break-even point (the number of units that need to be sold to cover the costs) for a product. The break-even point is given as:

    $$
    \text{BEP (units)} = \frac{\text{Fixed Costs}}{\text{Price per Unit} - \text{Variable Cost per Unit}}
    $$
    
    Calculate the $\text{BEP}$ for the following values:

    - **Fixed Costs**: 30000
    - **Variable Cost per Unit**: 45
    - **Price per Unit**: 75
    
    Assign each given value to a variable. Print the result in a sentence, e.g. `The break-even point is 200 units.`


## Recap

This section was all about numbers in Python. We have covered:

- Whole numbers :octicons-arrow-right-24: `#!python int`
- Decimal numbers :octicons-arrow-right-24: `#!python float`
- Floating-point arithmetic issues and limitations

Next up, we will introduce the `#!python bool` and `#!python NoneType` type in
Python.