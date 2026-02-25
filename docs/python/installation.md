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
            allowfullscreen style="border-radius: 15px;">
        </iframe>
    </div>

    If you prefer a written guide follow the next couple of sections.

    <h2>Step 1: :fontawesome-solid-download: Download</h2>

    We recommend installing **:fontawesome-brands-python: Python** `3.14`!

    1. Visit the official website
        [python.org :octicons-link-external-16:](https://www.python.org)
    1. Navigate to **Downloads**
    1. A section **"Download for Windows"** will automatically appear
    1. Click the button **Python install manager**
    1. Locate the downloaded `.msix` file in your Downloads folder

    <h2>Step 2: :fontawesome-solid-arrow-pointer: Run installer</h2>

    1. Double-click the `.msix` file to launch the install manager.

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

    <h2>Step 3: :fontawesome-solid-check-circle: Verify Installation</h2>

    1. Open a new terminal window (use Windows search with the keyword 
        `terminal`)

    1. Check your installation by running:

        ```commandline
        python --version
        ```

    1. You should see output similar to:

        ```
        Python 3.14.x
        ```

        where `x` represents the specific patch version (e.g., `3.14.3` or 
        `3.14.4`).

=== ":fontawesome-brands-apple: macOS"

    ???+ info

        Unfortunately, we do not have a installation video for macOS (yet). 
        If you're having any trouble, reach out to us!
    
    <h2>Step 1: :fontawesome-solid-download: Download</h2>

    We recommend installing **:fontawesome-brands-python: Python** `3.14`.

    1. Visit the official website
        [python.org :octicons-link-external-16:](https://www.python.org)
    1. Navigate to the **Downloads** tab
    1. A section **"Download for macOS"** will automatically appear
    1. Click the **Python 3.14.x** button to download
    1. Locate the downloaded `.pkg` file in your Downloads folder

    <h2>Step 2: :fontawesome-solid-arrow-pointer: Run installer</h2>

    1. Double-click the `.pkg` file to launch the installer
    1. Follow the installation wizard:
        - Click **Continue** through the introduction screens
        - Accept the license agreement
        - Click **Install** and enter your password if prompted
        - Wait for the installation to complete
    
    ???+ danger

        **Important:** After installation completes, Finder will automatically open,
        showing the Python installation folder. You **must** complete this final step:
        
        - Double-click the `Install Certificates.command` file
        - A Terminal window will open and execute the certificate installation
        - Wait for it to complete and close automatically
        
        This step is required for Python to make secure HTTPS connections.

    <h2>Step 3: :fontawesome-solid-check-circle: Verify Installation</h2>

    1. After the successful installation, open a terminal (use the spotlight 
        search with the keyword `terminal`)

    1. Verify the installation by typing:

        ```bash
        python3 --version
        ```

    1. You should see output similar to:

        ```
        Python 3.14.x
        ```

        where `x` represents the specific patch version (e.g., `3.14.3` or 
        `3.14.4`).

______________________________________________________________________

<h2>Done!</h2>

If everything went smoothly, you have successfully installed
**:fontawesome-brands-python: Python**! :tada:

<div style="text-align: center;">
    <img src="https://media.giphy.com/media/111ebonMs90YLu/giphy.gif" />
</div>

______________________________________________________________________

With **:fontawesome-brands-python: Python** installed, the next step is to set
up a code editor. In the following section, we will install Visual Studio Code
(VS Code).
