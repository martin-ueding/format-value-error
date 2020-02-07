# Copyright © 2017 Martin Ueding <martin-ueding.de>
# Licensed under the MIT/Expat license.

format.val.err <- function(value, error, error.digits = 1, allowed.hang = 3) {
    if (value == 0) {
        value.log <- 0
    }
    else {
        value.log <- floor(log10(abs(value)))
    }

    error.log <- floor(log10(abs(error)))

    difference <- value.log - error.log

    value.dis <- value * 10^(-value.log)
    error.dis <- error * 10^(-difference - error.log)
    exponent <- value.log

    if (abs(value.log) > allowed.hang) {
        here.digits <- error.digits - 1 + max(difference, 0)
        format <- sprintf('%%.%if', here.digits)
        value.mantissa <- sprintf(format, value.dis)
        error.mantissa <- sprintf(format, error.dis)
    }
    else {
        here.digits <- max(error.digits - 1 - error.log, 0)
        format <- sprintf('%%.%if', here.digits)
        value.mantissa <- sprintf(format, value)
        error.mantissa <- sprintf(format, error)
        exponent <- 0
    }

    if (exponent == 0) {
        return(sprintf('%s +- %s', value.mantissa, error.mantissa))
    }
    else {
        return(sprintf('%s +- %s e%i', value.mantissa, error.mantissa, exponent))
    }
}

tests <- list(
              c(123.4, 2.34),
              c(-123.4, 0.34),
              c(-0.5e-9, 0.04e-9)
              )

for (test in tests) {
    val <- test[1]
    err <- test[2]
    print(sprintf('(%g) (%g) → (%s)', val, err, format.val.err(val, err)))
}
