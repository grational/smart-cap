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
    'url': 'https://github.com/grational/smart-cap',
    'download_url': 'https://github.com/grational/smart-cap/archive/1.10.0.tar.gz',
    'author_email': 'giuseppe.ricupero@italiaonline.it',
    'install_requires': ['regex', 'pytest','jellyfish'],
    'packages': ['TextFilter'],
    'scripts': [],
}

setup(**config)
