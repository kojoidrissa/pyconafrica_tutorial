# Outline
## Setup/Prereqs
-  Python 3.5 or later should work, but 3.6 will give you f-strings
-  Git & do basic Git config (find chapter)
-  A Github account
-  Create a virtual environment; I'll be using `virtualenvwrapper`, but use what you're comfortable with
-  `pip install` IN your virtual environment: twilio; pytest
-  Able to navigate *your* computer from the command line:
    +  navigate & create directories
    +  Some Git & Heroku tools will be done from CLI

### Follow Up
-  Twilio trial account: https://www.twilio.com/try-twilio
-  Twilio Python Quickstart (for reference): https://www.twilio.com/docs/sms/quickstart/python
-  Heroku account and tools: Project Creation and setup

## Sequence
-  Quick groundwork lecture on software engineering vs programming
    -  Emphasis on working with a team and code reliability
    -  You can start to use these skills now on your own projects
-  Basic Python
    -  Be sure to point out `dir()` and `help()`
    -  String, List, Tuple, Dict (collections)
    -  Basic functions (Hello {name} function)
    -  imports; `import random as rnd`
    -  `input` for early die-roller
    -  Die Roller Function?
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
*  Documentation
    -  Back to the Hello World & Die Roller Functions; add docstrings
    -  Reminder: `help()` uses those docstrings
    -  Documentation is also for Future You and your teammates
*  Testing
    -  Why Testing: the BIG picture
        +  Automated -> CI/CD/CD
    -  Pytest vs unittest
    -  What to test and how?
    -  Let's make sure our die roller is behaving as expected
*  Dependency Management
    -  Remember having to create a virtual environment? And having to install that stuff?
    -  `requirements.txt`
    -  This area is changing
        +  Pipenv vs venv vs venvwrapper
*  Deployment
    -  What does it mean?
    -  Today, we'll let Heroku do the heavy lifting
