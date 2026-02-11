# Object-Oriented Programming

As code complexity grows, managing and understanding functionality becomes increasingly challenging. **Object-Oriented Programming (OOP)** addresses this by breaking down large tasks into smaller, modular components. Each module does one job.

## How OOP Helps
Imagine developing a simple game. For instance, your game includes different characters: heroes, enemies, and healers. Instead of coding everything in a single block, you can organize the project into different modules (classes): **Hero class, Enemy class, and Healer class**. Each one has its own job. That makes your game easier to develop, test, and maintain. Moreover, the individual modules can be reused in other applications if similar functionalities are required. Different team members can work on separate classes, improving scalability and collaboration.  

Think of it like running a restaurant: instead of handling every task yourself, roles like chef, waiter, and cleaner are delegated to specialized staff, making operations efficient and scalable.

<div style="text-align: center;">
    <iframe src="https://giphy.com/embed/yoJC2J9ftjg7eKtMSQ" width="390" height="293" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/spongebob-customer-service-waiter-yoJC2J9ftjg7eKtMSQ"></a></p>
</div>

## Core Concepts of OOP
Object-Oriented Programming is based on the concept of **objects**, which are instances of **classes**.

**Classes and Objects**:  

- **Class**: A class is just a recipe.
- **Object**: An object is something you made from the recipe.

For example, a cookie recipe would represent a class in Python, whereas the cookie itself is the object made from that recipe. Let's make our first class and create our first object:

```python
class GameCharacter:
    pass

hero = GameCharacter()
```
???+ info "Explanation"
    `GameCharacter` → the recipe (class)  
    `hero` → the actual character (object)  
    `pass` is a placeholder that indicates that no action is executed. It is used to define an empty code block.  

Just like with functions, the code inside the class is indented. Classes can be defined in the same script or in a separate script file, which can then be included using `import`.   

Objects combine **attributes** (what they "have") and **methods** (what they "do"). 

**Attributes and Methods**:  

- **Attributes**: Information stored inside an object (e.g., name, health, level).

Let's add an attribute:
```python
class GameCharacter:
    def __init__(self, name, health):
        self.name = name
        self.health = health

hero = GameCharacter("Mario", 100)

print(hero.name)
print(hero.health)
```
???+ info "Explanation"
    `__init__` runs when we create an object  
    `self` means: “this character”  
    `self.name` → stores the name   
    `self.health` → stores the health

- **Methods**: Functions defining an object's behavior (e.g., attack, heal, talk).

Let's add a method:
```python
class GameCharacter:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def say_hello(self):
        print("Hi, I am", self.name)

hero = GameCharacter("Mario", 100)
hero.say_hello()
```
???+ info "Explanation"
    `say_hello` is a method  
    `hero.say_hello()` calls the method  

???+ tip "Basic OOP Syntax in Python"
    When working with classes and objects in Python, some simple rules and conventions help you write clean and readable code. These rules are widely used in real Python projects.   
    1. **Class Names (PascalCase)**: start with a capital letter. Each new word is also capitalized.  
        Every class starts with the keyword `class` and ends with a colon `:`.
    ```python
    class GameCharacter:
        #class code goes here
    ```
    ❌ Avoid:
    ```python
    class gamecharacter:
    class game_character:
    ```
    2. **Object Names (snake_case)**: use lowercase letters. Words are separated with underscores.  
        Objects are created by calling the class with parentheses `()`.
    ```python
    main_hero = GameCharacter()
    princess = GameCharacter()
    ```
    3. **Methods and `self`**: All methods inside a class must use `self` as the first parameter. `self` refers to the current object.  
    ```python
    class GameCharacter:
        def greet(self):
            print("Hello!")
    ```
    When calling the method, do not write `self`.  
    The dot (`.`) is used to access attributes and methods (data). 
    ```python
    princess = GameCharacter()
    princess.greet()
    ```
     4. **Attributes and `self`**: Attributes store data inside an object. Without `self.` the value is not saved in the object.
    ```python
    class GameCharacter:
        def __init__(self,name):
            self.name = name
    ```

## Initialization Method
The `__init__(self, property)` method is called automatically every time a new object is created from a class.     
Inside the `__init__` method, the word **`self`** refers to the object that is being created. It is used to store information about the object.  
The job of the **initialization method** is to make sure that the object is ready to use. For example, a character can be given a name and a health amount.  

If required values are missing when the object is created, Python will show an error, just like it does with functions.  
Except if a default value is used, no error will be raised. In this example, health has a default value of 100, so if no health value is provided, it will automatically be set to 100.  

```python hl_lines="3"
class GameCharacter:
    # Setting the attributes name and health
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

# Creating objects of the GameCharacter class       
hero = GameCharacter("Mario")
print(hero.name, hero.health)
enemy = GameCharacter("Bowser", 150)
print(enemy.name, enemy.health)
anti_hero = GameCharacter()
print(anti_hero.name, anti_hero.health)
```
???+ question "Initialization Method"

    Why does this code generate an error message? Identify the cause and modify the code to ensure it runs without errors.

## The `__str__` Method
Notice that when you print an object created from a class, the output often provides unhelpful information:
```python
class GameCharacter:
    # Setting the attributes name and health
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

# Creating objects of the GameCharacter class       
hero = GameCharacter("Mario")
print(hero)
```
```title=">>> Output"
<__main__.GameCharacter object at 0x000002075A42B0E0>
```
The `__str__` method is a built-in Python function that defines how an object appears when it is converted to a string, such as when it is printed.   
Although `__str__` is not required for OOP, it makes your objects more readable, user-friendly, and easier to work with.
```python hl_lines="8"
class GameCharacter:
    # Setting the attributes name and health
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    # Creating the string method
    def __str__(self):
        return f"{self.name}, {self.health} HP."

# Creating objects of the GameCharacter class       
hero = GameCharacter("Mario")
print(hero)
```
```title=">>> Output"
Mario, 100 HP.
```

## Attributes
As shown in the example above, the `GameCharacter` class has attributes such as name and health, as well as methods for actions like talking. From this class, we can create multiple objects (characters).    

In the case of attributes, we can differ between two main types:      
- **Instance Attributes**: belong to each individual object.   
- **Class Attributes**: are shared by all objects of the class.   

### Instance Attributes
Instance attributes store information that is different for each character, such as their name, health, or level.
```python
class GameCharacter:
    def __init__(self, name, health):
        # Defining an instance attribute
        self.name = name
        self.health = health
```
Here, `name` and `health` are **instance attributes**. Each character can have different values.
```python
# Creating objects of the GameCharacter class
hero = GameCharacter("Mario", 100)
enemy = GameCharacter("Bowser", 150)

# Accessing the instance attribute using the dot operator
print(hero.name)   # Mario
print(enemy.name)  # Bowser
```
### Class Attributes
Sometimes, all characters need to share the same information. For example, they may all start in the same world.
```python
class GameCharacter:
    # Defining a class attribute
    world = "Mushroom Kingdom" 
    def __init__(self, name, health):
    # Defining an instance attribute
        self.name = name
        self.health = health

# Creating objects of the GameCharacter class
hero = GameCharacter("Mario", 100)
enemy = GameCharacter("Bowser", 150)

# Accessing the class attribute using the dot operator
print(hero.world)
print(enemy.world)
```
Here, `world` is a class attribute. It belongs to the class itself, not to individual objects. All objects created from `GameCharacter` share this same value.   
If we change the value of a **class attribute**, the change affects all objects that use it.

```python
# Changing the class attribute
GameCharacter.world = "Dinosaur Land"
    
# Both objects reflect the updated value
print(hero.world)  
print(enemy.world)    
```
**Quick Comparison**

| Feature                    | Instance Attribute | Class Attribute       |
| -------------------------- | ------------------ | --------------------- |
| Belongs to                 | one object         | the whole class       |
| Different for each object? | Yes                | No                    |
| Defined using              | `self.attribute`   | `ClassName.attribute` |
| Example                    | `self.name`        | `world`               |


???+ question "Attributes"

    Change the `hero` object's `name` attribute to Luigi instead of Mario using the **dot operator**.

## Encapsulation
Sometimes you don't want others to change data freely. **Encapsulation** is the idea of controlling how data in a class can be seen and changed. It separates what can be accessed directly (**public** properties and methods) from what is hidden inside the class (**private** data and methods).   

For example, we want to prevent users from changing a character’s health directly. Instead, health should only be updated in controlled ways. We can mark the health attribute as private by using double underscores before its name (`__health`).   

```python
class GameCharacter:
    # Setting the attributes name and health
    def __init__(self, name, health=100):
        self.name = name
        self.__health = health  #private

# Creating an object of the GameCharacter class          
hero = GameCharacter("Mario")
print(hero.name)
print(hero.health)
``` 
```title=">>> Output"
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[11], line 10
      8 hero = GameCharacter("Mario")
      9 print(hero.name)
---> 10 print(hero.health)

AttributeError: 'GameCharacter' object has no attribute 'health'
```
When an attribute is private, it cannot be accessed directly from outside the class. If you try, Python will raise an `AttributeError`.   
Instead, private data should be accessed and changed only through special methods (such as `show_health()` or `take_damage()`). To call these methods, we use again the **dot operator**.

```python
class GameCharacter:
    # Setting the attributes name and health
    def __init__(self, name, health=100):
        self.name = name
        self.__health = health  #private

    # Creating the method show_health
    def show_health(self):
        return self.__health

    # Creating the method take_damage
    def take_damage(self, amount):
        self.__health -= amount

# Creating an object of the GameCharacter class          
hero = GameCharacter("Mario")
print(hero.show_health())
hero.take_damage(30)
print(hero.show_health())
```
???+ question "Encapsulation"

    Create a new character of the `GameCharacter` class (e.g., enemy), then update and print its `health` attribute.

## Exceptions
The structure of data, such as its type and allowed values, can still be chosen freely at this point by the user. This can lead to unwanted behavior.   
For example, the attribute *name* might be given a list (**list**) or a number (**int**) instead of a text value (**str**). Similarly, *health* might be set to a negative value without any warning.   

These kinds of incorrect inputs can cause problems in a program. Luckily, there are ways to prevent this and make sure that only valid data is used:

```python
class GameCharacter:
    # Setting the attributes name and health
    def __init__(self, name, health):
        self.name = name
        self.__health = health

# Creating an object of the GameCharacter class          
hero = GameCharacter("Mario",-10)
```
```python hl_lines="4 5"
class GameCharacter:
    # Setting the attributes name and health
    def __init__(self, name, health):
        if health < 0:
            raise ValueError("Health cannot be a negative value")

        self.name = name
        self.__health = health

# Creating an object of the GameCharacter class          
hero = GameCharacter("Mario",-10)
```
???+ info "Causing Errors for Others"

    The statement `#!python raise ValueError("Error message")` is used to create a general error when a value is not acceptable. For example, it can be used to show that the health value cannot be negative.   
    If you want to check whether an attribute has the wrong data type (for example, giving a string when a number is expected), you can raise a `TypeError` with a clear message: `#!python raise TypeError("Error message")`   
    There are many other types of errors (or often called exceptions), that you can raise in Python. Using the right exception helps explain what went wrong and makes your program easier to understand and use.  
    [Here](https://docs.python.org/3.12/library/exceptions.html#exception-hierarchy) is a comprehensive list of all built-in exceptions in Python.  

    In addition, note that in the example above, the attribute `__health` is a **private attribute**. Making an attribute private is common practice when you want to control and validate changes, for example, to raise an error if an invalid value is given. **Public attributes**, by contrast, can be accessed and changed freely from outside the class, which is fine only when there is no risk of invalid values.

<div style="text-align: center;">
    <iframe src="https://giphy.com/embed/3o7WTDH9gYo71TurPq" width="390" height="220" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/glitch-art-professorlightwav-3o7WTDH9gYo71TurPq"></a></p>
</div>

One can check the data type of a value using the following command:    
`#!python isinstance(variable, data_type)`  

```python
class GameCharacter:
    # Setting the attributes name and health
    def __init__(self, name, health):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        
        if not isinstance(health, int):
            raise TypeError("Health must be a number")
        
        if health < 0:
            raise ValueError("Health cannot be a negative value")

        self.__name = name
        self.__health = health

# Creating an object of the GameCharacter class          
hero = GameCharacter("Mario","-100")
```
???+ question "Control Data Type and Value"

    Why does this code generate an error message? Identify the cause and modify the code to ensure it runs without errors.

You can also limit the possible values of an attribute by using a list, for example:   
`allowed_skills = ["heal", "attack", "defend", "run", "jump", "not stated"]`    
`allowed_movements = ["forward", "backward", "up", "down", "not stated"]` 

```python
class GameCharacter:
    #Setting the class attribute allowed_movements
    allowed_movements = ["forward", "backward", "up", "down", "not stated"]
    
    # Setting the instance attributes name and movement
    def __init__(self, name, movement="not stated"):
        if movement not in GameCharacter.allowed_movements:
            raise ValueError(
                f"Movement must be one of: {GameCharacter.allowed_movements}")
        self.__movement = movement
        self.__name = name
        
    # Creating the method show_movement
    def show_movement(self):
        return self.__movement
    
    # Creating the method set_movement
    def set_movement(self, new_movement):
        if new_movement not in GameCharacter.allowed_movements:
            raise ValueError(
                f"Movement must be one of: {GameCharacter.allowed_movements}")
        else:
            self.__movement = new_movement

#Creating an object of the GameCharacter class
hero = GameCharacter("Mario", "forward")
print(hero.show_movement())
hero.set_movement("up")
print(hero.show_movement())
hero.set_movement("side")
```
???+ question "Limit Allowed Values"

    Add a new attribute `skills` to the example above and limit its allowed values to:   
    `allowed_skills = ["heal", "attack", "defend", "run", "jump", "not stated"]`.   
    Additionally, create two new methods `show_skills()` and `set_skills()`, then test your code to make sure the attribute works correctly.  

## Inheritance
Inheritance is one of the most important features of object-oriented programming. It allows one class to reuse code from another class. A class can inherit attributes and methods from an existing class and then add new features or change how they work.   

In a game, many characters are similar. All of them have a name, health, and basic abilities. However, some characters also have special skills: warriors can fight or healers can heal.   
With inheritance, we can define these shared features only once and reuse them, instead of writing the same code again and again. This helps keep programs simple, organized, and easier to maintain.   

**Step 1: Create a Parent Class**
```python
class GameCharacter:
    # Setting the attributes name and health
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    # Creating the method show_health
    def show_health(self):
        print(f"{self.name} has {self.health} HP.")
```

All characters created from the **parent class** have the attributes `name` and `health`, as well as the method `show_health`.

**Step 2: Create Child Classes**   
Based on this parent class, we can create different child classes with special abilities.    

```python hl_lines="1 3"
class Hero(GameCharacter):
    def __init__(self, name, health=150):
        super().__init__(name, health)

    # Creating the method take_damage
    def take_damage(self, amount):
        self.health -= amount
```
```python hl_lines="1 3 4"
class Healer(GameCharacter):
    def __init__(self, name, health, healing_power=10):
        super().__init__(name, health)
        self.healing_power = healing_power

    # Creating the method heal
    def heal(self, target):
        target.health += self.healing_power
        print(f"{self.name} heals {target.name} for {self.healing_power} HP.")
```
???+ info "Explanation"
    The line `super().__init__(name, health)` inside each child class means: *run the parent's setup code first*.  
    This ensures that `GameCharacter` sets the attributes `name` and `health` and provides the `show_health` method.    

    After that, the child classes `Hero` and `Healer` add their own attributes (`healing_power`) and methods (`take_damage` and `heal`).  

**Step 3: Creating Different Characters**
```python
enemy = GameCharacter("Bowser", 150)
hero = Hero("Mario", 120)
healer = Healer("Toad", 80, 15)

enemy.show_health()
hero.show_health()
healer.show_health()

hero.take_damage(25)
healer.heal(hero)
hero.show_health()
``` 
In the last step, we create an enemy called Bowser from the `GameCharacter` class, a hero called Mario from the `Hero` class, and a healer called Toad from the `Healer` class.  

### Inheritance: Overriding Methods
A child class can also change how a method from the parent class works. This is called **method overriding**.    
For example, the `Hero` class wants to display a different message in the `show_health` method:   
```python hl_lines="7"
class Hero(GameCharacter):
    def __init__(self, name, health):
        super().__init__(name, health)

    # Overriding the method show_health
    def show_health(self):
        print(f"Hero, {self.name}, has {self.health} HP.")
```
Although we have only just learned about **inheritance**, we have actually been using it all along when working with **exceptions**.    
If you go back to the page about exceptions [(here)](https://docs.python.org/3.12/library/exceptions.html#exception-hierarchy), you can see that they are organized in a hierarchy with parent and child classes. Some exceptions are more general, while others are more specific and inherit from them. This hierarchy shows how inheritance works in practice.   

## Putting It All Together
Let's now put it all together in a mini-game example:   

```python
# Parent class: GameCharacter
class GameCharacter:
    # Class attribute shared by all characters
    world = "Mushroom Kingdom"

    def __init__(self, name, health=100):  # default value
        if health < 0:
            raise ValueError("Health cannot be negative")  # exception
        self.name = name
        self.health = health

    # __str__ method
    def __str__(self):
        return f"{self.name} ({self.health} HP)"

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        print(f"{self.name} takes {amount} damage!")

    def show_health(self):
        print(f"{self.name}: {self.health} HP in {self.world}")

# Child class: Enemy
class Enemy(GameCharacter):
    def __init__(self, name, health=100):
        super().__init__(name, health)

    def attack(self, target, damage=10):
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        target.take_damage(damage)

# Child class: Healer
class Healer(GameCharacter):
    def __init__(self, name, health=80, healing_power=15):
        super().__init__(name, health)
        self.healing_power = healing_power

    def heal(self, target):
        print(f"{self.name} heals {target.name} for {self.healing_power} HP!")
        target.health += self.healing_power

# Create characters
hero = GameCharacter("Mario")
enemy = Enemy("Bowser", 150)
healer = Healer("Toad", 80, 10)

# Start game
print("\n--- Initial Status ---")
print(hero)
print(enemy)
print(healer)

print("\n--- Battle ---")
enemy.attack(hero, 30)
enemy.take_damage(20)
healer.heal(hero)

print("\n--- Final Status ---")
hero.show_health()
enemy.show_health()
healer.show_health()
```  

???+ question "Final Project: Build Your Own Zoo"

    In this project, you will create your own classes and objects to simulate a mini-zoo. You’ll practice everything you’ve learned about classes, objects, attributes, methods, encapsulation, exceptions, and inheritance.    

    **Step 1: Define the Parent Class** `Animal`   
    1. Create a class called `Animal`.   
    2. Add a class attribute `zoo_name` that is shared by all animals.   
    3. Add **two** instance attributes: `name` (the animal's name) and `energy` (the animal's energy level)   
    4. Exception: make sure that `energy` is not a negative value. If it is, raise a `ValueError` with a message like `Energy cannot be negative`.   
    5. Add a `__str__` method so printing the object shows something readable like `Leo (80 energy)`.   
    6. Add a method `show_status()` that prints the animal’s name, energy, and the zoo it belongs to.   
    7. Add a method `eat()` that increases the animal’s energy.   

    **Step 2: Create Child Classes**    
    1. Create at least one child class, for example `Lion` or `Monkey`.   
    2. Add an additional method to the child class, for example `roar()` or `play()` that decreases the animal's energy.   

    **Step 3: Create Objects**    
    1. Create at least two animal objects from your classes, for example `leo = Lion("Leo", 80)`.    
    2. Use the methods you created to simulate a change in the animal's energy, for example `eat()` or `roar()`.    
    3. Print the status of each animal before and after the interactions using `show_status()` or the `__str__` method.   

## Final Remarks
As an introductory course, we have focused on the fundamentals of classes, objects, attributes, and methods. There are other features commonly used in Python OOP that we have not explored in detail here. For example:   
- **Getter and Setter methods** (`@property`): allow controlled access to private attributes.   
- **Class methods** (`@classmethod`): methods that operate on the class itself rather than individual objects.   
- **Static methods** (`@staticmethod`): methods that belong to a class but do not access class or instance data.   
- **Polymorphism**: the ability for different classes to respond to the same method call in their own way.   
- **Advanced Data Validation**: further techniques to protect attributes and ensure only valid data is stored.    

 As you continue learning Python, you will naturally encounter and use these additional concepts. The goal here is to understand the basic principles: how classes organize code, how objects store data and behavior, and how OOP helps make programs modular, maintainable, and easier to scale. 

???+ info "Connecting to Previous Work"
    
    Although it may not have been stated directly earlier in this course, you have been using classes and objects from the very beginning. Many of the data types you use every day in Python are actually objects created from built-in classes:   
    - For example, `float` is a class in Python. It is used to create decimal numbers, such as 3.14 or 0.5, and provides methods for working with them.   
    - Similarly, `str` is also a class. When you use methods like `str.upper()` or `str.replace()`, you are calling methods that belong to the `str` class.    
    - The `list` type is another built-in class. It contains many useful methods, such as `list.sort()`  and `list.remove()`, which help you manage collections of data.   
    
    To see how you have been using classes all along, you can use the `type()` function in your console:   
    ```python
    print(type(3.14))
    print(type("python"))
    print(type({}))
    ```
    This shows that `3.14` belongs to the `float` class, "python" belongs to the `str` class, and `{}` to the `dict` class.

<div style="text-align: center;">
    <iframe src="https://giphy.com/embed/fAnEC88LccN7a" width="305" height="300" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/boss-childhood-fAnEC88LccN7a">via GIPHY</a></p>
</div>

