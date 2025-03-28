# Contributions

We're really glad, you found your way here. 👋🏽 Contributions are welcomed, 
thank you in advance for improving the site!

## How to contribute

1. **Report Issues**: Found a bug, error, or non-working code snippet? Please 
open an issue [here](https://github.com/JakobKlotz/python-template/issues). 
Whether it's broken images, improperly rendered formulas, or anything else, 
let us know by reporting it. It's a great help for us!
2. **Submit Pull Requests**: Eager to submit changes yourself? 
Fork the repository, create a branch, make your changes, and submit a 
pull request.

> [!NOTE]
> If you're addressing an open issue, consider commenting on the issue to let others know you're working on it.

## Create a Pull Request

### Introduction

Submitting changes through a pull request?
Please follow the instructions below to ensure a smooth collaboration process.

### Steps

To get started follow these steps:

1. Create a fork of the repository. To do so, click on the fork button on the 
top right of the repository page.
2. Clone your fork locally.
3. Create and checkout a new branch.
4. Install the dependencies, refer to the [local development](README.md#1️⃣-prerequisites) 
section in the README.
5. Preview the site locally. On Windows, run [serve-local.bat](serve-local.bat).  
    For Linux and macOS, use the following command:  
    ```bash
    ENABLE_GIT_COMMITTERS=false ENABLE_GIT_REVISION_DATE=false mkdocs serve
    ```
    Disabling the `git-committers` and `git-revision-date-localized` plugins 
    is recommended, as they can significantly slow down the build process.

6. Open `localhost:8000` in your browser to view the site.  
7. Make your changes and see them reflected in real-time.
8. Commit and push your changes.
9. Visit the GitHub page of your fork and create a Pull Request.

That's it! Now you can sit back, relax, and enjoy a cup of coffee or tea while
we review your contribution. We'll get back to you soon! 😊

## Conventions

### Course Content

When adding or modifying course content, ensure that you look at existing 
pages. Use the same styling, such as admonition boxes, formatting, and 
structure, to ensure uniformity across the project. 
As a reference you can use the [CART chapter](docs/data-science/algorithms/supervised/tree-based/cart/)
which includes code blocks (including highlighting and annotations), formulas,
tables, graphs and images. 

### Commit Messages

If your changes are addressing a particular issue, reference the issue within
your commit message. For example:

```plaintext
git commit -m "docs: added contribution guidelines #97"
```

Issues can be referenced with a `#` and the corresponding issue number.

---

Thank you for improving the site! 🚀

Manuel & Jakob
