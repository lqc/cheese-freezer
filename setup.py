# -*- coding: utf-8
import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname), "rb").read().decode('utf-8')

setup(
    name = "cheese-freezer",
    version = "0.0.2",
    author = u"Łukasz Rekucki",
    author_email = "lrekucki@gmail.com",
    description = ("Upload helper for your local PyPI mirror"),
    license = "BSD",
    keywords = "pypi chishop upload mirror",
    url = "http://github.com/lqc/cheese-freezer/",
    packages=["cheese_freezer"],
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ],
    entry_points="""
    [console_scripts]
    cheese-freezer = cheese_freezer:main
    """
)
