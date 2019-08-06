# PyCon Africa 2019 Tutorial Outline
## Setup/Prereqs
-  Python 3.5 or later should work, but 3.6 will give you f-strings
-  Git & do basic Git config (find chapter)
-  A Github account
-  Create a virtual environment; I'll be using `virtualenvwrapper`, but use what you're comfortable with
-  `pip install` IN your virtual environment: 
    -  OpenPyXL
    -  pytest
    -  jupyter (optional, but very useful for beginners who don't have a text editor they like)
-  Able to navigate *your* computer from the command line:
    +  navigate & create directories
    +  Git will be done from the command line

## Sequence
-  Introduction
    +  Who am I? Why am I teaching this?
    +  Who are you all? Who's not from Ghana? Where are you from?
-  Quick groundwork lecture on software engineering vs programming
    -  Emphasis on working with a team and code reliability
    -  You can start to use these skills now on your own projects
*  Project Introduction
    -  Simple spreadsheet transformation
    -  Intended as a practical starting point
    -  Timesheet data (how common are time sheets and time tracking in different parts of Africa?)
-  Basic Python
    -  Be sure to point out `dir()` and `help()`
    -  String, List, Tuple, Dict (collections)
    -  Basic functions (Hello {name} function)
    -  imports; `import OpenPyXL`
*  Git
    -  `git init`
    -  `git status`
    -  `git add`
    -  `git commit` & `git commit -m`
    -  `git checkout -b`
    -  `git log`
-  Github
    -  We'll deal with remotes the "easy" way first (let Github tell us how), then `git remote -v`
    -  `git push` & `git pull`

## 15 minute Break

## Testing, Documentation, Refactoring
*  Testing
    -  Why Testing: the BIG picture
        +  Automated -> CI/CD/CD
    -  Pytest vs unittest
    -  What to test and how?
    -  Let's make sure our code is behaving as expected
-  Functions
-  Document Your Functions
-  Test Your Functions
    +  pytest
    +  unittest: built in to Python
    +  Doctests: `pytest --doctest-modules`
        *  Great for testing code snippets in your docs
        *  Not heavily used in software engineering
    +  "Standard" tests with pytest

## Discussion of Deployment & Dependency Management and Development Environment
*  Dependency Management
    -  Remember having to create a virtual environment? And having to install that stuff?
    -  `requirements.txt`
    -  This area is changing
        +  Pipenv vs venv vs venvwrapper
*  Deployment
    -  What does it mean?


## Q&A 
