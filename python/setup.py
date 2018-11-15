# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'SmartCap',
    'description': 'SmartCap is a tool that change the case of the input italian business name from whatever to smart case.',
    'version': '1.10.3',
    'author': 'Giuseppe Ricupero',
    'url': 'https://dl.dropboxusercontent.com/u/892871/IOL-smart-cap.jar',
    'download_url': 'https://dl.dropboxusercontent.com/u/892871/IOL-smart-cap.jar',
    'author_email': 'giuseppe.ricupero@italiaonline.it',
    'install_requires': ['regex', 'pytest','jellyfish'],
    'packages': ['TextFilter'],
    'scripts': [],
}

setup(**config)
