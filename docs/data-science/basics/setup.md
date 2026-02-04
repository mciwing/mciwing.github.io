# Setup

To get started, we setup the programming environment. Follow these couple
of steps to get ready, no prerequisites needed.

## Visual Studio Code

First, install a code editor. We urge you to instal Visual Studio Code (VS Code)
a free and open-source editor developed by Microsoft 
:fontawesome-brands-windows:.

If you don't have Visual Studio Code already installed on your machine visit
the IDE chapter from the Python Course [here](../../python-extensive/ide.md)

## `uv`

From the Python course you should already be familiar with the package manager
`pip`. That background will help you quickly understand `uv`, a modern tool that 
not only replaces `pip` for package management but also handles Python 
installations.

**Why the switch?** While `pip` remains widely used and important to understand,
this course aims to prepare you for modern real-world projects. `uv` has 
become a popular, state-of-the-art tool in modern Python development and 
learning it now will give you a competitive advantage.

???+ tip "No prior Python install necessary"

    A key benefit of uv is that you don’t need to install Python manually.

### 1. Install `uv`

=== ":fontawesome-brands-windows: Windows"

    Open Windows Powershell. Visit the uv documentation under under 
    "Standalone installer" [link](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_2).
    Make sure the Windows tab is selected.
    
    Return to PowerShell and paste the installer command shown in the docs.

    ![uv standalone installation](../../assets/data-science/basics/setup/uv-win-install.png)

=== ":fontawesome-brands-apple: MacOS / :fontawesome-brands-linux: Linux"

    On macOS or Linux, open Terminal. Visit the uv documentation under 
    "Standalone installer", [link](https://docs.astral.sh/uv/getting-started/installation/). 
    Make sure the macOS or Linux tab is selected.
    
    Return to your terminal and paste the installer command.

Press ++enter++ to execute the command

---

Regardless of your operating system, upon completion you should see 
something like:

```
Downloading uv
    uv
    uvx
    uvw
everything's installed!
```

You can now close the Terminal (:fontawesome-brands-apple: macOS / 
:fontawesome-brands-linux: Linux) or PowerShell (:fontawesome-brands-windows: 
Windows).

???+ info

    The following steps are OS-agnostic; they are the same for Windows, macOS 
    and Linux.

### 2. Create a project

Now, set up a new project.

???+ info

    A project is a folder that contains all scripts, configuration and data 
    files that belong together. Everything for the project lives in that 
    folder.

Create a new folder named `data-science` in an easy-to-find location you’ll 
use throughout this course.

Open VS Code. Go to File → Open Folder…, select the `data-science` folder. 
VS Code will open a new window.

???+ tip

    For more on navigating VS Code, see the Python course chapter: 
    [link](../../python-extensive/ide.md)

### 3. Initialize the project

In VS Code, open the integrated terminal (via Terminal → New Terminal).

```bash
uv init --vcs none
```

This initializes the project. uv creates a few files in your folder. 
Your workspace should look like this:

<figure markdown="span">
    <img 
        src="/assets/data-science/basics/setup/uv-init.png" width=75% 
        style="border-radius: 15px;"
    >
</figure>

#### Explore the new files

Click through these new files:

- `.python-version` Contains the Python version used by your virtual 
    environment.
- `main.py` An entry script to verify the setup (we’ll revisit this later).
- `pyproject.toml` Project metadata such as name and version.
- `README.md` An empty README for a project description; you can ignore it for 
    now.
