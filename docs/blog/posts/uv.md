---
date:
  created: 2025-08-07
readtime: 3
pin: true
authors:
  - jakob
slug: uv
---

# `uv`: My favourite Python package manager

![uv-post-thumbnail](../../assets/blog/uv-thumbnail.png)

TLDR: [`uv`](https://docs.astral.sh/uv/) simplifies the whole development 
experience. I use it daily to manage my Python projects and it has become an 
essential part of my workflow. A brief overview to get you started...

<!-- more -->

## What is `uv`?

It lets you manage your Python packages. But not just that, with `uv` you 
can also manage your Python installations. On top of that, it is way faster than
other package managers like `pip`.

## Why `uv`?

Setting up a new development environment has never been easier. On a new machine,
I can simply [install](https://docs.astral.sh/uv/getting-started/installation/) 
`uv` which is just a single command. Having `uv` installed, run:

```bash
uv python list
```

... to list all available Python versions. With another command, for example:

```bash
uv python install 3.13
```

... I can install the latest Python version. 
So with just 2 commands, I have a working Python development environment on my 
machine. There's no need to install Python manually anymore. 🚀

???+ tip
    With

    ```bash
    mkdir my_project && cd my_project
    uv init  #(1)!
    uv sync  #(2)!
    ```

    you can scaffold a new Python project and set up the virtual environment. 
    You can start developing right away.

    1. `uv init` creates a new project with a default configuration.
    2. `uv sync` sets up the virtual environment.

## Another example

Most of the time, programming is a team sport. Working with others on the same
codebase can be challenging, especially when it comes to managing dependencies.
Installing an existing project that was built with `uv`, is as simple as:

```bash
uv sync
```

???+ info

    `uv sync` reads the `pyproject.toml` and `uv.lock` files to install the 
    required dependencies and sets up the virtual environment. If you don't 
    have the required Python version installed, `uv` will automatically install
    it for you.


## Wrap up

Although this introductory post is just a brief overview, I hope it gives you 
an idea of how `uv` can simplify your Python development workflow. In 
subsequent posts, I will dive deeper into specific features and use cases of 
`uv`. Until then, you can take a look at a couple of projects that use `uv`:

- This site you're reading right now is built with `uv` - [code](https://github.com/mciwing/mciwing.github.io).
- Two Python packages I develop, [first](https://github.com/JakobKlotz/md-snakeoil) and
[second](https://github.com/JakobKlotz/tiler-api)
- An app to assess rainfall-triggered landslide risks - [here](https://github.com/JakobKlotz/lhasa-app/tree/main/backend).
