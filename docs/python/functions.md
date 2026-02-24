# Functions

In this section, you’ll learn to write functions, which are named blocks of
code that are designed to do one specific task. If you need to perform
that task multiple times throughout your program, you don’t need to type all
the code for the same task again and again; you just call the function
dedicated to handling that task. By defining functions, your programs will get
easier to write, read, test, and fix.


## Defining a function

Here’s a simple function named `#!python greet_user()` that prints a greeting:

```py
def greet_user():
    print("Hello!")
```

This example shows the simplest structure of a function. With the keyword
`#!python def` we define a function, followed by the name of our function. 
Within the parentheses we can (optionally) specify any information the function
needs to do its job. This information is defined in the form of parameters
(more on that later).

Any indented lines that follow `#!python def greet_user():` make up the body of
the function. The line `#!python print("Hello!")` is the only line of actual
code in the body of this function, so `#!python greet_user()` has just one job:
`#!python print("Hello!")`.

When you want to use a function, you have to call it. To do so, simply
write the function name, followed by any required information in parentheses.

```py
# call the function
greet_user()
```

```title=">>> Output"
Hello!
```

## Detour: docstrings

As previously discussed, it is always good practice to add comments to your
code in order to improve readability. That applies to functions as well. In 
case of functions, one can add a **docstring**, which is essentially a longer 
comment that describes the function. A docstring is written in triple quotes
`#!python """..."""` and is placed directly after the function definition.

```py hl_lines="2"
def greet_user():
    """Display a simple greeting."""
    print("Hello!")
```

Now, you can display the docstring by calling the built-in `#!python help()` 
function with the function name as an argument:

```py
help(greet_user)
```

```title=">>> Output"
Help on function greet_user in module __main__:
greet_user()
    Display a simple greeting.
```

Docstrings facilitate the proper documentation of your code. Most of all, they
will help you in the long run to remember what your code does.

<figure markdown="span">
  ![Meme](https://programmerhumor.io/wp-content/uploads/2024/09/programmerhumor-io-programming-memes-c70b5db2e255e9c.jpe){ width="400" }
</figure>

## Parameters

After some modification, the function `#!python greet_user()` should not only
tell the user "Hello!" but also greet them by name. Therefore, we have to 
define a parameter called `user_name`. Now, each time you call the function, 
you need to pass a `user_name` such as `#!python "admin"` to the function.

```py hl_lines="1 8"
def greet_user(user_name):
    """
    Display a simple greeting.
    Pass a string with the user's name.
    """
    print(f"Hello, {user_name}!")

greet_user("admin")
```

```title=">>> Output"
Hello, admin!
```

???+ info

    As you can see in the example above, a docstring can span multiple lines!

Up until now, the functions had no parameters at all or just a single 
parameter. However, you can define as many parameters as you like, seperated 
by a comma (`#!python ,`):

```py
def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")
```

???+ question "Break-even point"
    
    Remember the task to calculate the break-even point? Now, you'll wrap 
    following formula within a function:
    
    $$
    \text{BEP (units)} = \frac{\text{Fixed Costs}}{\text{Price per Unit} - \text{Variable Cost per Unit}}
    $$
    
    Write a function called `calculate_bep()` that takes the following
    parameters:

    - `fixed_costs`
    - `price_per_unit`
    - `variable_cost_per_unit`
    
    Print the calculation result (break-even point) within the function. 
    Call the function with following arguments:

    ```py
    fixed_costs = 30000
    price_per_unit = 75
    variable_cost_per_unit = 45
    ```

### Terminology :fontawesome-solid-triangle-exclamation:

**parameter vs. argument**

A parameter is the variable inside the parentheses of the function definition -
`#!python def greet_user(user_name):`. Here `user_name` is the parameter. When
you call the function with, for example `#!python greet_user("admin")`, the 
value `"admin"` is referred to as an argument. You can think of the parameter 
as a placeholder and the argument as the actual value.

## Positional arguments

When you call a function, `Python` must match each argument in the function 
call with a parameter in the function definition. The simplest way to do this 
is based on the order of the arguments provided which is referred to as
positional arguments.

```py
def add_numbers(a, b):
    """Add two numbers."""
    print(a + b)

add_numbers(3, 5)
```

```title=">>> Output"
8
```

### Order matters!

You can get unexpected results, if you mix up the order of the arguments in a
function call when using positional arguments:

```py hl_lines="9 11"
def perform_calculation(a, b):
    """Calculate something."""
    print(a + b**b)
    
a = 12
b = 5

# correct order
perform_calculation(a, b)
# incorrect order (produces a different result)
perform_calculation(b, a)
```

```title=">>> Output"
3137
8916100448261
```

Next up, we'll introduce keyword arguments to avoid such mistakes.

## Keyword arguments

A keyword argument is a name-value pair that you pass to a function. You
directly associate the name and the value within the argument, so when you
pass the argument to the function, there’s no confusion.

```py
perform_calculation(a=12, b=5)

#  you can switch the order of the named keyword arguments
perform_calculation(b=5, a=12)
```

No matter the order, the result is the same!

```title=">>> Output"
3137
3137
```

### Default values

When writing a function, you can optionally define a default value for each parameter. If
an argument for a parameter is provided in the function call, `Python` uses the
argument value. If not, the parameter’s default value is used. Using default values can
simplify your function calls and clarify the ways in which your functions are
typically used. Let's look at an example.

```py hl_lines="1 5 8"
def describe_lab(lab_name, lab_supervisor="Miriam"):
    print(f"{lab_name} is supervised by {lab_supervisor}")

# use the default value for lab_supervisor
describe_lab(lab_name="Chemistry")

# provide a value for lab_supervisor
describe_lab(lab_name="IT", lab_supervisor="Alex")
```

```title=">>> Output"
Chemistry is supervised by Miriam
IT is supervised by Alex
```

## Return values

A function doesn’t have to display its output directly with `#!python print()`. 
Instead, usually a function executes a task and returns the result. The result,
the return value can be of any type. To return a value, use the `#!python return`
statement.

```py hl_lines="3"
def square_number(number):
    square = number ** 2
    return square
```

When you call the function, you can assign the result to a variable.

```py
result = square_number(5)
```

???+ question "Password check"
    
    Write a function to check if a user is able to log-in.

    You have to determine if the given username and password (in 
    plain text) are within the database. The database is a `#!python dict` 
    with IDs as keys and another `#!python dict` as value, containing 
    username and hashed password.

    Given 'database':
    
    ```py
    very_secure_db = {
        0: {
            "username": "SwiftShark22",
            "password": "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f",
        },
        1: {
            "username": "FierceFalcon66",
            "password": "07ac6e7d83aa285293fc325fecd04a51e933ab94d43dbc6434ddca652718fb95",
        },
        2: {
            "username": "admin",
            "password": "6feb4c700de1982f91ee7a1b40ca4ded05d155af3987597cb179f430dd60da0b",
        },
        3: {
            "username": "BraveWolf11",
            "password": "c430e4368aff7c1bc75c3865343730500d7c1a5f65758ade56026b08e94686cc",
        },
    }
    ```

    <figure markdown="span">
      ![Meme](https://static.wixstatic.com/media/8d7a62_092e17448f91434cbfcf628bbe11e8dc~mv2.jpg/v1/fill/w_350,h_350,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/8d7a62_092e17448f91434cbfcf628bbe11e8dc~mv2.jpg){ width="350" }
    </figure>

    Use following function to convert a password to its hash:
    
    ```py
    import hashlib

    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()
    ```
    
    Now, write a function that takes at least two arguments, `username` and 
    `password` (in plain text!). Check if the given username and hashed 
    password are within the `very_secure_db`. Return `#!python True` if the 
    user is able to log-in, otherwise `#!python False`.

    Call your function for following users:

    ```
    user1 = ("SwiftShark22", "password123")
    user2 = ("FierceFalcon", "sdkjf34§")
    user3 = ("admin", "1b40ca4ded0")
    ```

???+ info
    
    As you have seen in the above example, functions help you to structure your
    code. For instance, the function `hash_password()` was reused multiple 
    times (to generate the `very_secure_db` and within your own function).

    Functions also help you to break down complex problems. You can write a 
    function for each subtask and then combine them to solve the problem as a 
    whole.

## Detour: Scope of a variable

The scope refers to the region of a program where variables are defined and can be accessed. Local variables, such as those declared inside a function, are only available within that function. In contrast, variables defined in the main body of the program are called global variables and can be accessed in any part of the program. 

The following example demonstrates that a local variable  created inside a function can be used within that function. 

```py
def greet_user():
	inside_user_name = "Max Mustermann"
	print(f"Hello, {inside_user_name}!")

greet_user()
```

```title=">>> Output"
Hello Max Mustermann!
```

The local variable `inside_user_name` exists only within the function otherwise an error occurs.

```py
def greet_user():
	inside_user_name = "Max Mustermann"

greet_user()
print(f"Hello, {inside_user_name}!")
```

```title=">>> Output"
NameError: name 'inside_user_name' is not defined
```

Therefore, attempting to print the local variable in the main body results in a `NameError`.
Global variables definied in the main body of the program can also be used within functions.

```py
def greet_user():
	print(f"Hello, {outside_user_name}!")

outside_user_name = "Maximilian Muster"
greet_user()
```

```title=">>> Output"
Hello Maximilian Muster!
```

Modifying a global variable inside a function does not overwrite the variable's value.

```py
def greet_user():
	outside_user_name = "change name"

outside_user_name = "Maximilian Muster"
greet_user()
print(f"Hello, {outside_user_name}!")
```

```title=">>> Output"
Hello Maximilian Muster!
```

Within the function, a new local variable with the same name is defined, but it has no effect on the value of the global variable.

???+ tip

    The best way to avoid mistakes is to pass data into and out of functions 
    using arguments and return values.

    ```py
    def greet_user(user_name):  # accept an argument
        greeting = f"Hello, {user_name}!"

        return greeting  # explicit return

    # pass data in, without a global variable
    result = greet_user("Maximilian Muster")
    print(result)
    ```


## Recap

This section introduced the concept of functions to better structure your 
code, make it more readable and reusable. We have covered:

- How to define a function
- Docstrings as a tool to document your functions
- Parameters vs arguments
- Positional and keyword arguments
- Defining default values for parameters
- The `#!python return` statement
- How to use functions to solve smaller subtasks and structure your code
- Detour on global versus local variables
