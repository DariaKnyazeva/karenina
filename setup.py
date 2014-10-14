#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='django-viewsite',
    version='0.7.0',
    author='Mikhail Podgurskiy',
    author_email='kmmbvnr@gmail.com',
    description='Cookie cutter for business app development with django',
    long_description=open('README.rst').read(),
    license='MIT License',
    platforms=['Any'],
    keywords=['django', ],
    url='http://github.com/viewflow/viewsite',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'Django>=1.6',
        'django-compressor',
        'django-extra-views',
    ],
    packages=find_packages(),
    include_package_data=True
)
