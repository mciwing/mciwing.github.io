# Graphical User Interfaces with Tkinter

## Introduction
A **Graphical User Interface (GUI)** allows users to interact with a program through visual elements like buttons, text fields, and menus, rather than typing commands in a terminal. GUIs thus make applications more accessible to non-technical users.

<div style="text-align: center;">
    <iframe src="https://giphy.com/embed/l2JdSlA1a1zKVAyze" width="410" height="310" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/season-15-the-simpsons-15x9-l2JdSlA1a1zKVAyze"></a></p>
</div>

#### How GUIs relate to OOP?
Each GUI element (widget), like a button or text field, can be thought as an object of the corresponding class. These objects:    

- have **attributes** (e.g., size, color, labels),
- have **methods** (e.g., click, enable/disable), and
- interact with each other through events,

following the principles of object-oriented programming (OOP).

**Tkinter** is the standard `Python` :fontawesome-brands-python: library for creating graphical user interfaces. It provides a practical introduction to GUI development and event-driven programming. By using **Tkinter**, interactive applications such as calculators, form-based tools, or simple games, can be build. The **Tkinter** documentation can be found here: [:octicons-link-external-16:](https://docs.python.org/3/library/tkinter.html)   
Nevertheless, there are many other GUI libraries that you could be interested in. The `Python` :fontawesome-brands-python: wiki lists several alternative [GUI frameworks and tools](https://wiki.python.org/moin/GuiProgramming).


## Creating a Basic Tkinter Application
### The Tkinter Main Loop
The **root window** is responsible for running the main event loop (`mainloop()`), which keeps the GUI application running, listens for events (e.g., clicks, keystrokes), and updates the interface. The main event loop ends when the window is closed. Without the main loop, the GUI application would close immediately after being displayed.
```python
import tkinter as tk

# Create root window
root = tk.Tk()
root.title("My First GUI Program")
root.minsize(width=300, height=400)

# Running the main loop event
root.mainloop()
```
### Widgets and Controls
Widgets and controls are the building blocks of a **Tkinter** GUI. Widgets are structured in a hierarchy, where some widgets serve as containers (**parent widgets** - e.g., windows or frames) that hold other widgets (**child widgets**). This hierarchical arrangement defines the relationships and organization of widgets, influencing their layout, behavior, and interaction.    
They are placed using a **layout manager** (place, pack, or grid).    
Widgets feature attributes like `text`, `font`, `bg` (background color), `fg` (foreground color), and `width`, which can be set during creation or updated later. 

**Collection of Different Widgets**:   
The following code provides a collection of different widgets: `Label`, `Input`, `Button`, `Text`, `Spinbox`, `Scale`, `Checkbutton`, `Radiobutton`, and `Listbox`.   
Each widget is an object of its class (e.g., button, label) and is part of the same **parent widget** (`root` window).

**Widget Callbacks**:   
Some widgets support event handling. Each widget's behavior is managed by a specific method:    

 - **Button**: `button_clicked()`
 - **Spinbox**: `spinbox_used()`
 - **Scale**: `scale_used(value)`
 - **Checkbutton**: `checkbutton_used()`
 - **Radiobutton**: `radio_used()`
 - **Listbox**: `listbox_used(event)`

**Dynamic Behavior**:    
Widgets like the spinbox, scale, and listbox dynamically print or process user interactions.

**Event Binding**:    
The `listbox` widget uses the `bind` method to associate the selection event with the `listbox_used` method.

???+ question "Run the Code"
    Interact with the widgets to see their behavior in action (check the console for printed outputs).

```python
import tkinter as tk

# Set window attributes
root = tk.Tk()
root.title("My First GUI Program and Widgets")
root.geometry("1024x768")
        
# Label
my_label = tk.Label(text="My First Label", font=("Arial", 24, "bold"))
my_label.pack()

# Input
my_input = tk.Entry(width=10)
my_input.pack()

# Button callback
def button_clicked():
    print("Do Something Cool")
# Button
my_button = tk.Button(text="Click Me", command=button_clicked)
my_button.pack()

# Text
text = tk.Text(height=5, width=30)
text.focus()
text.insert(tk.END, "My first try on a multi-line text entry.")
print(text.get("1.0", tk.END))  # Prints the current text
text.pack()

# Spinbox callback
def spinbox_used():
    print(spinbox.get())
# Spinbox
spinbox = tk.Spinbox(from_=0, to=3, width=5, command=spinbox_used)
spinbox.pack()

# Scale callback
def scale_used(value):
    print(value)
# Scale
scale = tk.Scale(from_=0, to=1000, command=scale_used)
scale.pack()

# Checkbutton callback
def checkbutton_used():
    print(checked_state.get())
# Checkbutton
checked_state = tk.IntVar()  # Variable to hold the checked state
checkbutton = tk.Checkbutton(text="Is This On?", variable=checked_state, command=checkbutton_used)
checkbutton.pack()

# Radiobutton callback
def radio_used():
    print(radio_state.get())
# Radiobutton
radio_state = tk.IntVar()  # Variable to hold the radio button selection
radiobutton1 = tk.Radiobutton(text="Answer1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tk.Radiobutton(text="Answer2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

# Listbox callback
def listbox_used(event):
    print(listbox.get(listbox.curselection()))
# Listbox
listbox = tk.Listbox(height=4)
colors = ["Red", "Green", "Blue", "Yellow"]
for item in colors:
    listbox.insert(colors.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

root.mainloop()
``` 

### Tkinter Layout Manager
The layout of a graphical user interface is largely determined by the arrangement and design of the GUI components. Tkinter provides three different layout managers that automatically generate the layout based on the settings defined in the program. Without using a layout manager, the GUI element will not appear on the screen.

1. **Place Manager**: Positions components based on specific coordinates (x, y), offering precise control over placement.
2. **Pack Manager**: Automatically arranges components in a container, either vertically or horizontally, based on the order they are added.
3. **Grid Manager**: Organizes components in a grid with rows and columns, allowing more complex layouts with alignment options.


**Key Concepts of the Grid Layout Manager**:   

1. **Rows and Columns:**
    - The grid is organized into rows and columns. You can place widgets in a specific row and column using the `grid(row, column)` method.
    - You can also span multiple rows or columns using `rowspan` and `columnspan` attributes.
   
2. **Control Placement:**
    - You can specify the **row**, **column**, and **sticky** options to control widget alignment (e.g., top, bottom, left, right).

3. **Column and Row Configuration:**
    - **Tkinter** allows you to configure the weight of rows and columns to define how they should expand when the window is resized. You can do this using `grid_columnconfigure()` and `grid_rowconfigure()`.

```python
import tkinter as tk

root = tk.Tk()
root.title("Grid Layout Example")

# Label in the first row and first column
name_label = tk.Label(text="Name:")
name_label.grid(row=0, column=0)

# Entry in the first row and second column
name_entry = tk.Entry()
name_entry.grid(row=0, column=1)

# Label in the second row and first column
age_label = tk.Label(text="Age:")
age_label.grid(row=1, column=0)

# Entry in the second row and second column
age_entry = tk.Entry()
age_entry.grid(row=1, column=1)

# Button in the third row and first column
submit_button = tk.Button(text="Submit")
submit_button.grid(row=2, columnspan=2)  # Spanning both columns

root.mainloop()
```

???+ info "Tkinter Hints and Suggestions"
    1. **Modularize Code**
        - Break the GUI into smaller classes or methods, particularly for large application.
        - Use reusable components: e.g., set an `InputForm` class for repeated input forms.
   
    2. **Use Meaningful Variable and Method Names**
        - Name widgets and methods clearly to reflect their purpose. Avoid generic names like `button1` or `label1`, use for example `submit_button` instead.

    3. **Avoid Hardcoding Layouts**
        - Use layout managers (`pack` or `grid`) instead of coding absolute positions (`place(x, y)`).
        - Avoid mixing layout manager in the same container.

    4. **Error Handling**
        - Add errror handling for user input or unexpected behavior.
        - Provide clear instructions and feedback.

## Example: Create Your Own To-Do List Application

The following code provides the basis for a simple To-Do List application with the following key features:

- **Add Task**: Enter tasks using the `Entry` widget and add them to the `Listbox`.
- **Cross Out Task**: Mark the selected task with a "✔" symbol to indicate completion.

???+ question "To-Do List Enhancements"
    Customize and enhance the To-Do List app with the following features:    
        1. Change the color scheme of the app.     
        2. Add a `Button` to entirely delete tasks from the `Listbox`.     
        3. Position the `delete_button` next to the `cross_out_button` and use a red color.      

    **Bonus**: Highlight important tasks by adding features like colored text or checkboxes to mark tasks as important.

```python
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("To-Do List")
root.minsize(height=400, width=400)
root.configure(bg="#d0ebff")  # Light blue background

# Function to add a new task
def add_task():
    task = task_entry.get()
    if task.strip():
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

# Function to cross out a selected task
def cross_task():
    selected = task_listbox.curselection()
    if selected:
        current_task = task_listbox.get(selected)
        task_listbox.delete(selected)
        task_listbox.insert(selected, f"✔ {current_task}")

# Entry box for adding tasks
task_entry = tk.Entry(width=30, font=("Helvetica", 14))
task_entry.grid(row=0, column=1, padx=10, pady=10)

# Add Task button
add_button = tk.Button(text="Add Task", font=("Helvetica", 12), bg="#b0e0e6", fg="black", command=add_task)
add_button.grid(row=0, column=0, padx=10, pady=10)

# Listbox to display tasks
task_listbox = tk.Listbox(width=40, height=15, font=("Helvetica", 12), selectbackground="#b3e5fc", selectforeground="black")
task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Cross Out Task button (centered)
cross_out_button = tk.Button(text="Cross Out Task", font=("Helvetica", 12), bg="#00264d", fg="white", command=cross_task)
cross_out_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Start the main loop
root.mainloop()
```

<div style="text-align: center;">
    <iframe src="https://giphy.com/embed/ITXgZuGi17YwCQIofC" width="380" height="300" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/gracetea-ITXgZuGi17YwCQIofC"></a></p>
</div>