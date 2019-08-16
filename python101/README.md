# Tools for Writing Consistent and Reliable Python Code

### Contents

```bash
.
├── README.md
├── docs
│   ├── docstrings.md
│   ├── ide_setup.md
│   ├── style_guide.md
│   └── type-hinting.md
├── imgs
│   ├── black.gif
│   ├── lint1.gif
│   ├── lint1.png
│   ├── lint2.gif
│   ├── lint2.png
│   └── pep8.png
├── requirements.txt
├── scripts
│   ├── code_with_lint.py
│   ├── code_without_lint.py
│   ├── type_hinting_example.py
│   ├── unformatted_code.py
│   └── variable_hints.py
└── slides
    ├── python101.pdf
    └── python101.pptx

4 directories, 20 files
```

[**`docs`:**]( https://github.com/smu095/presentations/tree/master/python101/docs) Contains summaries of relevant topics.

[**`imgs`:**](https://github.com/smu095/presentations/tree/master/python101/imgs ) Contains images and gifs used in slides.

[**`scripts`:**]( https://github.com/smu095/presentations/tree/master/python101/scripts) Contains example Python scripts used in slides.

[**`slides`:**](https://github.com/smu095/presentations/tree/master/python101/slides ) Contains .pdf and .pptx versions of slides.

[`requirements.txt`:]( https://github.com/smu095/presentations/blob/master/python101/requirements.txt) Contains required packages to run examples in slides.

### Reproducing examples

The following commands can be used to run the examples featured in the slides.

#### Flake8

```bash
$ flake8 code_with_lint.py 
```

```bash
$ flake8 code_without_lint.py
```

#### Black

```bash
$ black unformatted_code.py
```

#### Mypy

```bash
$ mypy type_hinting_example.py
```

```bash
$ mypy variable_hints.py
```

