#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright © 2013-2014 Martin Ueding <dev@martin-ueding.de>
# Licensed under The MIT License

import numpy as np
import unittest

import unitprint

class TestQuantity(unittest.TestCase):
    def test_init_value_1(self):
        q = unitprint.Quantity(1.23)
        self.assertEqual(q.value_mantissa, "1.23")
        self.assertIs(None, q.error_mantissa)
        self.assertEqual(q.exponent, 0)

    def test_init_error_2(self):
        q = unitprint.Quantity(1.23, 1.23)
        self.assertEqual(q.value_mantissa, "1")
        self.assertEqual(q.error_mantissa, "1")
        self.assertEqual(q.exponent, 0)

    def test_init_error_3(self):
        q = unitprint.Quantity(12.3, 1.23)
        self.assertEqual(q.value_mantissa, "12")
        self.assertEqual(q.error_mantissa, "1")
        self.assertEqual(q.exponent, 0)

    def test_init_error_4(self):
        q = unitprint.Quantity(123, 1.23)
        self.assertEqual(q.value_mantissa, "123")
        self.assertEqual(q.error_mantissa, "1")
        self.assertEqual(q.exponent, 0)

    def test_init_error_5(self):
        q = unitprint.Quantity(3.14189, 0.00234)
        self.assertEqual(q.value_mantissa, "3.142")
        self.assertEqual(q.error_mantissa, "0.002")
        self.assertEqual(q.exponent, 0)

    def test_init_error_6(self):
        q = unitprint.Quantity(1.23e-6, 1.3e-7)
        self.assertEqual(q.value_mantissa, "1.2")
        self.assertEqual(q.error_mantissa, "0.1")
        self.assertEqual(q.exponent, -6)

    def test_to_siunitx_1(self):
        q = unitprint.Quantity(1.23)
        self.assertEqual("1.23", q.to_siunitx())

    def test_to_siunitx_4(self):
        q = unitprint.Quantity(1234.5)

    def test_to_siunitx_2(self):
        q = unitprint.Quantity(1.23, 1.23)
        self.assertEqual("1 +- 1", q.to_siunitx())

    def test_to_siunitx_3(self):
        self.assertEqual("12 +- 1", unitprint.siunitx(12.3, 1.23))

    def test_negative(self):
        q = unitprint.Quantity(-12.3, 1.23)
        self.assertEqual(q.value_mantissa, "-12")
        self.assertEqual(q.error_mantissa, "1")
        self.assertEqual(q.exponent, 0)

    def test_siunitx_array_loop(self):
        x = np.array([1, 2, 3])
        out = unitprint.siunitx(x)

    def test_zero(self):
        q = unitprint.Quantity(0)
        self.assertEqual(q.value_mantissa, "0.00")
        self.assertEqual(q.exponent, 0)

    def test_zero_error(self):
        unitprint.siunitx(1.0, 0.0)

    def test_negative_error(self):
        unitprint.siunitx(1.0, -0.5)

if __name__ == '__main__':
    unittest.main()
