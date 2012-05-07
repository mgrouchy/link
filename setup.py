#!/usr/bin/env python
import sys
import os
from link import __version__

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
    name='link',
    version='.'.join(str(x) for x in __version__),
    description='',
    url='http://mikegrouchy.com/link',
    author='Mike Grouchy',
    author_email='mgrouchy@gmail.com',
    install_requires=['certifi==0.0.8',
                'chardet==1.0.1',
                'httplib2==0.7.4',
                'oauth2==1.5.211',
                'requests==0.11.2',
                'requests-oauth==0.3.0',
                'simplejson==2.5.0',
                'wsgiref==0.1.2'],
    packages=['link', ],
    license=open('LICENSE').read(),
    long_description='',
)
