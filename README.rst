========
Karenina
========

Cookie cutter template for happy internal tools and business app development with django.


Content
-------

*All happy teams resemble one another, but each unhappy teams is unhappy in its own way.*

* Django 1.7
* PostgreSQL
* Foundation CSS Framework
* Ready to use Grunt pipeline
* Vagrant/Docker development setup


Quick start
--------------

Prerequisites:
===========

* `Vagrant <https://docs.vagrantup.com/v2/installation/>`_
* `Docker <https://docs.docker.com/installation/#installation>`_


Setup
===========


.. code-block:: bash

    host$ vagrant up --debug
    host$ vagrant ssh

    vagrant$ npm install 
    vagrant$ bower install
    vagrant$ grunt build
    vagrant$ tox migrate 
    vagrant$ tox  # default: runserver 0.0.0.0:8000 
                  # (host access from http://localhost:9000)


Few more commands
=================

.. code-block:: bash

    vagrant$ grunt serve         # build, watch for css changes, and run django dev server
    vagrant$ tox -e test         # run tests
    vagrant$ tox -e prod shell   # run shell with production env and settings


License
=======

Public Domain. (No copyright, no rights, no license, do whatever you need)
