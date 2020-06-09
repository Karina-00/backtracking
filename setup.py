#!/usr/bin/env python

from setuptools import setup

setup(
    name='kkbacker',
    version='0.1',
    py_modules=['backer'],
    install_requires=[
        'Click',
        'tabulate'
    ],
    entry_points='''
        [console_scripts]
        kkbacker=backer.__main__:cli
    ''',
)
