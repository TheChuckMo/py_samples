# py_samples
Python Samples

# requirements 
   - [python 3.4+](https://www.python.org/)
   - 

# setup 
  1. Clone project into your projects directory
  1. Create a python3 virtual environment 
    - Venv will isolate module installs to just the project you're working on
    - Keeps your base install clean, and version locking based on project
  1. Install additional modules from the requirements file 
    
```bash
mkdir ~/projects # or code or whatever.
cd ~/projects 
git clone git@github.com:TheChuckMo/py_samples.git
cd py_samples
python3 -m venv py3venv
source ./py3venv/bin/activate
# --> (py3venv) <--
pip install requests
# begin testing
```

# python virtual environment
```bash
# Deactivate py3venv
deactivate

# Activate py3venv
cd projects/py_samples
source ./py3venv/bin/activate
```

# optional
  - [Virtualenv Wrapper](https://virtualenvwrapper.readthedocs.io) - Utilities for managing python virtual environments