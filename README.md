# Syllables: A fast syllable estimator for Python

[![Latest PyPI version](https://img.shields.io/pypi/v/syllables.svg)](https://pypi.python.org/pypi/syllables)
[![Python CI](https://github.com/prosegrinder/python-syllables/workflows/Python%20CI/badge.svg?branch=main)](https://github.com/prosegrinder/python-syllables/actions?query=workflow%3A%22Python+CI%22)

Syllables is a fast, simple syllable estimator for Python. It's intended for use
in places where speed matters. For situations where accuracy matters, please
consider the [cmudict](https://github.com/prosegrinder/python-cmudict) Python
library instead.

## Installation

`syllables` is available on PyPI. Simply install it with `pip`:

```bash
pip install syllables
```

## Usage

Syllables provides a single function, estimate, which estimates the number of
syllables in a single word.

```python
>>> import syllables
>>> syllables.estimate('estimate')
4
>>> syllables.estimate('syllables')
3
```

## Credits

Built on or modeled after the following open source projects:

- [One Bloke: Counting Syllables Accurately in Python on Google App Engine](http://www.onebloke.com/2011/06/counting-syllables-accurately-in-python-on-google-app-engine/)
