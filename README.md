# Syllables: A fast syllable estimator for Python

[![Latest PyPI version](https://img.shields.io/pypi/v/syllables.svg)](https://pypi.python.org/pypi/syllables)

[![Latest Travis CI build status](https://travis-ci.org/prosegrinder/python-syllables.svg?branch=master)](https://travis-ci.org/prosegrinder/python-syllables)

[![Latest Codacy Coverage Report](https://api.codacy.com/project/badge/Grade/a4cd7e19a37d4e578160d3c3e3448101)](https://www.codacy.com/app/ProseGrinder/python-syllables?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=prosegrinder/python-syllables&amp;utm_campaign=Badge_Grade)

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

* [One Bloke: Counting Syllables Accurately in Python on Google App Engine](http://www.onebloke.com/2011/06/counting-syllables-accurately-in-python-on-google-app-engine/)
