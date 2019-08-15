# Type Hinting in Python

Summary based on [Python Type Checking (Guide)](https://realpython.com/python-type-checking/) at [realpython.com](https://realpython.com/).

Python is a dynamically typed language. This means that Python only does type checking only as the code runs. For example:

```python
>>> if False:
...  1 + "two"
... else:
...  1 + 2
3

>>> 1 + "two" # This will throw a TypeError
```

In Python, the type of an object is allowed to change, and the type is correctly inferred as it changes:

```python
>>> thing = "Hello"
>>> type(thing)
<class 'str'>
>>> thing = 42
>>> type(thing)
<class 'int'>
```

This stands in contrast to statically typed languages, such as Java, where types are checked as the program compiles:

```java
String thing;
thing = "Hello";
```

In the snippet above, `thing` can never be assigned a value that is not a `String` object.

##  What is type hinting?

[PEP 484](https://www.python.org/dev/peps/pep-0484/) introduces *type hinting* which makes it possible to do static type checking in Python. 

However, in Python type hints are literally *hints*, meaning that they simply suggest types but do not enforce them. Other tools (such as [mypy](http://mypy-lang.org/)) perform static type checking.

**Example.** Consider the following script, available in `type_hinting_example.py`. This is an example of function annotation, the most common use case for type hinting:

```python
def hello(text: str, caps: bool) -> str:
    """ Returns text in all caps if caps = True, else returns 
    text capitalised."""
    if caps:
        return text.upper()
    else:
        return text.capitalize()
    
print(hello("Hello my friend!", caps=True))
print(hello("Hello my friend!", caps="True"))
```

This program runs fine, even though we pass the wrong kind of argument to the function. In this contrived example it doesn't really matter, but ideally we would like to catch this mistake.

Running mypy on `type_hinting_example.py` in your shell results in:

```shell
$ mypy type_hinting_example.py 
type_hinting_example.py:17: error: Argument "caps" to "hello" has incompatible type "str"; expected "bool"
```

Mypy tells us we are using the wrong type in line 17.

## Why are type hints useful?

Type hints are good because they:

* help document your code,
* help catch (potentially many) bugs in one fell swoop,
* improve certain IDEs (such as PyCharm) and linters, 
* force you to think about the software you are designing,
* can be introduced as needed, which is useful when refactoring or maintaining older code bases.

Type hints are not so good because they:

* take time and effort to add,
* requires Python 3.5+,
* introduce some overhead,
* introduces unneeded verbosity.

## Should you use type hinting?

Considerations:

* Adds little value in short throw-away scripts.
* Adds a lot of value in bigger, collaborative projects. Helps developers understand flow of types through code.

Quoting [The State of Type Hints in Python](https://www.bernat.tech/the-state-of-type-hints-in-python/):

> Type hints should be used whenever unit tests are worth writing.

## Syntax of function annotation

You can annotate arguments and return value of a function in Python 3. Consider again `type_hinting_example.py`:

```python
def hello(text: str, caps: bool) -> str:
    """ Returns text in all caps if caps = True, else returns 
    text capitalised."""
    if caps:
        return text.upper()
    else:
        return text.capitalize()
    
print(hello("Hello my friend!", caps=True))
print(hello("Hello my friend!", caps="True"))
```

The annotation is in te`text: str` indicates that the argument text should be of type `str`. Likewise, `caps: bool` indicates that caps should be a Boolean variable. The return value is specified by the right arrow `-> str`. 

The syntax of type hinting is based on [PEP 8](https://www.python.org/dev/peps/pep-0008/), and is summarised in the following:

* No space before colon and one after.
* Spaces around `=` when assigning default variable.
* Use spaces around `->` when annotating return type.

Variables can also be annotated in Python 3:

```python
pi: float = 3.142
empty_string: str # We can assign types without assigning values
```

##The `typing` module

How do we annotate composite types, like a list of strings or a tuple of integers? Enter the `typing` module:

```python
from typing import List, Dict, Tuple

list_example: List[str] = ["These", "are", "defaults"]
dict_example: Dict[str, bool] = {"Example 1": True, "Example 2": False}
tuple_example: Tuple[int, int, int] = (1, 2, 3)
```

**Note:** Tuples are an immutable sequence typically consisting of a fixed number of possibly differently typed elements. For an n-tuple, we would write `Tuple[t_1, t_2, ..., t_n]`. Lists typically have an unknown number of elements of the same type, which is why there is only one type in `List[t]`. In some cases we don't really care if the argument or variable is a list or a tuple. In these cases we could use `Sequence`. The `typing` module contains many different composite types. See [documentation](https://docs.python.org/3/library/typing.html) for more info.

A common design pattern is to assign `None` as a default value to an argument. `typing` has the `Optional` type to accomodate this. E.g.:

```python
from typing import Optional

def some_function(optional_string: Optional[str] = None) -> None:
  """ Returns optional_string if provided."""
  if optional_string:
    print(optional_string)
  else:
    print("No string argument passed.")
```

Alternatively, one could use `Union[None, str]` which can be read as one of `None` *or* `int`.

**Note:** Since `some_function` does not have a return value, we annotate it with `-> None`.

## Miscellaneous

### Type hinting in object-oriented programming

**Methods**. Type hints for methods work the same way as type hints for functions. The only difference is that the `self` argument does not need to be annotated and that the `.__init__()` method should always return `None`.

**Classes.** To use classes as types, simply use the name of the class. There are some details here, please refer to [RealPython: Classes as Types](https://realpython.com/python-type-checking/#classes-as-types).

### Annotating `*args` and `**kwargs`

You should only annotate the type of the inputs, e.g.:

```python
def some_function(*args: str, **kwargs: int) -> None:
  pass
```

### Callables

Functions, lambdas, methods and classes are represented by `typing.Callable`. For example, when passing a function as an argument:

```python
from typing import Callable

def do_twice(func: Callable[[str], str], argument: str) -> None:
  """Print output of func when passed argument, twice."""
  print(func(argument))
  print(func(argument))
```

**Note:** `Callable[[str], str]` indicates that the function accepts a string as an argument and returns a string.

## Performing type checking

Performing static type checking is done through [mypy](http://mypy-lang.org/). Install using `pip`:

```bash
$ pip install mypy
```

Perform type checking by running mypy through command line interface:

```bash
$ mypy type_hinting_example.py
type_hinting_example.py:17: error: Argument "caps" to "hello" has incompatible type "str"; expected "bool"
```

**Note:** Some popular packages, such as NumPy, do not contain type hints. In these cases, we want to use the `--ignore-missing-import` command line option when running mypy.

## Resources

#### Documentation

[PEP 484: Type Hints](https://www.python.org/dev/peps/pep-0484/)

[PEP 3107: Function Annotations](https://www.python.org/dev/peps/pep-3107/)

[PEP 526: Syntax for Variable Annotation](https://www.python.org/dev/peps/pep-0526/)

[PEP 563: Postponed Evaluation of Annotations](https://www.python.org/dev/peps/pep-0563/)

#### Blogs

[A deep dive on Python type hints (Vicki Boykis)](https://veekaybee.github.io/2019/07/08/python-type-hints/)

[The state of type hints in Python (Bernat Gabor)](https://www.bernat.tech/the-state-of-type-hints-in-python/)

#### Tutorials

[RealPython: Python Type Checking (Guide)](https://realpython.com/python-type-checking/)

#### Presentations

[Type hinting and Mypy (Bernat Gabor, PyCon2019)](https://www.youtube.com/watch?v=hTrjTAPnA_k)

[Getting started with Mypy and type checking (Jukka Lehtosalo, europython 2018)](https://www.youtube.com/watch?v=18nZ5xMeGno)

