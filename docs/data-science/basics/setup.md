# Setup

To get started, we setup the programming environment. Follow these couple
of steps to get ready, no prerequisites needed.

## Visual Studio Code

First, install a code editor. We urge you to instal Visual Studio Code a free 
and open-source editor developed by Microsoft :fontawesome-brands-windows:.

If you don't have Visual Studio Code already installed on your machine visit
the IDE chapter from the Python Course [here](../../python-extensive/ide.md)

## `uv`

One of this course’s aims is to give you as much insight into real-world 
projects as possible. We use uv, a popular, state-of-the-art tool to manage 
both your Python installations and virtual environments. 

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
