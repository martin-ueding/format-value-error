#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright © 2012 Martin Ueding <dev@martin-ueding.de>

import math

__docformat__ = "restructuredtext en"

digits = 3
"""
Number of digits to print. This can be overwritten.
"""

def format(value, error=None, unit=None, lit=None):
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

    if error is None:
        format_string = "{:."+str(digits-1)+"e}"
        parts.append(format_string.format(value))
    else:
        value_log = int(math.floor(math.log(value, 10)))
        error_log = int(math.floor(math.log(error, 10)))

        difference = value_log - error_log
        exp = 0

        if difference >= 0:
            value_dis = value * 10**(difference - value_log)
            error_dis = error * 10**(- error_log)
            exp = error_log
        else:
            value_dis = value * 10**(- value_log)
            error_dis = error * 10**(difference - error_log)
            exp = value_log

        format_string = "({:."+str(digits-1)+"f} ± {:."+str(digits-1)+"f})e{:+d}"
        parts.append(format_string.format(value_dis, error_dis, exp))

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

if __name__ == '__main__':
    print format(1.23, 1.23)
    print format(12.3, 1.23)
    print format(790e-9, 10e-9, "m")
    print format(12.3, 1.23, lit=14.0)
    print format(12.3, 1.23, "V", lit=10.0)
    print format(12.3, lit=10.0)
