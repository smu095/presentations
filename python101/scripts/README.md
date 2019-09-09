# Tutorial

First, make sure you have installed `flake8`, `black` and `mypy`.

```bash
$ pip install flake8 black mypy
```

Consult the subsections below on information about how to run the different listing/autoformatting packages. Make sure you understand the output. Refer to the package documentation for more info.

## Flake8

`code_with_lint.py` and `code_without_lint.py` are examples of code with and without linting errors. To use `flake8` on these, write the following command in your terminal:

```bash
$ flake8 code_with_lint.py
$ flake8 code_without_lint.py
```

Documentation: http://flake8.pycqa.org/en/latest/

## Black

`unformatted_code.py` is an example of unformatted code that is not PEP 8 compliant. To autoformat this file with `black`, type the following command in your terminal:

```bash
$ black unformatted_code.py
```

Documentation: https://black.readthedocs.io/en/stable/

## Mypy

`type_hinting_example.py` and `variable_hints.py` are examples of code with type annotations for static type checking. To use `mypy` on these, write the following command in your terminal:

```bash
$ mypy type_hinting_examples.py
$ mypy variable_hints.py
```

Documentation: https://mypy.readthedocs.io/en/latest/