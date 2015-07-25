#!/usr/bin/env python

from __future__ import with_statement
import sys
from setuptools import setup, find_packages

long_description = ""

setup(
    name='ifilter',
    version="0.2",
    description='ifilter is a command line tool for interactive filtering of pipes.',
    long_description=long_description,
    author='Stefan Hudelmaier',
    author_email='hudelmaier@gmail.com',
    url='https://github.com/stefan-hudelmaier/ifilter',
    download_url='https://github.com/stefan-hudelmaier/ifilter/tarball/0.2',
    keywords=["shell", "pipe", "filter", "interactive"],
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'ifilter = ifilter:main',
        ]
    },
    classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'Operating System :: Unix',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.5',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Topic :: System :: Systems Administration'
    ],
)
