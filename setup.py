# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='DS18B20',
    version='0.1.0',
    description='Module for interacting with DS18B20 tempertature sensors on the raspberrry pi',
    long_description=readme,
    author='Wytamma Wirth',
    author_email='wytamma.wirth@me.com',
    url='https://github.com/Wytamma/ds18b20',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)