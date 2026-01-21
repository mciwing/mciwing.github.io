[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-121013?style=flat-square&logo=github&logoColor=white)](https://mciwing.github.io/)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=flat-square&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-blue?style=flat-square&logo=python&logoColor=white)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg?style=flat-square&logo=creativecommons&logoColor=black)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

<div align="center">
  <h1><b>CODE CAMPUS</b></h1>
  <img src="docs/assets/icon.PNG" alt="WING Logo" style="width: 250px; height: auto;">
  <hr>
</div>

This site offers a variety of courses focused on Python, including:

- Python Programming
- Data Science
- Statistics
- Computer Vision
- MicroPython

📚 Visit the site [here](https://code-campus.at/)!

## Docker

To build and serve the site with `docker`, use:

```bash
docker compose up -d --build
```

That's it! 🚀 Visit the site at [http://localhost:8001](http://localhost:8001)

## Local development

Eager to contribute or develop locally? Here's how to get started!

### 1️⃣ Install `uv`

This site is built using the `uv` package manager. If you haven't installed it
yet, navigate to their [installation guide](https://docs.astral.sh/uv/getting-started/installation/)
and follow the instructions.

### 2️⃣ Project setup

Install all dependencies with:

```bash
uv sync
```

### 3️⃣ Serve the site

Lastly, serve the site locally with:

```bash
uv run dev.py
```

> [!NOTE]
> The script disables the `git-committers` and `git-revision-date-localized` plugin for faster local builds.

Visit `localhost:8000` in your browser to view the site. 🎉

### 4️⃣ Write content

Now, you can start writing content. While the site is served locally, any changes 
will automatically trigger a reload of the site in your browser.

> [!TIP]
> The sites content is housed in the `docs/` directory and is written in Markdown.
> For formatting reference, check out the [Material for MkDocs documentation](https://squidfunk.github.io/mkdocs-material/reference/).

## Contributions

Found a mistake, have an idea or want to report an issue? Contributions in any form are always welcome! 😊