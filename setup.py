#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright © 2012-2014 Martin Ueding <dev@martin-ueding.de>
# Licensed under The MIT License

from setuptools import setup, find_packages

setup(
    author = "Martin Ueding",
    author_email = "dev@martin-ueding.de",
    description = "Prints physical measurements",
    #license = "GPL3",
    name = "unitprint",
    py_modules = ["unitprint"],
    url = "http://martin-ueding.de/projects/python-unitprint",
    version = "1.0",
    test_suite='unitprint-test',
)
