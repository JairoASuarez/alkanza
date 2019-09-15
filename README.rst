poem generator
===============

Terminal application to generate random poems from a grammar.

Usage
-----

::

  usage: poem_generator [-h] [-g GRAMMAR_PATH] [-s START_RULE]
  
  optional arguments:
    -h, --help            show this help message and exit
    -g GRAMMAR_PATH       Grammar file path. Default value: grammar.txt
    -s START_RULE         Start rule. Default value: <POEM>

Structure
---------

Makefile
  Tasks to initialize the project and create distributable versions of it. It works on Linux.

Pipfile
  Pipenv configuration file.

Development
-----------

Requirements
^^^^^^^^^^^^

#. Python 3. The project was created using Python 3.5, but it should also
   work with newer versions.
#. `Pipenv <https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv>`_.
   Packages and virtual environment manager.
#. Make. The Makefile includes useful goals to initialize the project
   and create a bundle to distribute it

Make goals
^^^^^^^^^^

init
  Install the packages required by the project.

dist
  Create a bundle of the project using PyInstaller in zip format.
