### Table of Contents  
---------------------

- [Before Start](#before-you-start)
- [Quick Start](#quick-start)
    + [Clone repo](#clone-repo)
    + [Goto the base directory](#goto-the-base-directory)
    + [Create virtual environment and install all required packages](#create-virtual-environment-and-install-all-required-packages)
    + [Run the project](#run-the-project)
    + [See project in action](#see-project-in-action)


# Before you start
----------------------------
Hello! Welcome to the Strativ assigment repo. This `readme.md` file will guide you to run the project in your local machine. The section [Quick Start](#quick-start) has all the required steps to run the project. Before that, please read the following notes:

- A SQLite database is provided with pre-populated data.
- An user is provided with `username: admin` and `password: p123p123`.
- If you would like to delete the database and populate it again, just follow the steps in [Quick Start](#quick-start) section till [Run the project](#run-the-project) and then run the command: `python manage.py populate_database`
- You would also need to create a user for yourself manually if you choose to delete the database. To create user (superuser) run the following command: `python manage.py createsuperuser`


# Quick Start
-----------------
In order to run the project, please pursue the following steps. I assume you are using `unix based operating system` and you have `python 3` installed. 


#### Clone repo
--------------------
First of all, clone this git repository to your local machine. Open your terminal and run the command
```
git clone https://github.com/prantoamt/strativ-restcountries.git
```

#### Goto the base directory
------------------------------------
After cloning the repo, goto the django project's base directory by executing the following command: 
```
cd strativ-restcountries/app/
```

#### Create virtual environment and install all required packages
-----------------------------------------------------------------
Now, create a python virtual environment, activate it and install all required packages listed in `requirements.txt`. Execute the following commands to do so:
```
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### Run the project
-------------------
There is a run.sh file inside this directory where all neccessary commands are provided to run the project. Execute the following commands to run the .sh file:
```
chmod +x ./run.sh
./run.sh
```

### See project in action
-------------------------
Congratulations! you have successfully run the project in development server. You can access the project at `8000` port.
Open your browser and goto the url: `127.0.0.1:8000/countries/`, You will be redirected to Login page. Please use: `username: admin` and `password:p123p123`. After successfull login, you will be redirected to country list page where you can test your requirements.
