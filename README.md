# Django-CRM

============

Django CRM is opensource CRM developed on django framework. It has all
the basic features of CRM to start with. We welcome code contributions
and feature requests via github.

This is divided into three parts
1. Backend API [Django CRM](https://github.com/ScriptScallywag/Py-Django-CRM)
2. Frontend UI [React CRM]("Coming soon...")
3. Mobile app [Flutter CRM]("Coming soon...")

## Runcode 

 Runcode is online developer workspace. It is cloud based simple, secure and ready to code workspaces, assuring high performance & fully configurable coding environment. With runcode you can run django-crm(API) with one-click.


- Open below link to create django-crm workspace on [RunCode](https://runcode.io/ "RunCode"). It will cretae django-crm API

    [![RunCode](https://runcode-app-public.s3.amazonaws.com/images/dark_btn.png)](https://runcode.io)

## Docs

Please [Click Here](http://django-crm.readthedocs.io "Click Here") for latest documentation.

## Project Modules
This project contains the following modules:
- Contacts
- Companies
- Leads
- Accounts
- Invoices (todo)
- Cases (todo)
- Opportunity (todo)

## Try for free [here](https://bottlecrm.com/)

## Installation Guide

We recommend ubuntu 20.04. These instructions are verified for ubuntu 20.04.

#### To install system requirments

```
sudo apt update && sudo apt upgrade -y

sudo apt install python-is-python3 xvfb libfontconfig wkhtmltopdf python3-dev python3-pip build-essential libssl-dev libffi-dev python3-venv redis-server redis-tools virtualenv -y
```

#### Install dependencies

##### Optional (based on personal choice)

```
sudo apt update && sudo apt upgrade -y && sudo apt install zsh python3-virtualenv

sh -c ...

pip install virtualenvwrapper

echo "source /home/ubuntu/.local/bin/virtualenvwrapper.sh" >> ~/.zshrc
```

If you want to install postgres, follow https://www.postgresql.org/download/
#### To modify postgresql root password

```
sudo -u postgres psql
ALTER USER postgres WITH PASSWORD 'root';
```

#### Create and activate a virtual environment.
if you installed and configured virtualenv wrapper then use the following
``` 
mkvirtualenv <env_name>
workon <env_name>
```
or else
```
virtualenv venv
source venv/bin/activate
```
Install the project's dependency after activating env

```
pip install -r requirements.txt
```

### Env variables

* Then refer to `env.md` for environment variables and keep those in the `.env` file in the current folder as your project is in.


### Docker / docker-compose
in order to use docker, please run the next commands after cloning repo:
```
docker build -t djcrm:1 -f docker/Dockerfile .
docker-compose -f docker/docker-compose.yml up
```

**Note**: you must have docker/docker-compose installed on your host. 
### next steps


```
python manage.py migrate
python manage.py runserver
```
- Then open http://localhost:8000/swagger/ in your borwser to explore API.


## Start celery worker in another terminal window

celery -A crm worker --loglevel=INFO

### Useful tools and packages

```
pipdeptree # to see pip dependancy tree
black # to format code to meet python coding standards
pip-check -H  # to see upgradable packages
isort # to sort imports in python
```

### Feature requests and bug reports

We welcome your feedback and support, raise github issue if you want to
report a bug or request new feature. we are glad to help.

# Trigger deploy