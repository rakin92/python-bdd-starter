## Python Behavior Driven Testing
[![Build Status](https://travis-ci.org/rakin92/python-bdd-starter.svg?branch=master)](https://travis-ci.org/rakin92/python-bdd-starter)

"*In software engineering, behavior-driven development is an Agile software development process that encourages collaboration among developers, QA and non-technical or business participants in a software project.*" - Wiki

### Stack
* Python: [Python3.7](https://www.python.org/)
* Behave: [Behave Test Suite](https://behave.readthedocs.io/en/latest/)
* Selenium: [Selenium Webdriver](https://www.webmd.com/a-to-z-guides/supplement-guide-selenium#1)

### Installation
Always recommand using `virtualenv` when dealing with python.
Setup your virtual environment

```
virtualenv venv
```

Activate virtual env

```
. venv/bin/activate
```

Use the package manager pip to install dependencies from requirements.txt

```
pip install -r requirements.txt
```

### Run the tests

Run tests locally

```
behave
```

If you wish to run headless
```
RUN_HEADLESS=TRUE behave
```

Run test remote in SauceLab
```
IS_REMOTE=TRUE SAUCE_USERNAME=<YOUR_USERNAME> SAUCE_ACCESS_KEY=<YOUR_KEY> behave
```

### Formatting
Python follow the [PEP 8](https://www.python.org/dev/peps/pep-0008/) standard, To maintain we are using [autopep8 package](https://pypi.org/project/autopep8/).

```
autopep8 --in-place --aggressive --aggressive <file_path>
```