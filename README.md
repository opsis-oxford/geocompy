# Geocomputation with Python

These materials are derived from the book "Geocomputation with Python", available at https://py.geocompx.org

> Dorman, M., Graser, A., Nowosad, J., & Lovelace, R. (2025). Geocomputation with Python. CRC Press

The material is shared under the "Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International" license.

Running the code requires the following:

1.  Python dependencies, which can be installed with
    [`pip`](https://pypi.org/project/pip/) or a package manager
2.  An integrated development environment (IDE) such as [VS
    Code](https://code.visualstudio.com/) (running locally or on
    Codespaces/other host) or Jupyter Notebook for running and exploring the
    Python code interactively

## Install dependencies with pip

Install [python](https://www.python.org/), which comes with the program
[`pip`](https://packaging.python.org/en/latest/tutorials/installing-packages/)
that can be used to install libraries.

Use `pip` to install the dependencies as follows, after cloning or downloading
this repository and opening a terminal in the root folder.

First we’ll set up a virtual environment to install the dependencies in:

```sh
# Create a virtual environment called geocompy
python -m venv geocompy
# Activate the virtual environment
source geocompy/bin/activate
```

Then install the dependencies (with the optional
[`python -m`](https://fosstodon.org/deck/@hugovk@mastodon.social/111311327842154267)
prefix specifying the Python version):

```sh
# Install dependencies from the requirements.txt file
python -m pip install -r requirements.txt
```

You can also install packages individually, e.g.:

```sh
pip install osmnx
```

Deactivate the virtual environment when you’re done:

```sh
deactivate
```

## Install dependencies with a package manager

The [`environment.yml`](environment.yml) file contains a list of
dependencies that can be installed with a package manager such as
`conda`, `mamba` or `micromamba`. The instructions below are for
[micromamba](https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html)
but should work for any package manager.

Install dependencies with the following command:

```bash
micromamba env create -f environment.yml
```

Activate the environment as follows:

```bash
micromamba activate geocompy
```

Install kernel, this will allow you to select the environment in vscode or
IPython as follows:

```bash
python -m ipykernel install --user
```

You can now run the notebooks

```bash
micromamba run -n geocompy jupyter notebook
```
