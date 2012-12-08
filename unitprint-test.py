#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright © 2012 Martin Ueding <dev@martin-ueding.de>

import unittest
import unitprint

__docformat__ = "restructuredtext en"

class UnitprintTest(unittest.TestCase):
    def setUp(self):
        unitprint.digits = 3

    def test_number(self):
        self.assertEqual(unitprint.format(1.23), "1.23e+00")

    def test_small_number(self):
        self.assertEqual(unitprint.format(0.123), "1.23e-01")

    def test_error(self):
        self.assertEqual(unitprint.format(1.23, 0.123), "(12.30 ± 1.23)e-01 (1.0e-01)")

    def test_small_error(self):
        self.assertEqual(unitprint.format(0.123, 0.123), "(1.23 ± 1.23)e-01 (1.0)")
