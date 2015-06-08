Django Animals
============

[![Build Status](https://travis-ci.org/stonelasley/django-animals.svg)](https://travis-ci.org/stonelasley/django-animals)

A small app intended to help me track pet records

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install django-animals

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/stonelasley/django-animals.git#egg=animals

TODO: Describe further installation steps (edit / remove the examples below):

Add ``animals`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'animals',
    )

Add the ``animals`` URLs to your ``urls.py``

.. code-block:: python

    urlpatterns = patterns('',
        ...
        url(r'^animals/', include('animals.urls')),
    )

Before your tags/filters are available in your templates, load them by using

.. code-block:: html

	{% load animals_tags %}


Don't forget to migrate your database

.. code-block:: bash

    ./manage.py migrate animals


Usage
-----

TODO: Describe usage or point to docs. Also describe available settings and
templatetags.


Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    mkvirtualenv -p python2.7 django-animals
    make develop

    git co -b feature_branch master
    # Implement your feature and tests
    git add . && git commit
    git push -u origin feature_branch
    # Send us a pull request for your feature branch

In order to run the tests, simply execute ``tox``. This will install two new
environments (for Django 1.6 and Django 1.7) and run the tests against both
environments.
