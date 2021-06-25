### Table of Contents  
---------------------

- [Before you start](#before-you-start)
- [Quick Start](#quick-start)
    + [Clone repo](#clone-repo)
    + [Goto the base directory](#goto-the-base-directory)
    + [Create virtual environment and install all required packages](#create-virtual-environment-and-install-all-required-packages)
    + [Run the project](#run-the-project)
    + [See project in action](#see-project-in-action)
- [Api](#api)
    + [`/api/api-token-auth/`](#--api-api-token-auth--)
    + [`/api/countries/`](#--api-countries--)
    + [`/api/countries/{country_id}/`](#--api-countries--country-id---)
    + [`/api/countries/{country_id}/neighbouring-countries/`](#--api-countries--country-id--neighbouring-countries--)
    + [`/api/languages/{language_id}/countries/`](#--api-languages--language-id--countries--)
    + [Api Security](#api-security)
    + [Api Specifications](#api-specifications)



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


# Api
-----
The following api end-points have been created to perform actions asked in the question. <br/>
**Note: These end-points are secured with token authentication. They will not perform actions for unauthorized users.** 
### `/api/api-token-auth/`
 Actions:
  - POST: returns token for requested user.
  - Example request body: {'username': 'admin', 'password': 'p213p123'}
  - Example response: {'token': 'd46828fb1f0325bf46b7a6de78880aef5557daa9'}
 
### `/api/countries/`
Actions:
 - GET: returns list of all countries.
 - GET (name in query params): returns countries which have queried `name` in their name.
 
### `/api/countries/{country_id}/`
The country_id here is the uuid of a specific country.
 Actions:
  - GET: returns details of a specific country.
  - POST: creates a new country.
  - PUT: updates an existing country fully.
  - PATCH: updates an existing country partially.
  - DELETE: deletes an existing country.
  
### `/api/countries/{country_id}/neighbouring-countries/`
The country_id here is the uuid of a specific country.
 Actions:
    GET: returns a list of neighbouring countries of a specific country.
    
### `/api/languages/{language_id}/countries/`
The language_id here is the uuid of a specific language.
 Actions:
    GET: returns a list of countries who speaks a specific language.

### Api Security
All the End-points are secured. You must send token in header for each request. An example request is provided below:
```
curl -X GET http://127.0.0.1:8000/api/countries/ -H 'Authorization: Token d46828fb1f0325bf46b7a6de78880aef5557daa9'
```

## Api Specifications
A full api-specifications of all end-points are provied in [docs/api_specifications/api_specifications.yaml](https://github.com/prantoamt/strativ-restcountries/blob/main/docs/api_specification/api_specifications.yaml). It is written in `openapi: 3.0.0`.

