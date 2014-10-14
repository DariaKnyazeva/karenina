========
Karenina
========

Cookie cutter template for happy internal tools and business app development with django.


Content
-------

* Django 1.7
* PostgreSQL
* Foundation CSS Framework
* Ready to use Grunt pipeline
* Vagrant/Docker development setup


Quick start
===========

*All happy teams resemble one another, but each unhappy teams is unhappy in its own way.*

Prerequisites:
--------------

* `Vagrant <https://docs.vagrantup.com/v2/installation/>`_
* `Docker <https://docs.docker.com/installation/#installation>`_


Setup
-----


.. code-block:: bash

    host$ vagrant up --debug
    host$ vagrant ssh

    vagrant$ npm install 
    vagrant$ bower install
    vagrant$ tox -e dev runserver

