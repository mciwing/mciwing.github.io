# Installation

In this section, we will guide you through the installation process of
**:fontawesome-brands-python: Python**.

???+ danger

    Before you skip the content and proceed with the installation, we encourage
    you to read our instructions. Following them, will save you some time
    and potential headaches with the setup process!

---

## Step 1: :fontawesome-solid-download: Download

We urge you to install **:fontawesome-brands-python: Python** `3.12.9`. 
Visit the official website [python.org :octicons-link-external-16:](https://www.python.org/downloads/release/python-3129/), 
scroll to the bottom of the page and download the installer for your operating 
system.

Now, <span style="color:red">do not run the installer just yet</span> - watch 
the below video first! It will save you time! :ok_hand:

???+ tip ":fontawesome-brands-apple: Are you on Apple silicon?"

    If you are using an Apple silicon Mac (M1, ... M4), you can also pick 
    the `macOS 64-bit universal2 installer`.

## Step 2: :fontawesome-solid-arrow-pointer: Run installer

No matter which operating system you're on, When installing Python, make sure 
that you check the box `Add python.exe to PATH`!
Now run the Python installer.

=== ":fontawesome-brands-windows: Windows"

    <div style="text-align: center;">
        <iframe 
            width="840" height="473" 
            src="https://www.youtube.com/embed/fpxdo5QYvmM?si=vjsmF84v80GsgeK6"
            title="YouTube video player" frameborder="5" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; 
            gyroscope; picture-in-picture;" 
            referrerpolicy="strict-origin-when-cross-origin"
        >
        </iframe>
    </div>

    After the successful installation, we recommend to open a command prompt
    (use the Windows search with the keyword `cmd`) and verify the installation
    by typing 

    ```commandline
    python --version
    ```

    Which should result in:
    
    ```title="CMD Output"
    Python 3.12.9
    ```

=== ":fontawesome-brands-apple: macOS"
    
    ???+ info

        Unfortunately, we do not have a installation video for macOS (yet). 
        If you're having any trouble, please reach out to us!

    Nevertheless, the installation process is straightforward. Double click the
    downloaded `python-3.12.9-macos11.pkg.pkg` file and follow the installation
    instructions.

    Make sure to `Add python to PATH` during the installation process!

    After the successful installation, open a terminal (use the spotlight search
    with the keyword `terminal`) and verify the installation by typing 

    ```bash
    python --version
    ```
    
    Alternatively, if that does not work, try 

    ```bash
    python3 --version
    ```

    which should result in
    
    ```
    Python 3.12.9
    ```

---

## Step 3: :fontawesome-solid-check: Done!

If everything went smoothly, you have successfully installed 
**:fontawesome-brands-python: Python**! You can now skip the 
troubleshooting part and proceed with the next chapter. :party_popper:

---

## Optional: Troubleshooting

???+ info

    The troubleshooting section is specific to :fontawesome-brands-windows:
    Windows. If you're on :fontawesome-brands-apple: macOS and encounter 
    issues, please reach out to us!

### PATH issues

If you didn't check the box `Add python.exe to PATH` during 
installation, or you encounter an error message along the lines of 

```commandline
'python' is not recognized as an internal or external command
```

you need to add Python to your PATH (which means that
**:fontawesome-brands-python: Python** is simply not found).

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

Again, verify the installation by typing `python --version` within a command 
prompt.

---

With **:fontawesome-brands-python: Python** installed, the next step is to set
up a code editor. In the following section, we will install Visual Studio Code
(VS Code).
