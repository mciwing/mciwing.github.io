# Comparisons & Logical operators

## Comparisons

Now, that we have covered all basic `Python` types, we can start comparing them.
As the name suggests, comparisons are used to compare two values. The result 
of a comparison is a boolean value.

### Equality

```py
print("Abc" == "abc")
```

```title=">>> Output"
False
```

We can compare any type with each other. In the above case, the comparison 
checks if both strings are equal, using the `==` operator. The result is 
`False`, because the case of the strings do not match.

Let's check if two integers are equal:

```py
print(1 == 1)
```

```title=">>> Output"
True
```

### Inequality

We can also check if two values are **not** equal with the `!=` operator:

```py
user_name = "Eric"
print(user_name != "admin")
```

```title=">>> Output"
True
```

```py
print(2 != 2.1)
print(2 != 2)
```

```title=">>> Output"
True
False
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
print(1 < 2)
print(1 > 2)
```

```title=">>> Output"
True
False
```

```py
print(10.2 <= 10.2)
print(9.99 >= 10)
```

```title=">>> Output"
True
False
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

```title=">>> Output"
True
```

### `or`

```py
age = 20
print(age >= 50 or age <= 25) # False or True -> True
```

```title=">>> Output"
True
```

### `not`

```py
age = 20
print(not(age >= 18)) # not(True) -> False
```

```title=">>> Output"
False
```

---


???+ question "Password strength: Part 1"
    
    <figure markdown="span">
      ![Secure lock](https://preview.redd.it/j7i00nnpx6211.jpg?width=640&crop=smart&auto=webp&s=d4b58226076d45f0c637fd3789d3ccb547a4a54a){ width=50% }
    </figure>

    It's your time to check if a password meets certain requirements. 
    Use the following defined variables `password_length` and 
    `has_special_characters` to evaluate if the password is secure.

    ```py
    password_length = 18
    has_special_characters = False
    ```

    The password is secure if:

    - it exceeds a certain length (10 characters)
    - and contains special characters.

    Use comparison together with logical operators to solve the task.

???+ question "Password strength: Part 2"

    To increase security, a third variable is introduced, namely 
    `already_used` which is a boolean value and indicates whether the password 
    was already in use. Now, check if all of these requirements are met:

    - Has more than 10 characters
    - Contains special characters
    - and was not already used before

    ```py
    password_length = 18
    has_special_characters = True
    already_used = False
    ```

## Recap

We have covered the basic comparison and logical operators in `Python` 
:fontawesome-brands-python:.

- Comparisons
    - `==` for equality
    - `!=` for inequality
    - `<`, `>`, `<=`, `>=` for numerical comparisons
  
- Logical operators
    - `and`
    - `or`
    - `not`