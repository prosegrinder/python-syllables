# -*- coding: utf-8 -*-

from os import path

from setuptools import setup

# Version
with open(path.join(path.dirname(__file__), 'syllables', 'VERSION')) as version_file:
    VERSION = version_file.read().strip()
# Long Description
with open(path.join(path.dirname(__file__), 'README.md')) as readme_file:
    LONG_DESCRIPTION = readme_file.read()


setup(
    name="syllables",
    version=VERSION,
    url="https://github.com/prosegrinder/python-syllables",

    author="David L. Day",
    author_email="dday376@gmail.com",

    description="A Python package for estimating the number of syllables in a word.",
    long_description=LONG_DESCRIPTION,

    packages=[
        'syllables'
    ],
    package_dir={'syllables': 'syllables'},
    package_data={
        '': ['LICENSE', '*.md', '*.rst', 'MANIFEST.in'],
    },
    include_package_data=True,

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
