# BITInvoice
The BITinvoice project is a user friendly web platform created to provide invoicing services for freelancers,startups and business owners.BITinvoice services allows users to create and send invoices digitally.

#### Functionalities of the project:
* Sign In and open dashboard
* Create a new invoice
* Update, Delete and existing invoice
* Search function
* Clients and Products and Services view
* Sending Invoice to client via email

## Table of Content
* [Environment](#environment)
* [Installation](#installation)
* [File Descriptions](#file-descriptions)
* [Usage](#usage)
* [Bugs](#bugs)
* [Authors](#authors)
* [License](#license)

## Environment
This project is interpreted/tested on Ubuntu 20.04 LTS using Django (version 4.2.4)

## Installation
* To get started, install python3 development tools on your virtual machine.
* `sudo apt-get update`
* `sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib`
* Setup postgre database: `sudo -u postgres psql` (Create database, create user and grant all priviledges, alter encoding and timezone role)
* Install virtual environment and install django
* `sudo -H pip3 install --upgrade pip` then `sudo -H pip3 install virtualenv`
* Create directory and install django 
* `mkdir project_portfolio && cd project_portfolio`
* `virtualenv bitinvoiceenv`
* `source bitinvoiceenv/bin/activate`
* Install packages: `pip install django` and `pip install psycopg2`
* Create a new django project called bitinvoice: `django-admin startproject bitinvoice`
* `cd bitinvoice` and edit settings file with Database details
* Run django app: `python manage.py makemigrations` then `python manage.py migrate`
* Create a superuser: `python manage.py createsuperuser`
* Collect static: `python manage.py collectstatic`
* Run app: `python manage.py runserver 0.0.0.0:5000`
* Start the app bitinvoice: `python manage.py startapp bitinvoice_01`

## File Descriptions
[models.py](bitinvoice_01/models.py) - This are the base models for my project, the entry point to the project. 
Classes in the model:
#### `Client` - This is the class containing the clients information
* Basic Fields and Utility fields defined
* `def __str__(self)` - String representation of the client name, provice and uniqueId
* `def get_absolute_url(self)` - get url of client detail, slug
* `def save(self, *args, **kwargs)` - Autosave function definition

#### `Invoice` - This is the class containing the Invoice inormation

#### `Product` - This is the class containing the products and services information

#### `Settings` - This is the class containg the settings about the company


#### `models/` directory contains classes used for this project:
[base_model.py](/models/base_model.py) - The BaseModel class from which future classes will be derived
* `def __init__(self, *args, **kwargs)` - Initialization of the base model
* `def __str__(self)` - String representation of the BaseModel class
* `def save(self)` - Updates the attribute `updated_at` with the current datetime
* `def to_dict(self)` - returns a dictionary containing all keys/values of the instance

Classes inherited from Base Model:
* [amenity.py](/models/amenity.py)
* [city.py](/models/city.py)
* [place.py](/models/place.py)
* [review.py](/models/review.py)
* [state.py](/models/state.py)
* [user.py](/models/user.py)

#### `/models/engine` directory contains File Storage class that handles JASON serialization and deserialization :
[file_storage.py](/models/engine/file_storage.py) - serializes instances to a JSON file & deserializes back to instances
* `def all(self)` - returns the dictionary __objects
* `def new(self, obj)` - sets in __objects the obj with key <obj class name>.id
* `def save(self)` - serializes __objects to the JSON file (path: __file_path)
* ` def reload(self)` -  deserializes the JSON file to __objects

#### `/tests` directory contains all unit test cases for this project:
[/test_models/test_base_model.py](/tests/test_models/test_base_model.py) - Contains the TestBaseModel and TestBaseModelDocs classes
TestBaseModelDocs class:
* `def setUpClass(cls)`- Set up for the doc tests
* `def test_pep8_conformance_base_model(self)` - Test that models/base_model.py conforms to PEP8
* `def test_pep8_conformance_test_base_model(self)` - Test that tests/test_models/test_base_model.py conforms to PEP8
* `def test_bm_module_docstring(self)` - Test for the base_model.py module docstring
* `def test_bm_class_docstring(self)` - Test for the BaseModel class docstring
* `def test_bm_func_docstrings(self)` - Test for the presence of docstrings in BaseModel methods

## Bugs
No known bugs at this time. 

## Authors
* Samuel Chiemeka - [Github](https://github.com/chiemekaifemegbulem)

* Bamigbopa Oluwafikayomi - [Github](https://github.com/faykey)
* Felix Too - [Github](https://github.com/felixtoo48) 

Second part of Airbnb: Joann Vuong
## License

MIT License

`Copyright (c) 2023 Chiemeka`
  `Ifemegbulem`

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
