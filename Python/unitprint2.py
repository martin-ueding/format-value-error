# cop

import math

def unitprint(value, error, value_digits=3, error_digits=1, allowed_hang=3):
    if value == 0:
        value_log = 0
    else:
        value_log = int(math.floor(math.log(abs(value), 10)))

    if error is None or error == 0:
        if abs(value_log) > allowed_hang:
            value_mantissa = ("{:."+str(digits-1)+"f}").format(value * 10**(- value_log))
            error_mantissa = None
            exponent = value_log
        else:
            value_mantissa = ("{:."+str(max(digits-1 - value_log, 0))+"f}").format(value)
            error_mantissa = None
            exponent = 0
    else:
        error_log = int(math.floor(math.log(abs(error), 10)))

        difference = value_log - error_log

        value_dis = value * 10**(- value_log)
        error_dis = error * 10**(-difference - error_log)
        exp = value_log

        if abs(value_log) > allowed_hang:
            here_digits = error_digits - 1 + max(difference, 0)

            value_mantissa = ("{:."+str(here_digits)+"f}").format(value_dis)
            error_mantissa = ("{:."+str(here_digits)+"f}").format(error_dis)
            exponent = exp
        else:
            here_digits = max(error_digits - 1 -error_log, 0)

            value_mantissa = ("{:."+str(here_digits)+"f}").format(value)
            error_mantissa = ("{:."+str(here_digits)+"f}").format(error)
            exponent = 0

    if error_mantissa is None:
        if exponent == 0:
            return "{}".format(value_mantissa)
        else:
            return "{}e{}".format(value_mantissa, exponent)
    else:
        if exponent == 0:
            return "{} +- {}".format(value_mantissa, error_mantissa)
        else:
            return "{} +- {} e{}".format(value_mantissa, error_mantissa, exponent)


if __name__ == '__main__':
    for val, err in [
        (123.4, 2.34),
        (-123.4, 0.34),
        (-0.5e-9, 0.04e-9),
    ]:
        print('({}) ({}) → ({})'.format(val, err, unitprint(val, err)))
