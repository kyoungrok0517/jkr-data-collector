#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from codecs import open


def readme():
    with open('README.md', 'r', encoding='utf-8') as f:
        return f.read()

setup(
    name='jcollector',
    version='0.0.1',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    url='https://github.com/kyoungrok0517/jkr-data-collector',
    license='',
    description='KJang\'s personal data collector',
    long_description=readme(),
    author='Kyoung-Rok Jang',
    author_email='kyoungrok.jang@gmail.com',

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'Click',
        'tweepy'
    ],
    entry_points='''
        [console_scripts]
        jcollector=main:cli
    ''',
    zip_safe=False
)
