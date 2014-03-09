#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

# use requirements.txt for dependencies
with open('requirements.txt') as f:
    required = map(lambda s: s.strip(), f.readlines())

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='webmention-basic',
    version='0.1.0',
    description='Trivial webmention receiver, wsgi or cgi',
    long_description=readme,
    install_requires=required,
    author='Paul Oppenheim',
    author_email='paul@pauloppenheim.com',
    url='https://github.com/pauloppenheim/webmention-basic',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
