# Syllables: A fast syllable estimator for Python

[![Latest PyPI version](https://img.shields.io/pypi/v/syllables.svg)](https://pypi.python.org/pypi/syllables)
[![Python CI](https://github.com/prosegrinder/python-syllables/workflows/Python%20CI/badge.svg?branch=main)](https://github.com/prosegrinder/python-syllables/actions?query=workflow%3A%22Python+CI%22)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/b8f26e0833ae4698b927614e64fd91b4)](https://www.codacy.com/app/ProseGrinder/python-syllables?utm_source=github.com&utm_medium=referral&utm_content=prosegrinder/python-syllables&utm_campaign=Badge_Grade)

Syllables is a fast, simple syllable estimator for Python. It's intended for use in places where
speed matters. For situations where accuracy matters, please consider the
[cmudict](https://github.com/prosegrinder/python-cmudict) Python library instead.

## Installation

`syllables` is available on PyPI. Simply install it with `pip`:

    $ pip install syllables

You can also install it from source:

    $ git clone https://github.com/prosegrinder/python-syllables.git
    Cloning into 'python-syllables'...
    ...

    $ cd python-syllables
    $ python setup.py install
    ...

## Usage

Syllables provides a single function, estimate, which estimates the number fo syllables in a single word.

    >>> import syllables
    >>> syllables.estimate('estimate')
    4
    >>> syllables.estimate('syllables')
    3

## Credits

Built on or modeled after the following open source projects:

- [One Bloke: Counting Syllables Accurately in Python on Google App Engine](http://www.onebloke.com/2011/06/counting-syllables-accurately-in-python-on-google-app-engine/)
