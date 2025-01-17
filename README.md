<div align="center">
   <img src="docs/assets/logo.png" alt="WING Logo" style="width: 200px; height: auto;">
   <h1>MCI | WING</h1>

   [![GitHub Pages](https://img.shields.io/badge/github%20pages-121013?style=for-the-badge&logo=github&logoColor=white)](https://mciwing.github.io/)
   ![Python](https://img.shields.io/badge/Python-3.12-blue)
   [![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

   <h2>📚 Visit the site <a href="https://mciwing.github.io/">here</a><h2>
</div>

---

<details>
<summary>🛠️ Local development</summary>

The site is built with 
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

To serve the site locally, you need a couple of prerequisites 
(`python >= 3.11 < 3.13`,`pipx` and `poetry`)

> **Note**: This project currently supports Python 3.11 and 3.12 only. While older
versions may work, they haven't been tested. We plan to add Python 3.13 support
once `mkdocs` extends compatibility to that version.

---

## 1️⃣ Prerequisites

### `pipx`

`pipx` lets you install and run Python applications in isolated environments.
We'll use it to install a package manager (`poetry`) later on.

1. To set it up:

    ```bash
    python -m pip install --user pipx
    ```

2. After installation, you'll see a warning that `pipx` is not in your system
   PATH. Copy the path shown in the warning message (this path varies by user).

3. Navigate to the copied path.

    ```bash
    cd your_path_from_warning
    ```

4. Set `pipx` to your PATH environment variable.

    ```bash
    .\pipx.exe ensurepath
    ```

### `poetry`

The project uses the package manager `poetry`. In a new terminal window,
install `poetry` with:

```bash
pipx install poetry
```

---

## 2️⃣ Project setup

To install all project dependencies, clone this repository and within the
project directory, run:

```bash
poetry install
```

## 3️⃣ Serve the site locally (on Windows)

Lastly, build and serve the site locally with:

```bash
.\serve-local.bat
```

> The script disables the `git-committers` plugin for faster local builds.
> Visit `localhost:8000` in your browser to view the site. 🎉

---

## ✍️ Contributing content

If you properly set up the project, you can now start writing content.
While the site is served locally, any changes you make to the content will 
automatically trigger a reload of the site in your browser.

The sites content is housed in the `\docs` directory and is written in Markdown.
For formatting reference, check out the 
[Material for MkDocs documentation](https://squidfunk.github.io/mkdocs-material/reference/).

</details>

---

<div align="center">
    <h2>📄 License</h2>

   This work is licensed under a 
   <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>
   
   <img src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" alt="by-nc-sa 4.0">
</div>


