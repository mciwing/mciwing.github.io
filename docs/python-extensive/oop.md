# Object Oriented programming

As code complexity increases, it becomes challenging to manage and understand its functionality. Object-Oriented Programming (OOP) helps address this challenge by breaking large, complex tasks into smaller, modular components.

For example, consider developing a program for a self-driving car. Instead of handling all functionalities in a single block of code, you can split the project into modules like **camera systems, lane detection, navigation, and battery management**. Each module is simpler to develop, maintain, and test. Moreover, these modules can be reused in other projects, such as controlling a drone, if similar functionalities are needed.

OOP enhances this modular approach by allowing each module (class) to function independently and be developed by different team members. It also supports scalability by enabling developers to focus on managing the system as a whole rather than micromanaging every detail. Think of it like running a restaurant: instead of being the receptionist, waitress, chef, and cleaner all at once, you delegate these roles to specialized staff. Each team member knows how to perform their job without needing constant instruction, making the operation more efficient and scalable.

Object-Oriented Programming (OOP) is based on the concept of **objects**, which are instances of **classes/modules**.  
- **Classes and Objects**:  
    - **Class**: A blueprint for objects. It defines the attributes (properties) and methods (actions) that the objects will have.
    - **Object**: An instance of a class, created based on the blueprint provided by the class.

Objects combine **attributes** (what they "have") and **methods** (what they "do").
- **Attributes and Methods**: 
    - **Attributes** are variables attached to an object, representing its properties.   
    - **Methods** are functions associated with an object, defining its behavior. These methods are not standalone but tied to the specific object.

For example, in a programm for a self-driving car, a **`Camera`** class might define common attributes such as resolution and lens type, as well as methods like capturing images or detecting objects.
Using this blueprint, multiple instances of the class can be created, such as a rear camera and a front camera. While they share the same structure, each object (camera) can have unique values for its attributes (e.g., resolution or lens type).

This approach allows developers to efficiently reuse and extend the code, making complex systems like self-driving cars modular, maintainable, and scalable. 

### Class Definition

In a class definition, the data structure of the objects belonging to that class is defined, primarily by specifying the attributes. A new class is introduced using the syntax:    
`class ClassName:`    
Just like with functions, the code inside the class is indented.    
Classes can be defined in the same script or in a separate script file, which can then be included using **`import`**.   
Changes to the class definition only apply to new objects, meaning that all objects from the old definition must be removed from the workspace. The workspace can be cleared using **`%reset -f`**.

A class for a **camera module** in a self-driving car could be defined as follows:

```python hl_lines="2"
class Camera:
    pass
```