Cheese Freezer
==============

## About

Cheese Freezer helps you freeze your project's requirements by fetching them (through PIP) 
and uploading back to a cheese shop of your choice (see http://github.com/disqus/chishop).

## Install

    $ pip install cheese-freezer

## Usage

First you need to define an alternative shop in your .pypirc. For example:

    # ~/.pypirc
    [distutils]
    index-servers = myshop

    [myshop]
    repository = http://example.chishop.me/
    username = my_username
    passsword = my_password

Then just run:

    $ cheese-freezer myshop requirements.pip

and watch :)

## Author

Łukasz "lqc" Rekucki (<lrekucki+github@gmail.com>)
