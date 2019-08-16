# Docstrings

[PEP 8](https://www.python.org/dev/peps/pep-0008/) recommends some conventions for writing good documentation strings (aka docstrings). These conventions are detailed in [PEP 257](https://www.python.org/dev/peps/pep-0257/).

Python docstrings come in different formats. Which one you choose is up to you, but **stay consistent** within your project.



## Docstring formats

In the following we will briefly present some minimal doctoring examples from the three most common formats. The example we use can be found at [RealPython](https://realpython.com/documenting-python-code/#docstring-formats).

Consider the function `get_spreadsheet_cols()`. This function uses Pandas to read an Excel file and returns the column headers:

```python
def get_spreadsheet_cols(file_loc, print_cols=False):
    file_data = pd.read_excel(file_loc)
    col_headers = list(file_data.columns.values)

    if print_cols:
        print("\n".join(col_headers))

    return col_headers
```

A minimal docstring should contain a one-liner that summarises the function, followed by a description of the parameters and the return value. Below are three minimal examples in the most popular formats: **reStructuredText**, **Google docstrings** and **NumPy/Scipy docstrings**.

### reStructuredText

```python
"""Gets and prints the spreadsheet's header columns

:param file_loc: The file location of the spreadsheet
:type file_loc: str
:param print_cols: A flag used to print the columns to the console
    (default is False)
:type print_cols: bool
:returns: a list of strings representing the header columns
:rtype: list
"""
```

(If you use PyCharm, this may look familiar.)

### Google docstrings

```python
"""Gets and prints the spreadsheet's header columns

Parameters:
    file_loc (str): The file location of the spreadsheet
    print_cols (bool): A flag used to print the columns to the console
        (default is False)

Returns:
    list: a list of strings representing the header columns
"""
```

### NumPy/Scipy docstrings

```python
"""Gets and prints the spreadsheet's header columns

Parameters
----------
file_loc : str
    The file location of the spreadsheet
print_cols : bool, optional
    A flag used to print the columns to the console (default is False)

Returns
-------
list
    a list of strings representing the header columns
"""
```

The Numpy/SciPy docstring format also strongly encourages the inclusion of examples in the docstring. Examples are parsed and run via the `docstring` package. The idea is to make sure that the examples are running as shown. Check the documentation in the Resources section to see how to write docstring examples. **Note:** Examples are not meant to replace unit tests.



# Resources

[[RealPython] Documenting Python Code: A Complete Guide](https://realpython.com/documenting-python-code/#documenting-your-python-code-base-using-docstrings)

[PEP 8: Style Guide for Python](https://www.python.org/dev/peps/pep-0257/)

[PEP 257: Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)

[Numpydoc docstring guide](https://numpydoc.readthedocs.io/en/latest/format.html)

[Google docstring guide (section 3.8)](https://github.com/google/styleguide/blob/gh-pages/pyguide.md)

