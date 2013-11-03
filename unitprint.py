#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright © 2012-2013 Martin Ueding <dev@martin-ueding.de>
# Licensed under The MIT License

import math
import logging

logger = logging.getLogger(__name__)

__docformat__ = "restructuredtext en"

class Quantity(object):
    def __init__(self, value, error=None, digits=3, error_digits=1):
        if value == 0:
            value_log = 0
        else:
            value_log = int(math.floor(math.log(abs(value), 10)))

        if error is None or error == 0:
            self.value_mantissa = ("{:."+str(digits-1)+"f}").format(value * 10**(- value_log))
            self.error_mantissa = None
            self.exponent = value_log
        else:
            error_log = int(math.floor(math.log(abs(error), 10)))

            difference = value_log - error_log

            value_dis = value * 10**(- value_log)
            error_dis = error * 10**(-difference - error_log)
            exp = value_log

            error_digits = digits - 1 + max(difference, 0)
            value_digits = error_digits

            self.value_mantissa = ("{:."+str(value_digits)+"f}").format(value_dis)
            self.error_mantissa = ("{:."+str(error_digits)+"f}").format(error_dis)
            self.exponent = exp

    def to_siunitx(self):
        if self.error_mantissa is None:
            if self.exponent == 0:
                return "{}".format(self.value_mantissa)
            else:
                return "{}e{}".format(self.value_mantissa, self.exponent)
        else:
            if self.exponent == 0:
                return "{} +- {}".format(self.value_mantissa, self.error_mantissa)
            else:
                return "{} +- {} e{}".format(self.value_mantissa, self.error_mantissa, self.exponent)

def siunitx(value, error=None, **kwargs):
    if hasattr(value, "__iter__"):
        if error is None:
            return [Quantity(v, None, **kwargs).to_siunitx() for v in value]
        else:
            return [Quantity(v, e, **kwargs).to_siunitx() for v, e in zip(value, error)]
    else:
        q = Quantity(value, error, **kwargs)
        return q.to_siunitx()


def format(value, error=None, unit=None, lit=None, latex=False):
    """
    Formats the given value and error in a human readable form. If an error is
    supplied, it will calculate the relative error. If a literature value is
    given, the deviation from the canonical value is calculated and the error
    is given as a ratio and in the number of standard deviations.

    :param value: Value itself
    :type value: float
    :param error: Error of the value
    :type error: None or float
    :param unit: Physical unit
    :type unit: None or str
    :param lit: Canonical value
    :type lit: None or float
    :return: Formatted output
    :rtype: str
    """

    parts = []


    if unit is not None:
        parts.append(unit)

    if error is not None:
        parts.append("({:.0%})".format(error/value))

    if lit is not None:
        lit_parts = []
        lit_parts.append("{:+.0%}".format((value-lit)/lit))
        if error is not None:
            lit_parts.append("{:+.1f}σ".format((value-lit)/error))
        parts.append("[" + ", ".join(lit_parts) + "]")

    return ' '.join(parts)
