# Comparisons & Logical operators

## Comparisons

Now, that we have covered all basic `Python` types, we can start comparing them.
As the name suggests, comparisons are used to compare two values. The result 
of a comparison is a boolean value.

### Equality

```py
print("Abc" == "abc")
```

... which evaluates to

```
False
```

We can compare any type with each other. In the above case, the comparison 
checks if both strings are equal, using the `==` operator. The result is 
`False`, because the case of the strings do not match.

Let's check if two integers are equal:

```py
print(1 == 1)  # True
```

### Inequality

We can also check if two values are **not** equal with the `!=` operator:

```py
user_name = "Eric"
print(user_name != "admin") # True
```

```py
print(2 != 2.1) # True
print(2 != 2)   # False
```

### Numerical comparisons

... are done with:

| Operator | Description           |
|----------|-----------------------|
| `<`      | less than             |
| `>`      | greater than          |
| `<=`     | less than or equal    |
| `>=`     | greater than or equal |

```py
print(1 < 2)  # True
print(1 > 2)  # False

print(10.2 <= 10.2)  # True
print(9.99 >= 10)  # False
```

## Logical Operators

You may want to check multiple conditions at the same time. For example,
sometimes you might need two conditions to evaluate to `True` in 
order to perform an action. Hence, **logical operators** are introduced. 
There are three logical operators:

| Operator | Meaning                                           | Example         | Result  |
|----------|---------------------------------------------------|-----------------|---------|
| `and`    | Returns `True` if both statements are `True`      | `True and True` | `True`  |
| `or`     | Returns `True` if one of the statements is `True` | `True or False` | `True`  |
| `not`    | Reverses a result                                 | `not True`      | `False` |

### `and`

```py
age = 20
print(age >= 18 and age <= 25) # True and True -> True
```

### `or`

```py
age = 20
print(age >= 50 or age <= 25) # False or True -> True
```

### `not`

```py
age = 20
print(not(age >= 18)) # not(True) -> False
```

