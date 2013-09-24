#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright © 2013 Martin Ueding <dev@martin-ueding.de>
# Licensed under The GNU Public License Version 2 (or later)

import unittest

import unitprint

class TestQuantity(unittest.TestCase):
    def test_init_1(self):
        q = unitprint.Quantity(1.23)
        self.assertEqual(q.value_mantissa, "1.23")
        self.assertIs(None, q.error_mantissa)
        self.assertEqual(q.exponent, 0)

    def test_init_2(self):
        q = unitprint.Quantity(1.23, 1.23)
        self.assertEqual(q.value_mantissa, "1.23")
        self.assertEqual(q.error_mantissa, "1.23")
        self.assertEqual(q.exponent, 0)

    def test_init_3(self):
        q = unitprint.Quantity(12.3, 1.23)
        self.assertEqual(q.value_mantissa, "1.230")
        self.assertEqual(q.error_mantissa, "0.123")
        self.assertEqual(q.exponent, 1)

    def test_init_4(self):
        q = unitprint.Quantity(123, 1.23)
        self.assertEqual(q.value_mantissa, "1.2300")
        self.assertEqual(q.error_mantissa, "0.0123")
        self.assertEqual(q.exponent, 2)

    def test_init_5(self):
        q = unitprint.Quantity(1.23, 12.3)
        self.assertEqual(q.value_mantissa, "1.23")
        self.assertEqual(q.error_mantissa, "12.30")
        self.assertEqual(q.exponent, 0)

    def test_to_siunitx_1(self):
        q = unitprint.Quantity(1.23)
        self.assertEqual("1.23", q.to_siunitx())

    def test_to_siunitx_2(self):
        q = unitprint.Quantity(1.23, 1.23)
        self.assertEqual("1.23 +- 1.23", q.to_siunitx())

    def test_to_siunitx_3(self):
        self.assertEqual("1.230 +- 0.123 e1", unitprint.siunitx(12.3, 1.23))

if __name__ == '__main__':
    unittest.main()
