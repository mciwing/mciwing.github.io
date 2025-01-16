# Object-Oriented Programming

## Introduction
As code complexity grows, managing and understanding functionality becomes increasingly challenging. **Object-Oriented Programming (OOP)** addresses this by breaking down large tasks into smaller, modular components.

### Example: Self-Driving Car
Imagine developing software for a self-driving car. Instead of coding everything in a single block, you can organize the project into modules like **camera systems, lane detection, navigation, and battery management**. Each module is easier to develop, test, and maintain. Moreover, these modules can be reused in other applications, such as drone control, if similar functionalities are required.

### How OOP Helps
OOP enhances modularity by allowing each module (or class) to operate independently. Different team members can work on separate classes, improving scalability and collaboration. Think of it like running a restaurant: instead of handling every task yourself, roles like chef, waiter, and cleaner are delegated to specialized staff, making operations efficient and scalable.

<div style="text-align: center;">
    <iframe src="https://giphy.com/embed/yoJC2J9ftjg7eKtMSQ" width="390" height="293" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/spongebob-customer-service-waiter-yoJC2J9ftjg7eKtMSQ"></a></p>
</div>

### Core Concepts of OOP
Object-Oriented Programming (OOP) is based on the concept of **objects**, which are instances of **classes** (modules).

**Classes and Objects**:  

- **Class**: A blueprint defining attributes (properties) and methods (actions) for objects.
- **Object**: An instance of a class, created using the class blueprint.

Objects combine **attributes** (what they "have") and **methods** (what they "do"). 

**Attributes and Methods**:  

- **Attributes**: Properties specific to the object (e.g., resolution, lens type).
- **Methods**: Functions defining object behavior (e.g., capturing images, detecting objects).

For instance, a `Camera` class in a self-driving car may define attributes like resolution and lens type, along with methods for capturing images or detecting objects. Multiple objects (e.g., front and rear cameras) can be created from this class, each with unique attribute values.

OOP makes it easy to reuse and extend code, simplifying the development of complex systems like self-driving cars.

<div style="text-align: center;">
    <iframe src="https://giphy.com/embed/KXYojKgWCzoQ0" width="350" height="293" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/gifnews-car-csaba-klement-KXYojKgWCzoQ0"></a></p>
</div>

## Class Definition
Classes define the structure of objects, specifying their attributes and methods. Use the syntax:  
`class ClassName:`    
Just like with functions, the code inside the class is indented. Classes can be defined in the same script or in a separate script file, which can then be included using `import`.   
Changes to the class definition only apply to new objects, meaning that all objects from the old definition must be removed from the workspace. The workspace can be cleared using    
`%reset -f`.

A class for a `Camera` module in a self-driving car could be defined as follows:
```python
%reset -f

class Camera:
    pass
```
???+ info "Info"
    `pass` is a placeholder that indicates that no action is executed. It is used to define an empty code block.

You can create **Camera** objects — instances of the class — by assigning them using  `Camera()`.
```python
%reset -f

class Camera:
    pass

# Creating instances of the Camera class
front_camera = Camera()
rear_camera = Camera()

print(type(front_camera)) 
print(type(rear_camera))  
```
```title=">>> Output"
<class '__main__.Camera'>
<class '__main__.Camera'>
```
This demonstrates that `front_camera` and `rear_camera` are instances of the `Camera` class, even though the class currently has no defined attributes or methods.    

Variables or attributes can be defined within a class. As a result, all objects of the class will have this variable with the specified value. The attribute can be accessed using a **dot operator**.
```python
%reset -f

class Camera:
    # Defining a class attribute
    lens_type = "wide-angle" 

# Creating an instance of the Camera class
front_camera = Camera()

# Accessing the attribute using the dot operator
print(front_camera.lens_type)
```
The `lens_type` attribute is a **class attribute**, meaning it is shared by all instances of the class.    
Changing the value of the class attribute (`Camera.lens_type`) affects all objects created from the class, as they share the same attribute.  
```python
%reset -f

class Camera:
    # Defining a class attribute
    lens_type = "wide-angle"  
    
# Creating two instances of the Camera class
front_camera = Camera()
rear_camera = Camera()

# Accessing the shared attribute
print(f"Front camera lens type: {front_camera.lens_type}")  
print(f"Rear camera lens type: {rear_camera.lens_type}")    

# Changing the class attribute
Camera.lens_type = "telephoto"

# Both instances reflect the updated value
print(f"Front camera lens type: {front_camera.lens_type}")
print(f"Rear camera lens type: {rear_camera.lens_type}") 
```

## Initialization Method
The `__init__(self, property)` method is called each time a new object is instantiated.   

**Attributes** are characteristics that describe an object (e.g., camera_type, lens_type). Within the `__init__` method, the term **`self`** refers to the object being created, and additional attributes can be added to it. This **initialization method** ensures that the Camera object is set up with specific values (e.g., camera_type and lens_type) right when it is created. An error message occurs if these specific values are missing.
```python
%reset -f

class Camera:
    # Setting the attributes camera_type and lens_tpye
    def __init__(self,camera_type, lens_type):
        self.camera_type = camera_type
        self.lens_type = lens_type

# Creating an instance of the Camera class       
front_camera = Camera("front","wide-angle")
print(f"{front_camera.camera_type} and {front_camera.lens_type}")

# Creating another instance of the Camera class
rear_camera = Camera()
```
???+ question "Initialization Method"

    Why does this code generate an error message? Identify the cause and modify the code to ensure it runs without errors.
 
**Initialization parameters** allow optional customization when creating an object. If no values are provided, default values will be used.
```python
%reset -f

class Camera:
    # Setting the attributes camera_type, lens_tpye and resolution
    def __init__(self,camera_type, lens_type, resolution=1080):
        self.camera_type = camera_type
        self.lens_type = lens_type
        self.resolution = resolution
        
# Creating an instance of the Camera class w/o defining the resolution      
front_camera = Camera("front","wide-angle")
print(f"{front_camera.camera_type}, {front_camera.lens_type} and {front_camera.resolution}")
```
```python
# Creating an instance of the Camera class        
front_camera = Camera("front","wide-angle",720)
print(f"{front_camera.camera_type}, {front_camera.lens_type} and {front_camera.resolution}")
```

## Encapsulation
**Encapsulation** separates what a class shows (**public** properties and methods) from its hidden internal details (**private** implementation). If data is **public**, it can be directly accessed and changed using the **dot operator**.   
```python
%reset -f

class Camera:
    # Setting the attributes camera_type and lens_tpye
    def __init__(self,camera_type, lens_type):
        self.camera_type = camera_type
        self.lens_type = lens_type

# Creating an instance of the Camera class          
front_camera = Camera("front","wide-angle")
print(front_camera.camera_type)
```
```python
# Changing the attribute camera_type
front_camera.camera_type = "rear"
print(front_camera.camera_type)
```
If data is **private**, it allows access only through specific **methods**, protecting the object's internal workings. Using double underscores before the attribute name (`__name`), restricts access to the **private** attribute.   
```python
%reset -f

class Camera:
    # Setting the private attributes camera_type and lens_tpye
    def __init__(self,camera_type, lens_type):
        self.__camera_type = camera_type
        self.__lens_type = lens_type
        
# Creating an instance of the Camera class 
front_camera = Camera("front","wide-angle")

# Incorrect usage: Accessing the attribute camera_type
print(front_camera.camera_type)
```
By defining appropriate **methods**, interface functions can be provided to allow the user to modify and read **private** attributes (e.g., change_camera_type, display_data). The **dot operator** is used when calling the function.
```python
%reset -f

class Camera:
    # Setting the private attributes camera_type and lens_tpye
    def __init__(self,camera_type, lens_type):
        self.__camera_type = camera_type
        self.__lens_type = lens_type

    # Creating the method change_camera_type
    def change_camera_type(self, camera_type_new):
        self.__camera_type = camera_type_new

    # Creating the method display
    def disp(self):
        print(f"Object of Camera Class:\n")
        print(f"Camera Type: {self.__camera_type}")
        print(f"Lens Type: {self.__lens_type}")
```
???+ question "Encapsulation"

    Create a new instance of the `Camera` class (e.g., `front_camera`), then update its `camera_type` attribute.

## Definition of the Data Structure
The structure of data — such as data types and dimensions — can still be freely chosen by the user, which may lead to undesired behavior. For example, the attribute *camera_type* might be assigned a list (**list**) instead of a string (**str**), or *resolution* might be given a string (**str**) instead of an integer (**int**) without any warning about the incorrect input.  

To prevent this, data structures can be validated within the class definition. If the input is incorrect, an error message can be raised using:  
`#!python raise ValueError("Error message")`  

<div style="text-align: center;">
    <iframe src="https://giphy.com/embed/3o7WTDH9gYo71TurPq" width="390" height="220" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/glitch-art-professorlightwav-3o7WTDH9gYo71TurPq"></a></p>
</div>

You can check the data type with the command:  
`isinstance(variable, data_type)`    

Possible attributes of a category can also be defined in a list, for example:  
*`__camera_types = ["front", "rear", "left", "right", "top", "not stated"]`*    
*`orientation = ["horizontal", "vertical"]`*    

By validating the data types during object creation, you can ensure the object behaves as expected and avoid unexpected errors later in the program.
```python
%reset -f

class Camera:
    __camera_types = ["front","rear","left","right","top","not stated"]

    # Setting the attributes camera_type, lens_type, resolution and orientation with restrictions
    def __init__(self, camera_type, lens_type, resolution, orientation="not stated"):
        if camera_type not in self.__camera_types:
            raise ValueError(f"Camera type must be one of {self.__camera_types}.")  # Check if camera_type is one attribute from list.
        if not isinstance(lens_type, str):                      
            raise TypeError("Lens type must be a string.")  # Check if lens_type is a string.
        if not isinstance(resolution, int):                                                         
            raise TypeError("Resolution must be an integer.")  # Check if resolution is an integer.
        if orientation not in ["horizontal","vertical"]:
            raise ValueError("Orientation must be either 'horizontal' or 'vertical'.")  # Check if orientation is one attribute from list.
        self.__camera_type = camera_type
        self.__lens_type = lens_type
        self.resolution = resolution
        self.orientation = orientation

    # Creating the method change_camera_type with data type restrictions
    def change_camera_type(self, camera_type_new):
        if camera_type_new not in self.__camera_types:
            raise ValueError(f"Camera type must be one of {self.__camera_types}.")
        self.__camera_type = camera_type_new

    # Creating the method set_orientation with data type restrictions
    def set_orientation(self, orientation):
        if orientation not in ["horizontal", "vertical"]:
            raise ValueError("Orientation must be either 'horizontal' or 'vertical'.")
        self.orientation = orientation

    # Creating the method display
    def disp(self):
        print(f"Object of Camera Class\n:")
        print(f"Camera Type: {self.__camera_type}")
        print(f"Lens Type: {self.__lens_type}")
        print(f"Resolution: {self.resolution}p")
        print(f"Orientation: {self.orientation}")
```
???+ question "Data Structure"

    Create two instances of the `Camera` class. Ensure one is created correctly, and intentionally cause an error with the other.