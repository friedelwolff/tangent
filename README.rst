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

Configure settings in the file `.env`, with at least these fields:

.. code::

  SECRET_KEY = ARANDOMSECRETKEY
  API_AUTH_URL = http://...../api-token-auth/
  API_URL = http://...../api/

Alternative methods for configuring (such as environment variables) are
possible. Consult the documentation for `python-decouple`.

Initialise the database:

.. code:: bash

  ./manage.py migrate
  ./manage.py createcachetable

To run the tests:

.. code:: bash

  ./manage.py test
