# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'SmartCap',
    'description': 'SmartCap is a tool that change the case of the input italian business name from whatever to smart case.',
    'version': '0.1.0',
    'author': 'SmartCap',
    'url': 'https://dl.dropboxusercontent.com/u/892871/IOL-smart-cap.jar',
    'download_url': 'https://dl.dropboxusercontent.com/u/892871/IOL-smart-cap.jar',
    'author_email': 'giuseppe.ricupero@polito.it',
    'install_requires': ['regex', 'pytest'],
    'packages': ['TextFilter'],
    'scripts': [],
}

setup(**config)
