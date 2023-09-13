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
#### models - contains base classes used for this project
Classes in the model:
#### `Client` - This is the class containing the clients information
* Basic Fields and Utility fields defined
* `def __str__(self)` - String representation of the client name, provice and uniqueId
* `def get_absolute_url(self)` - get url of client detail, slug
* `def save(self, *args, **kwargs)` - Autosave function definition

#### `Invoice` - This is the class containing the Invoice inormation
* Basic fields, utility fields and related field(client foreign key)
* `def __str__(self)` - String representation of the number and uniqueId
* `def get_absolute_url(self)` - get url of slug
* `def save(self, *args, **kwargs)` - Autosave function definition

#### `Product` - This is the class containing the products and services information
* Basic fields, utility fields and related field(client foreign key)
* `def __str__(self)` - String representation of the product title and uniqueId
* `def get_absolute_url(self)` - get url of slug
* `def save(self, *args, **kwargs)` - Autosave function definition

#### `Settings` - This is the class containg the settings about the company
* Basic fields, utility fields
* `def __str__(self)` - String representation of the client name, provice and uniqueId
* `def get_absolute_url(self)` - get url of client detail, slug
* `def save(self, *args, **kwargs)` - Autosave function definition


[functions.py](bitinvoice_01/functions.py) - Function definition for emailing invoice to the client
* `def emailInvoiceClient(to_email, from_client, filepath)` - For emailing invoice function

[forms.py](bitinvoice_01/forms.py) - Control form for information input from the front-end view
#### forms - contains classes used for controlling form input
#### `DateInput(forms.DateInput)` - Used to input date
#### `UserLoginForm(forms.ModelForm)` - Class for user log in at the login page
#### `ClientForm(forms.ModelForm)` - Class for client input form
#### `ProductForm(forms.ModelForm)` - Class for product input form
#### `InvoiceForm(forms.ModelForm)` - Invoice details input form
* `def __init__(self, *args, **kwargs)` - Initializing base model
#### `SettingsForm(forms.ModelForm)` - Company settings details input form
#### `ClientSelectForm(forms.ModelForm)` - Client selection form
* `def clean_client(self)` - client removal from the form

[urls.py](bitinvoice_01/urls.py) - Contails urls for respective paths

[views.py](bitinvoice_01/views.py) - Definition of the views rendered
#### views - views rendered/requested
* `def anonymous_required(function=None, redirect_url=None)` - Definition for checking if one is logged in or not to be able to access dashboard, and invoice
* `def login(request)` - Log in request
* `def dashboard(request)` - Dashboard request definition
* `def index(request)` - landing page request definition
* `def about(request)` - about page request definition
* `def invoices(request)` - Invoice view  request definition
* `def products(request)` - Product view request definition
* `def clients(request)` - Client view request definition
* `def logout(request)` - Logout request
* `def createInvoice(request)` - Create invoice
* `def createBuildInvoice(request, slug)` - Build invoice
* `def viewPDFInvoice(request, slug)` - View Invoice in pdf
* `def viewDocumentInvoice(request, slug)` - view document invoice
* `def emailDocumentInvoice(request, slug)` - email invoice document
* `def deleteInvoice(request, slug)` - Delete invoice request
* `def companySettings(request)' - company settings view request

## Bugs
No known bugs at this time. 

## Authors
* Chiemeka Ifemegbulem - [Github](https://github.com/chiemekaifemegbulem)

* Bamigbopa Oluwafikayomi - [Github](https://github.com/faykey)
* Felix Too - [Github](https://github.com/felixtoo48) 

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
