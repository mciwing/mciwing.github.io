[![GitHub Pages](https://img.shields.io/badge/github%20pages-121013?style=for-the-badge&logo=github&logoColor=white)](https://mciwing.github.io/)
![Python](https://img.shields.io/badge/Python-3.12-blue)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

<div align="center">
    <h1>MCI | WING</h1>
</div>

<p align="center">
  <img src="docs/assets/logo.png" alt="WING Logo" style="width: 200px; height: auto;">
</p>

<div align="center">
<hr>

Visit the site <a href="https://mciwing.github.io/">here</a>
</div>

---

<details>
<summary>Local development</summary>

To serve the site locally, you need a couple of prerequisites (`pipx`, `poetry` 
and `python >= 3.11 < 3.13`)

### `pipx`

Install `pipx`

```bash
python -m pip install --user pipx
```

which will throw a warning that `pipx` is not on Path. Navigate to the 
path mentioned in the warning and execute

```bash
.\pipx.exe ensurepath
```

### `poetry`

In a new terminal, install `poetry`

```bash
pipx install poetry
```

### Project setup

To install all project dependencies, navigate to the project root and execute

```bash
poetry install
```

### Serve the site

... with

```bash
poetry run mkdocs serve
```

The site is served at `localhost:8000`

</details>

## License

This work is licensed under a 
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).