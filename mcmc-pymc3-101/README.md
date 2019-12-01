# An introduction to Markov Chain Monte Carlo and PyMC3

This repo will contain presentation materials for Monday talk about [Markov Chain Monte Carlo
methods](https://en.wikipedia.org/wiki/Markov_chain_Monte_Carlo) and their practical applications using the [probabilistic programming
framework PyMC3](https://docs.pymc.io/).

## Todo list
See [issue #12](https://github.com/smu095/presentations/issues/12) for an up-to-date to do-list.

## Contents
```bash
.
├── README.md
├── notebooks
│   └── README.md
└── slides
    └── README.md
```

## Setup
This repo assumes that you have installed the [Anaconda distribution](https://www.anaconda.com/distribution/). To create and activate a conda environment with all the necessary dependencies, type the following commands into the terminal:

```bash
$ conda env create -f environment.yml
$ conda activate fagdag-pymc3
```

To enable [`black`](https://black.readthedocs.io/en/stable/) for autoformatting code in Jupyter notebooks, enter the
following commands in the terminal:

```bash
$ jupyter nbextension install https://github.com/drillan/jupyter-black/archive/master.zip --user
$ jupyter nbextension enable jupyter-black-master/jupyter-black
```

To enable autoformatting, click `View > Toggle Toolbar` after opening a new
notebook.
## Contributions
Pull request (PRs) are welcome. Note that this repo enforces master protection. Contributors must submit a PR and be reviewed before being approved for merging into the master branch. We require that code is
[PEP8 compliant](https://www.python.org/dev/peps/pep-0008/) and autoformatted using [`black`](https://black.readthedocs.io/en/stable/).

