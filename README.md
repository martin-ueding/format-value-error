# Format Value and Error

Formats value and error in a sensible way.

## Description

The LaTeX package `siunitx` can format numbers from `1.3e-7 +- 0.4e-7` into
`1.3(4) \cdot 10^{-7}` or alternatively into `1.3 \pm 0.4 \cdot 10^{-7}`,
depending on the package options chosen. The number of digits must match. If
one just dumps in floating point numbers from a computer program, they will
likely not have the same number of digits. Also the 

## License

[MIT/Expat](https://opensource.org/licenses/MIT)

## Implementations

- Octave
- Python 3
- R

## Usage

The functions always have the parameters “value” and “error”, these are the
floating point value and error. The “error digits” controls the number of
significant digits in the error, the number of digits of the value is derived
from this.

## Examples

| Value     | Error     | Formatted          | siunitx rendered         |
| --------- | --------- | ------------------ | ------------------------ |
| `123.4`   | `2.34`    | `123 +- 2`         | `123(2)`                 |
| `-123.4`  | `0.34`    | `-123.4 +- 0.3`    | `-123.4(3)`              |
| `-0.5e-9` | `0.04e-9` | `-5.0 +- 0.4 e-10` | `-5.0(4) \cdot 10^{-10}` |
