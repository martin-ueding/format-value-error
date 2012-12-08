#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright © 2012 Martin Ueding <dev@martin-ueding.de>

import unittest

__docformat__ = "restructuredtext en"

class UnitprintTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)
