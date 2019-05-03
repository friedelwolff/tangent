Tangent assignment
==================

A Django application to consume the given API.

Requirements
------------
Developed on Django 2.2 with Python 3.7. Should work on earlier versions, but
this is untested. For more detailed requirements, see requirements/base.txt
for running this application.

Installing
----------
Create a virtualenv, for example:

.. code:: bash

  python3 -m venv env
  . env/bin/activate

Then install the dependencies:

.. code:: bash

  pip install -r requirements/base.txt

Initialise the database:

.. code:: bash

  ./manage.py migrate
