# Custom User Database  

This is a customized reusable user model created using Django customizable manager and authentication backend  

## Basic Information
### This user interface utilizes two types of authentication. 
1. JWT Authentication with RESTful API using access and refresh token
2. HTTP Session Authentication 


## Installation

This application is created in Python 3.6 using Linux
* Simply download this repository
* Before running, "cd" into this project directory and type "pwd" in Linux terminal and copy the output of "pwd" command
* Open "1_setup_environment.sh", replace the path in "home_dir" variable with the output of "pwd" 
* Then run the commands below

```bash
source 1_setup_environment.sh      # This file automates python env, setup environment variables, and clear database. 
pip install requirements.txt
cd app
python manage.py makemigrations; python manage.py migrate; python manage.py runserver

```

## Usage

```python
import foobar

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```

## Contributing

This is written by Kevin Lin
Pull requests are welcome.
