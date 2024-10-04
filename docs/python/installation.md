# Installation

First, we need to install Python. You can download the latest version of Python
from the official website [python.org](https://www.python.org/downloads/).

We recommend to install the latest version of **:fontawesome-brands-python: Python**
(as of September 2024, the latest stable release is `3.12.6`).

Depending on your operating system, the installation process may vary slightly.
Below, we will cover the installation process on a Windows machine. If you are
using **macOS**, python.org offers a corresponding installer (64-bit). 

## :fontawesome-brands-windows: Windows

Execute the downloaded file (installer). When installing Python, make sure that
you check the box `Add python.exe to PATH`.

<div style="text-align: center;">
    <img height="350" src="/assets/python/installation/python-install.gif" width="500" style="border-radius: 10px;"/>
</div>

After the successful installation, we recommend to open a command prompt
(use the Windows search with the keyword `cmd`) and verify the installation by 
typing 

```commandline
python --version.
```

Which should result in:

```title="CMD Output"
Python 3.12.6
```

## Troubleshooting

### PATH issues

If you didn't check the box `Add python.exe to PATH` during 
installation, or you encounter an error message along the lines of 

```commandline
'python' is not recognized as an internal or external command
```

you need to add Python to your PATH (which means the
**:fontawesome-brands-python: Python** executable is simply not found).

We cover two options to fix the PATH issue, either use the command prompt 
or the GUI.

=== "Option 1: GUI"

    **Step 1**:
    
    First, we need to find the path to the executable. 
    
    Open the :fontawesome-brands-windows: Windows search and type `python`.
    Select `Dateispeicherort öffnen` (open file location). Open the context menu
    of `Python` (that's just a shortcut) and select `Eigenschaften` (properties)
    :octicons-arrow-right-24: `Dateipfad öffnen` (open file path). 
    Lastly, copy the path of the newly opened explorer window.
    
    <img
        height="750" src="/assets/python/installation/get-path.gif"
        style="border-radius: 10px;"
    />
    <figcaption style="text-align: center;">
        Determine the path to the Python executable.
    </figcaption>
    
    **Step 2**:
    
    Now, we need to add the path to the environment variables. Again use 
    the :fontawesome-brands-windows: Windows search and type 
    `Umgebungsvariablen` (Environment variables). Select the Path value in the 
    `Benutzervariablen für <user-name>` (User variables) section. Click on 
    `Neu` (New) and paste the copied path.
    
    <div style="text-align: center;">
        <img
            height="750" src="/assets/python/installation/add-path.gif" width="400" 
            style="border-radius: 10px;"
        />
        <figcaption style="text-align: center;">
            Add the path to the user variables.
        </figcaption>
    </div>

=== "Option 2: Command prompt"

    **Step 1**:

    Determine the path to the **:fontawesome-brands-python: Python** executable 
    using the Python launcher `py` (which is part of the Python installation and 
    is on PATH by default).
    
    ```commandline
    py -3.12 -c "import sys; print(sys.executable)"
    ```
    
    In my case, the output is:
    
    ```title="CMD Output"
    C:\Users\ztklotz\AppData\Local\Programs\Python\Python312\python.exe
    ```
    
    Copy your path *without* the `python.exe` part.
    
    **Step 2**:
    
    Set the PATH variable using the command prompt.
    
    ```commandline
    setx PATH "%PATH%;<copied-path>"
    ```
    
    For instance (using my path):
    
    ```commandline
    setx PATH "%PATH%;C:\Users\ztklotz\AppData\Local\Programs\Python\Python312"
    ```

**Step 3**:

Again, verify the installation by typing `python --version` in your command 
prompt.

---

With **:fontawesome-brands-python: Python** installed, the next step is to set
up a code editor. In the following section, we will install Visual Studio Code
(VS Code).
