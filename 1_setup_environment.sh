#!/bin/bash


# ----------------- REQUIRES USER INPUT -------------------
home_dir='/mnt/c/Users/Kevin\ Lin/Desktop/new/'


# ----------------- REQUIRES USER INPUT -------------------
python_dir='env/bin/python'
python_pip_dir='env/bin/pip'

# Set Python Environment Locations
python_env="${home_dir}${python_dir}"
python_pip_env="${home_dir}${python_pip_dir}"


# Rename Python Executors
alias python=$python_env
alias pip=$python_pip_env

# Shortcuts
alias h='cd /mnt/c/Users/Kevin\ Lin/Desktop/new/;'
alias 1='source 1_setup_environment.sh'

alias mm='python manage.py makemigrations'
alias m='python manage.py migrate'
alias r='python manage.py runserver'
alias c='python manage.py createsuperuser'
alias t='python manage.py test'  # python manage.py test users.testing.tests.TestAbstractUser



# Checking if enviroment works. 
python --version
pip -V


# Remove Migration files and Database
database="app/db.sqlite3"


# if test -f $database; then  # if database file exists, then remove it  
# 	rm $database
# 	echo '-----DATABASE REMOVED-----'
# 	rm /mnt/c/Users/Kevin\ Lin/Desktop/new/app/users/migrations/0*
# fi 



# Testing
