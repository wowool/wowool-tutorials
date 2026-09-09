## Notebooks — Setup Instructions

This folder contains the Jupyter notebooks for the course/project.

### Requirements

* Python 3.12
* VS Code
* VS Code Python extension
* VS Code Jupyter extension

### Create the Python environment

Open a terminal and navigate to the notebooks folder:

```
cd notebooks
```

Create a virtual environment using Python 3.12:

```
python3.12 -m venv .venv
```

On macOS, if python3.12 is not found, you may need to use:

```
/opt/homebrew/bin/python3.12 -m venv .venv
```

### Activate the environment
macOS / Linux

```
source .venv/bin/activate
```

Windows

```
.venv\Scripts\activate
```

### Install the required packages

Install the dependencies listed in requirements.txt:

```
python -m pip install -r requirements.txt
```

This will also install ipykernel, which is required to run the notebooks in VS Code.

### Select the notebook kernel in VS Code

Open a .ipynb notebook in VS Code.

Click the kernel selector in the upper-right corner and select:

```
.venv
```

or the Python interpreter located at:

```
notebooks/.venv/bin/python
```

On Windows, it will be:

```
notebooks\.venv\Scripts\python.exe
```

Make sure the selected Python version is 3.12.

### Run the notebook

Once the .venv environment is selected as the kernel, you can run the notebook cells normally.

Project structure

The folder should look approximately like this:

notebooks/
├── .venv/              # Local environment — do not share/commit
├── usecase1
├── usecase2
├── requirements.txt
└── README.md

