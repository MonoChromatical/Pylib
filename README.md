# Pylib

A personal Python utility library containing reusable modules, functions, and tools that extend Python's standard functionality.

The goal of this repository is to build a collection of lightweight utilities for common tasks without relying on unnecessary third-party dependencies. Where practical, features are implemented using only the Python standard library, making the package easy to install and use in any project.

As the library grows, it will include utilities that:

* Fill gaps in Python's built-in functionality.
* Replace simple third-party dependencies where a lightweight alternative is sufficient.
* Provide reusable helpers that can be shared across multiple projects.

## Installation

Install directly from GitHub:

```bash
py -m pip install git+https://github.com/MonoChromatical/Pylib.git
```

## Usage

Import modules using the following structure:

```python
from pylib.<package_name>.<module_name> import *
```

Or import only the specific objects you need:

```python
from pylib.<package_name>.<module_name> import MyClass
```

## Philosophy

Pylib is built around a few simple principles:

* **Minimal dependencies** – Prefer the Python standard library whenever possible.
* **Reusable** – Write utilities that can be shared across multiple projects.
* **Lightweight** – Keep implementations simple and efficient.
* **Expandable** – Continue adding new modules and utilities as the library evolves.

Rather than depending on several small third-party packages, the aim is to build a single collection of commonly used utilities that can be reused across future projects.

## Status

This project is under active development. New modules and functionality will be added over time, and APIs may change as the library matures.

## Contributing

Issues, suggestions, and pull requests are welcome. If you have an idea for a useful utility or an improvement to an existing module, feel free to contribute.

## Contributers
MechtrixPrime

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
