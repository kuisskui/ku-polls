## Ku-Polls
Web application for polls and surveys at Kasetsart University, written in Python using Django. It is based on the [Django Tutorial project][django-tutorial], with additional functionality.


This application is part of the [Individual Software Process](https://cpske.github.io/ISP) course at [Kasetsart University](https://ku.ac.th).

## How to Install and Run
The computer must have Python version 3.9

# How to install
clone the https://github.com/kuisskui/ku-polls.git in your directory.
```
  git clone https://github.com/kuisskui/ku-polls.git ku-polls
```
go to ku-polls and install the package as a virtual environment following these commands.
```
  cd ku-polls
  python -m venv venv
  
  (if you are mac)
  source ./venv/bin/activate
  
  (if you are window)
  venv\Scripts\activate
  
  pip install -r requirements.txt
  python manage.py migrate
  python manage.py loaddata data/polls.json data/users.json
```
last step, get the SECRET_KEY [here](https://djecrety.ir/) then open the sample.env file to fill the SECRET_KEY in line two and change that file name to .env

# How to run
before you run the server you must activate the virtual environment first(can notice by (venv) in front of the prompt)
command to activate the virtual environment
```
  (if you are mac)
  source ./venv/bin/activate
  
  (if you are window)
  venv\Scripts\activate
```
then run the server only one command
```
  python manage.py runserver
```
## Demo account

# admin account
|admin|Username|Password|
|-----|--------|--------|
|1|admid|1234|

# user account
|admin|Username|Password|
|-----|--------|--------|
|1    |Pikachu |Pikachu.2002|
|2    |Raichu  |Raichu.2002|

## Project Documents

All project documents are in the [Project Wiki](../../wiki/Home)

- [Vision Statement](../../wiki/Vision%20Statement)
- [Requirements](../../wiki/Requirements)
- [Project Plan](../../wiki/Development%20Plan)
- [Iteration 1 Plan](../../wiki/Iteration%201%20Plan)
- [Iteration 2 Plan](../../wiki/Iteration%202%20Plan)
- [Iteration 3 Plan](../../wiki/Iteration%203%20Plan)
- [Task Board](https://github.com/users/kuisskui/projects/3/views/2?layout=board)

[django-tutorial]: https://docs.djangoproject.com/en/4.1/intro/tutorial01/
