# Installation

In this section, we will guide you through the installation process of
**:fontawesome-brands-python: Python**.

???+ danger

    Before you skip the content and proceed with the installation, we encourage you
    to read our instructions. Following them, will save you some time and potential
    headaches with the setup process!

______________________________________________________________________

=== ":fontawesome-brands-windows: Windows"

    Following video walks you through the installation steps for
    :fontawesome-brands-windows: Windows.

    <div style="text-align: center;">
        <iframe width="840" height="480" 
            src="https://www.youtube.com/embed/wqawj4XK8UE?si=Wjlt4L-KfU7Ho2qQ"
            title="YouTube video player" frameborder="0" allow="accelerometer;
            autoplay; clipboard-write; encrypted-media; gyroscope; 
            picture-in-picture; web-share" 
            referrerpolicy="strict-origin-when-cross-origin" 
            allowfullscreen>
        </iframe>
    </div>

    If you prefer a written guide follow the next couple of sections.

    <h2>Step 1: :fontawesome-solid-download: Download</h2>

    We recommend installing **:fontawesome-brands-python: Python** `3.14`.

    1. Visit the official website
        [python.org :octicons-link-external-16:](https://www.python.org)
    1. Navigate to **Downloads**
    1. Select the *Python install manager* to automatically trigger the download
    1. Once downloaded, open the MSIX file (MSIX is the Windows application
        distribution format)

    <h2>Step 2: :fontawesome-solid-arrow-pointer: Run installer</h2>

    1. Click **"Install Python"** to begin the installation

    1. A new Terminal window will open

    1. **Optional:** If prompted with "Open Settings to modify App execution
        aliases":

        - Type `y` and press ++enter++
        - In the Settings app, search for `alias`
        - Navigate to **App execution aliases**
        - Toggle the Python aliases **on**

        ???+ info

            The app alias configuration is an optional step that may appear during
            installation. It might not be necessary on your machine. Properly configured
            aliases allow you to execute Python commands from the terminal.

    1. When prompted `Install CPython now? [Y/n]`:

        - Press ++enter++ to accept the default option (Yes)

    1. When prompted `View online help? [y/N]`:

        - Press ++enter++ to skip this step
        - The terminal will close automatically

    <h3>Step 3: :fontawesome-solid-check-circle: Verify Installation</h3>

    1. Open a new terminal window (use Windows search with the keyword `terminal`)

    1. Check your installation by running:

        ```commandline
        python --version
        ```

    1. You should see output similar to:

        ```
        Python 3.14.*
        ```

        where `*` represents the specific patch version.

=== ":fontawesome-brands-apple: macOS"

    ???+ tip ":fontawesome-brands-apple: Are you on Apple silicon?"

        If you are using an Apple silicon Mac (M1, ... M4), you can also pick the
        `macOS 64-bit universal2 installer`.

    ???+ info

        Unfortunately, we do not have a installation video for macOS (yet). If you're
        having any trouble, please reach out to us!

    Nevertheless, the installation process is straightforward. Double click the
    downloaded `python-3.12.9-macos11.pkg` file and follow the installation
    instructions.

    Make sure to `Add python to PATH` during the installation process!

    After the successful installation, open a terminal (use the spotlight search
    with the keyword `terminal`) and verify the installation by typing

    ```bash
    python3 --version
    ```

    which should result in

    ```
    Python 3.12.9
    ```

______________________________________________________________________

<h2>Done!</h2>

If everything went smoothly, you have successfully installed
**:fontawesome-brands-python: Python**!

<div style="text-align: center;">
    <iframe src="https://giphy.com/embed/XreQmk7ETCak0" 
    width="336" height="252" style="" frameBorder="0" class="giphy-embed" 
    allowFullScreen
    >
    </iframe>
</div>

______________________________________________________________________

With **:fontawesome-brands-python: Python** installed, the next step is to set
up a code editor. In the following section, we will install Visual Studio Code
(VS Code).
