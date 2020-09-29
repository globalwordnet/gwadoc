#!/usr/bin/env python3

from setuptools import setup

setup(
    name='gwadoc',
    version='0.1.0',
    description=('Documentation for sense relations '
                 'for the Open Multilingual Wordnet'),
    #long_description=long_description,
    url='https://github.com/globalwordnet/gwadoc',
    author='GWA Documentation Working Group',
    author_email='bond@ieee.org',
    license='CC-BY 4.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Documentation',
    ],
    keywords='wordnet linguistics',
    packages=[
        'gwadoc'
    ],
    install_requires=[
    ],
    extras_require={
        "build": [
            'jinja2',
            'docutils',
            'pygments',
        ]
    }
)

