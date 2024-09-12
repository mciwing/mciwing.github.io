<div style="text-align: center;">

# MCI | WING

<div style="text-align: center;">
  <img src="docs/assets/logo.png" alt="WING Logo" style="width: 200px; height: auto;">
</div>

**Visit the site [here](https://mciwing.github.io/).**

</div>


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

The site will be available at `localhost:8000`

</details>
