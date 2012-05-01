#!/usr/bin/env python

from link import __version__

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='link',
    version='.'.join(str(x) for x in __version__),
    description='',
    url='https://github.com/mgrouchy/link',
    author='Mike Grouchy',
    author_email='mgrouchy@gmail.com',
    install_requires=[],
    packages=['link', ],
    license='MIT',
    long_description='',
)
